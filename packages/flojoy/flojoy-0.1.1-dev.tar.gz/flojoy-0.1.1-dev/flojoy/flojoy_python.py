from box import Box
import numpy as np
import traceback
import yaml
import json
import re
from pathlib import Path
import networkx as nx
from redis import Redis
from rq.job import Job
import os
from functools import wraps
from .utils import PlotlyJSONEncoder
import requests
from dotenv import dotenv_values


def get_port():
    try:
        p = dotenv_values()['REACT_APP_BACKEND_PORT']
    except:
        p = '8000'
    return p


port = get_port()

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
BACKEND_HOST = os.environ.get('BACKEND_HOST', 'localhost')
r = Redis(host=REDIS_HOST, port=REDIS_PORT)


class DataContainer(Box):
    '''
    A class that processes various types of data and supports dot assignment

    Learn more: https://github.com/flojoy-io/flojoy-python/issues/4

    Usage
    -----
    import numpy as np

    v = DataContainer()

    v.x = np.linspace(1,20,0.1)
    v.y = np.sin(v.x)
    v.type = 'ordered_pair'

    '''
    allowed_types = ['grayscale', 'matrix', 'dataframe',
                     'image', 'ordered_pair', 'ordered_triple', 'scalar']
    allowed_keys = ['x', 'y', 'z', 't', 'm', 'c', 'r', 'g', 'b', 'a']
    combinations = {
        'x': ['y', 't', 'z'],
        'y': ['x', 't', 'z'],
        'z': ['x', 'y', 't'],
        'c': ['t'],
        'm': ['t'],
        't':  [value for value in allowed_keys if value not in ['t']],
        'r': ['g', 'b', 't', 'a'],
        'g': ['r', 'b', 't', 'a'],
        'b': ['r', 'g', 't', 'a'],
        'a': ['r', 'g', 'b', 't']
    }

    def _ndarrayify(self, value):
        s = str(type(value))
        v_type = s.split("'")[1]

        match v_type:
            case 'int' | 'float':
                value = np.array([value])
            case 'list':
                value = np.array(value)
            case 'dict' | 'box.box.Box':
                for k, v in value.items():
                    value[k] = self._ndarrayify(v)
            case 'numpy.ndarray':
                pass
            case 'NoneType':
                pass
            case _:
                raise ValueError(value)
        return value

    def init_data(self, data_type: str, kwargs: dict):
        match data_type:
            case 'grayscale' | 'matrix' | 'dataframe':
                if 'm' not in kwargs:
                    raise KeyError(
                        'm key must be provided for type "{}"'.format(data_type))
                else:
                    self['m'] = kwargs['m']
            case 'image':
                if 'r' and 'g' and 'b' and 'a' not in kwargs:
                    raise KeyError(
                        'r g b a keys must be provided for type "{}"'.format(data_type))
                else:
                    self['r'] = kwargs['r']
                    self['g'] = kwargs['g']
                    self['b'] = kwargs['b']
                    self['a'] = kwargs['a']
            case 'ordered_pair':
                if 'x' and 'y' not in kwargs.keys():
                    raise KeyError(
                        'x and y keys must be provided for "{}"'.format(data_type))
                else:
                    self['x'] = kwargs['x']
                    self['y'] = kwargs['y']
            case 'ordered_triple':
                if 'x' and 'y' and 'z' not in kwargs:
                    raise KeyError(
                        'x, y and z keys must be provided for "{}"'.format(data_type))
                else:
                    self['x'] = kwargs['x']
                    self['y'] = kwargs['y']
                    self['z'] = kwargs['z']
            case 'scalar':
                if 'c' not in kwargs:
                    raise KeyError(
                        'c key must be provided for type "{}"'.format(data_type))
                else:
                    self['c'] = kwargs['c']
            case _:
                if data_type.startswith('parametric_'):
                    if 't' not in kwargs:
                        raise KeyError(
                            't key must be provided for "{}"'.format(data_type))
                    self['t'] = kwargs['t']
                    t = kwargs['t']
                    is_ascending_order = all(
                        t[i] <= t[i+1] for i in range(len(t) - 1))
                    if is_ascending_order is not True:
                        raise ValueError(
                            't key must be in ascending order')
                    parametric_data_type = data_type.split('parametric_')[
                        1]
                    self.init_data(parametric_data_type, kwargs)
                else:
                    raise ValueError(
                        'Invalid data type "{}"'.format(data_type))

