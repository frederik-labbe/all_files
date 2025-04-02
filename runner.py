import logging
import actions

class Runner:
    def __init__(self, filepath, actions_module):
        self._filepath = filepath
        self._actions_module = actions_module if actions_module is not None else actions

    def run(self, action_name: str, report_success: bool) -> bool:
        action_fn_name = f'action_{action_name}'

        if not hasattr(self._actions_module, action_fn_name):
            raise ValueError(f'Action {action_name} does not exist !')

        action_fn = getattr(self._actions_module, action_fn_name)

        if action_fn(self._filepath):
            if report_success:
                logging.info(f'Action {action_name} on file {self._filepath} has succeeded !')
            return True
        else:
            logging.info(f'Action {action_name} on file {self._filepath} has failed !')
            return False
