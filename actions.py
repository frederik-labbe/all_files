def action_check_hello_start(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        content = f.read()

    return content.startswith('hello')