# This function compares data type with the provided key and assigns it to class attribute if matches
    def validate_key(self, data_type, key):
        match data_type:
            case 'ordered_pair':
                if key not in ['x', 'y']:
                    raise KeyError(self.build_error_text(key, data_type))
            case 'grayscale' | 'matrix' | 'dataframe':
                if key not in ['m']:
                    raise KeyError(self.build_error_text(key, data_type))
            case 'image':
                if key not in ['r', 'g', 'b', 'a']:
                    raise KeyError(self.build_error_text(key, data_type))
            case 'ordered_triple':
                if key not in ['x', 'y', 'z']:
                    raise KeyError(self.build_error_text(key, data_type))
            case 'scalar':
                if key not in ['c']:
                    raise KeyError(self.build_error_text(key, data_type))

    def set_data(self, data_type: str, key: str, value, isType: bool):
        if data_type not in self.allowed_types and data_type.startswith('parametric_'):
            if 't' not in self:
                if key != 't':
                    raise KeyError(
                        't key must be provided for "{}"'.format(data_type))
                is_ascending_order = all(
                    value[i] <= value[i+1] for i in range(len(value) - 1))
                if is_ascending_order is not True:
                    raise ValueError(
                        't key must be in ascending order')
                if isType:
                    return
                super().__setitem__(key, value)
                return
            else:
                parametric_data_type = data_type.split('parametric_')[
                    1]
                if key != 't':
                    self.validate_key(
                        parametric_data_type, key)
                if isType:
                    return
                array = []
                for i in range(len(self['t'])):
                    array.append(self._ndarrayify(value))

                super().__setitem__(key, array)
                return
        elif data_type in self.allowed_types:
            self.validate_key(data_type, key)
            if isType:
                return
            super().__setitem__(key, self._ndarrayify(value))
        else:
            raise ValueError(
                'Invalid data type "{}"'.format(data_type))

    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self['type'] = kwargs['type']
        else:
            self['type'] = 'ordered_pair'
        self.init_data(self['type'], kwargs)

    def __getitem__(self, key, **kwargs):
        return super().__getitem__(key)

    def check_combination(self, key, keys, allowed_keys):
        for i in keys:
            if i not in allowed_keys:
                raise ValueError('You cant have %s with %s' % (key, i))

# This function is called when a attribute is assigning to this class
    def __setitem__(self, key, value):
        keys = []
        if key != 'type':
            if 'type' in self:
                self.set_data(self.type, key, value, False)
                return
            else:
                keys = [*self.allowed_keys]
                keys.remove(key)
                has_keys = []
                has_other_keys = False
                for i in keys:
                    if hasattr(self, i):
                        has_keys.append(i)
                        has_other_keys = True
                if has_other_keys:

                    if key in self.combinations.keys():
                        self.check_combination(
                            key, has_keys, self.combinations[key])
                        super().__setitem__(key, value)
                        return
                else:
                    super().__setitem__(key, self._ndarrayify(value))
                    return
        else:
            has_any_key = False
            has_keys = []
            for i in self.allowed_keys:
                if hasattr(self, i):
                    has_keys.append(i)
                    has_any_key = True
            if has_any_key:
                for i in has_keys:
                    self.set_data(value, i, self[i], True)
            super().__setitem__(key, value)

    def build_error_text(self, key: str, data_type: str):
        return 'Invalid key "%s" provided for data type "%s"' % (key, data_type)


