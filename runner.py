import actions

import logging

class Runner:
    def __init__(self, filepath):
        self._filepath = filepath

    def run(self, action_name: str, report_success: bool) -> None:
        action_fn_name = f'action_{action_name}'

        if not hasattr(actions, action_fn_name):
            raise ValueError(f'Action {action_name} does not exist !')

        action_fn = getattr(actions, action_fn_name)

        if action_fn(self._filepath):
            if report_success:
                logging.log(logging.INFO, f'Action {action_name} on file {self._filepath} has succeeded !')
        else:
            logging.log(logging.INFO, f'Action {action_name} on file {self._filepath} has failed !')
