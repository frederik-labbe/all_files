import os
import tomllib

import importlib

import logging
logging.basicConfig(level=logging.INFO)

from .runner import Runner

actions = None

def load_action_config(configs_path: str) -> dict[str, any]:
    with open(configs_path, 'rb') as f:
        return tomllib.load(f)

def file_iter(root: str, ext_filters: list[str] = []):
    for path in [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(root) for f in filenames]:
        if len(ext_filters) > 0 and not path.endswith(tuple(ext_filters)):
            continue

        yield path

def validate_action_config(action_name: str, action_config: dict[str, any]) -> None:
    if not 'enabled' in action_config:
        raise ValueError(f'Key "enable" is missing for action {action_name} in config !')

    if not 'root' in action_config:
        raise ValueError(f'Key "root" is missing for action {action_name} in config !')
        
    if not 'ext_filters' in action_config:
        raise ValueError(f'Key "filters" is missing for action {action_name} in config !')
    
    if not 'report_success' in action_config:
        raise ValueError(f'Key "report_success" is missing for action {action_name} in config !')
    
    if not 'stop_on_error' in action_config:
        raise ValueError(f'Key "stop_on_error" is missing for action {action_name} in config !')
    
def register_actions_module(action_module: any) -> None:
    global actions

    actions = action_module

def run_actions(actions_config_file: str = './default_actions.toml') -> None:
    actions_config = load_action_config(actions_config_file)

    for action_name in actions_config['actions']:
        action_config = actions_config['actions'][action_name]

        if not action_config['enabled']:
            continue

        logging.info(f'Processing {action_name}...')

        validate_action_config(action_name, action_config)

        for filepath in file_iter(action_config['root'], action_config['ext_filters']):
            if not Runner(filepath, actions).run(action_name, action_config['report_success']) and action_config['stop_on_error']:
                raise ValueError(f'Error on action {action_name} for file {filepath}, please check !')