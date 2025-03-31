# all_files

## A Python module that centralizes file iteration and applies specific actions to different file branches.

### Configuration:
- Fill `actions.py` with potential actions. Define those actions likes this:

```python
def action_[action name](filepath: str) -> bool:
    # Function body
```

- Fill `default_actions.toml` with a mapping of desired actions on specific file branches. E.g.,

```toml
[actions]

[actions.check_hello_start] # Action named "check_hello_start"
enabled = true
root = "." # Current location
ext_filters = [".txt"] # Applies to .txt files
report_success = false # Only report actions that fail
```

### Usage:

```python
all_files.run_actions()
```