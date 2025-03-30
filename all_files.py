import os
from typing import List, Dict
import tomllib

import logging
logging.basicConfig(level=logging.INFO)

from runner import Runner

def load_actions(configs_path: str) -> Dict[str, any]:
    with open(configs_path, 'rb') as f:
        return tomllib.load(f)

def file_iter(root: str, filters: List[str] = []):
    for path in [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(root) for f in filenames]:
        if len(filters) > 0 and not path.endswith(tuple(filters)):
            continue

        yield path

def validate_action_config(action_name: str, action_config: Dict[str, any]) -> None:
    if not 'enabled' in action_config:
            raise ValueError(f'Key "enable" is missing for action {action_name} in config !')

    if not 'root' in action_config:
            raise ValueError(f'Key "root" is missing for action {action_name} in config !')
        
    if not 'filters' in action_config:
        raise ValueError(f'Key "filters" is missing for action {action_name} in config !')
    
    if not 'report_success' in action_config:
        raise ValueError(f'"report_success" is missing for action {action_name} in config !')

def run_actions(actions_config_file: str = './default_actions.toml') -> None:
    actions_config = load_actions(actions_config_file)

    for action_name in actions_config['actions']:
        action_config = actions_config['actions'][action_name]

        if not action_config['enabled']:
            continue

        logging.log(logging.INFO, f'Processing {action_name}...')

        validate_action_config(action_name, action_config)

        for filepath in file_iter(action_config['root'], action_config['filters']):
            Runner(filepath).run(action_name, action_config['report_success'])