def get_flojoy_root_dir():
    home = str(Path.home())
    # TODO: Upate shell script to add ~/.flojoy/flojoy.yaml
    path = os.path.join(home, '.flojoy/flojoy.yaml')
    stream = open(path, 'r')
    yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
    root_dir = ''
    if isinstance(yaml_dict, str) == True:
        root_dir = yaml_dict.split(':')[1]
    else:
        root_dir = yaml_dict['PATH']
    return root_dir


def js_to_json(s):
    '''
    Converts an ES6 JS file with a single JS Object definition to JSON
    '''
    split = s.split('=')[1]
    clean = split.replace('\n', '').replace(
        "'", '').replace(',}', '}').rstrip(';')
    single_space = ''.join(clean.split())
    dbl_quotes = re.sub(r'(\w+)', r'"\1"', single_space).replace('""', '"')
    rm_comma = dbl_quotes.replace('},}', '}}')

    return json.loads(rm_comma)


def get_parameter_manifest():
    root = get_flojoy_root_dir()
    f = open(os.path.join(root, 'src/data/manifests-latest.json'))
    param_manifest = json.load(f)
    return param_manifest['parameters']


def fetch_inputs(previous_job_ids, mock=False):
    '''
    Queries Redis for job results

    Parameters
    ----------
    previous_job_ids : list of Redis job IDs that directly precede this node

    Returns
    -------
    inputs : list of DataContainer objects
    '''
    if mock is True:
        return [DataContainer(x=np.linspace(0, 10, 100))]

    inputs = []

    try:
        for ea in previous_job_ids:
            job = Job.fetch(ea, connection=Redis(
                host=REDIS_HOST, port=REDIS_PORT))

            inputs.append(job.result)
    except Exception:
        print(traceback.format_exc())

    return inputs


def get_redis_obj(id):
    get_obj = r.get(id)
    parse_obj = json.loads(get_obj) if get_obj is not None else {}
    return parse_obj


def handle_loop_params(result, jobset_id):

    data = result['data']
    initial_value = result['params']['initial_value']
    total_iterations = result['params']['total_iterations']
    current_iteration = result['params']['current_iteration']
    step = result['params']['step']
    verdict = result['verdict']

    r_obj = get_redis_obj(jobset_id)
    if len(r_obj):
        special_type_jobs = r_obj['SPECIAL_TYPE_JOBS'] if 'SPECIAL_TYPE_JOBS' in r_obj else {
        }
        loop_jobs = {
            "status": verdict,
            "is_loop_body_execution_finished": False,
            "params": {
                "initial_value": initial_value,
                "total_iterations": total_iterations,
                "current_iteration": current_iteration,
                "step": step
            }
        }
        r.set(jobset_id, json.dumps({
            **r_obj,
            'SPECIAL_TYPE_JOBS': {
                **special_type_jobs,
                'LOOP': loop_jobs,
            }
        }))
    return data, {
        "status": verdict,
        "current_iteration": current_iteration
    }


def handle_conditional_params(result, jobset_id):
    data = result['data']
    direction = result['direction']
    r_obj = get_redis_obj(jobset_id)

    if len(r_obj):
        special_type_jobs = r_obj['SPECIAL_TYPE_JOBS'] if 'SPECIAL_TYPE_JOBS' in r_obj else {
        }
        conditional_jobs = {
            "direction": bool(direction)
        }

        r.set(jobset_id, json.dumps({
            **r_obj,
            'SPECIAL_TYPE_JOBS': {
                **special_type_jobs,
                'CONDITIONAL': conditional_jobs
            }
        }))

    return data


