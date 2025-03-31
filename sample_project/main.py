import all_files

import extra_actions

if __name__ == '__main__':
    # Default use case
    all_files.run_actions() # Using local default_actions.toml

    # Custom use case
    all_files.register_actions_module(extra_actions)
    all_files.run_actions('./extra_actions.toml')