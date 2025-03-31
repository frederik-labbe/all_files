# all_files

## A Python module that centralizes file iteration and applies specific actions to different file branches.

### Configuration:
- Create a file `actions.py` that contains available options. Define those actions likes this:

```python
def action_[action name](filepath: str) -> bool:
    # Function body
```

- Create a file `default_actions.toml` that contains a mapping of desired actions to be applied on specific file branches. E.g.,

```toml
[actions]

[actions.check_hello_start] # Action named "check_hello_start"
enabled = true
root = "." # Current location
ext_filters = [".txt"] # Applies to .txt files
report_success = false # Only report actions that fail
```

### Usage (default):

```python
all_files.run_actions()
```

### Usage (advanced):

```python
import custom_actions_module

all_files.register_action_module(custom_actions_module)

all_files.run_actions('./custom_actions.toml')
```