def check_if_loop_exists(params, jobset_id):
    r_obj = get_redis_obj(jobset_id)

    print(r_obj)

    check_special_type_job_status = True if 'SPECIAL_TYPE_JOBS' in r_obj else False

    loop_status = (True if 'SPECIAL_TYPE_JOBS' in r_obj else False) and \
        (True if 'LOOP' in r_obj['SPECIAL_TYPE_JOBS'] else False) and \
        (True if 'status' in r_obj['SPECIAL_TYPE_JOBS']['LOOP'] else False) and \
        (True if r_obj['SPECIAL_TYPE_JOBS']['LOOP']
         ['status'] == 'ongoing' else False)

    conditional_status = (True if 'SPECIAL_TYPE_JOBS' in r_obj else False) and \
        (True if 'CONDITIONAL' in r_obj['SPECIAL_TYPE_JOBS'] else False) and \
        (True if 'type' in r_obj['SPECIAL_TYPE_JOBS']['CONDITIONAL'] else False) and \
        r_obj['SPECIAL_TYPE_JOBS']['CONDITIONAL']['type'] == 'default'

    # conditional_status = conditional_status and r_obj['SPECIAL_TYPE_JOBS']['CONDITIONAL']['type'] == 'default'

    print("loop status: ", loop_status)
    print("conditional status: ", conditional_status)

    if loop_status and not conditional_status:

        params['loop_current_iteration'] = r_obj['SPECIAL_TYPE_JOBS']['LOOP']['params']['initial_value']
        params['loop_total_iteration'] = r_obj['SPECIAL_TYPE_JOBS']['LOOP']['params']['total_iterations']
        params['loop_step'] = r_obj['SPECIAL_TYPE_JOBS']['LOOP']['params']['step']
        params['type'] = 'loop'
        params['current_iteration'] = r_obj['SPECIAL_TYPE_JOBS']['LOOP']['params']['current_iteration']

    return params


def get_additional_info(jobset_id):
    r_obj = get_redis_obj(jobset_id)
    loop_status = (True if 'SPECIAL_TYPE_JOBS' in r_obj else False) and \
        (True if 'LOOP' in r_obj['SPECIAL_TYPE_JOBS'] else False) and \
        (True if 'status' in r_obj['SPECIAL_TYPE_JOBS']['LOOP'] else False)

    if loop_status:
        return {
            'status': r_obj['SPECIAL_TYPE_JOBS']['LOOP']['status'],
            "current_iteration": r_obj['SPECIAL_TYPE_JOBS']['LOOP']['params']['current_iteration']
        }
    return {}


def send_to_socket(data):
    requests.post(
        'http://{}:{}/worker_response'.format(BACKEND_HOST, port), json=data)


def flojoy(func):
    '''
    Decorator to turn Python functions with numerical return
    values into Flojoy nodes.

    @flojoy is intended to eliminate  boilerplate in connecting
    Python scripts as visual nodes

    Into whatever function it wraps, @flojoy injects
    1. the last node's input as an XYVector
    2. parameters for that function (either set byt the user or default)

    Parameters
    ----------
    func : Python function object

    Returns
    -------
    VectorYX object

    Usage Example
    -------------

    @flojoy
    def SINE(v, params):

        print('params passed to SINE', params)

        output = VectorXY(
            x=v[0].x,
            y=np.sin(v[0].x)
        )
        return output

    pj_ids = [123, 456]

    # equivalent to: decorated_sin = flojoy(SINE)
    print(SINE(previous_job_ids = pj_ids, mock = True))
    '''
    @wraps(func)
    # def wrapper(previous_job_ids, mock):
    def wrapper(*args, **kwargs):
        try:
            previous_job_ids, mock = {}, False
            if 'previous_job_ids' in kwargs:
                previous_job_ids = kwargs['previous_job_ids']
            if 'ctrls' in kwargs:
                ctrls = kwargs['ctrls']
            node_id = kwargs['node_id']
            jobset_id = kwargs['jobset_id']
            FN = func.__name__
            # remove this node from redis ALL_NODES key
            r.lrem(jobset_id+'_ALL_NODES', 1, node_id)
            sys_status = '🏃‍♀️ Running python job: ' + FN
            send_to_socket(json.dumps({
                'SYSTEM_STATUS': sys_status,
                'jobsetId': jobset_id,
                'RUNNING_NODE': node_id
            }))
            # Get default command paramaters
            default_params = {}
            func_params = {}
            pm = get_parameter_manifest()
            if FN in pm:
                for param in pm[FN]:
                    default_params[param] = pm[FN][param]['default']
                # Get command parameters set by the user through the control panel
                func_params = {}
                if ctrls is not None:
                    for key, input in ctrls.items():
                        func_params[input['param']] = input['value']

                # Make sure that function parameters set is fully loaded
                # If function is missing a parameter, fill-in with default value
                for key in default_params.keys():
                    if key not in func_params.keys():
                        func_params[key] = default_params[key]

            func_params['jobset_id'] = jobset_id
            func_params['type'] = 'default'

            if FN == 'CONDITIONAL':
                func_params = check_if_loop_exists(func_params, jobset_id)

            node_inputs = fetch_inputs(previous_job_ids, mock)
            result = func(node_inputs, func_params)

            additional_info = get_additional_info(jobset_id)

            if 'type' in result and result['type'] == 'LOOP':
                result, additional_info = handle_loop_params(result, jobset_id)

            if 'type' in result and result['type'] == 'CONDITIONAL':
                result = handle_conditional_params(result, jobset_id)

            send_to_socket(json.dumps({
                'NODE_RESULTS': {
                    'cmd': FN,
                    'id': node_id,
                    'result': result,
                    'additional_info': additional_info
                },
                'jobsetId': jobset_id
            }, cls=PlotlyJSONEncoder))
            all_nodes_length = r.llen(jobset_id + '_ALL_NODES')
            if all_nodes_length == 0:
                send_to_socket(json.dumps({
                    'SYSTEM_STATUS': '🤙 python script run successful',
                    'RUNNING_NODE': '',
                    'jobsetId': jobset_id
                }))
            return result
        except Exception:
            send_to_socket(json.dumps({
                'SYSTEM_STATUS': 'Failed to run: ' + func.__name__,
                'FAILED_NODES': node_id,
                'jobsetId': jobset_id
            }))
            print(traceback.format_exc())
            raise

    wrapper.original = func
    wrapper.original.__qualname__ += ".original"

    return wrapper


def reactflow_to_networkx(elems, edges):
    DG = nx.DiGraph()
    for i in range(len(elems)):
        el = elems[i]
        data = el['data']
        ctrls = data['ctrls'] if 'ctrls' in data else {}
        inputs = data['inputs'] if 'inputs' in data else {}
        label = data['label'] if 'label' in data else {}
        DG.add_node(
            i+1, pos=(el['position']['x'], el['position']['y']), id=el['id'], ctrls=ctrls, inputs=inputs, label=label)
        elems[i]['index'] = i+1
        elems[i]['label'] = el['id'].split('-')[0]
    pos = nx.get_node_attributes(DG, 'pos')

    # Add edges to networkx directed graph
    edge_label_dict = {}

    def get_tuple(edge):
        e = [-1, -1]
        src_id = edge['source']
        tgt_id = edge['target']

        if tgt_id not in edge_label_dict.keys():
            edge_label_dict[tgt_id] = []

        edge_label_dict[tgt_id].append({
            'source': src_id,
            'label': edge['label'] if 'label' in edge else "default",
            'sourceHandle': edge['sourceHandle'],
            'targetHandle': edge['targetHandle']
        })

        # iterate through all nodes looking for matching edge
        for el in elems:
            if 'id' in el:
                if el['id'] == src_id:
                    e[0] = el['index']
                elif el['id'] == tgt_id:
                    e[1] = el['index']
        return tuple(e)

    for i in range(len(edges)):
        el = edges[i]

        # element is an edge
        e = get_tuple(el)
        DG.add_edge(*e)
    # Add labels (commands) to networkx nodes

    labels = {}

    for el in elems:
        # if element is not a node
        labels[el['index']] = el['data']['func']

    nx.set_node_attributes(DG, labels, 'cmd')
    nx.draw(DG, pos, with_labels=True, labels=labels)

    def get_node_data_by_id():
        nodes_by_id = dict()
        for n, nd in DG.nodes().items():
            if n is not None:
                nodes_by_id[n] = nd
        return nodes_by_id
    sort = nx.topological_sort(DG)

    return {'topological_sort': sort, 'getNode': get_node_data_by_id, 'DG': DG, 'edgeInfo': edge_label_dict}
