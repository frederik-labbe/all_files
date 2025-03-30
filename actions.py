def action_check_hello(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        content = f.read()

    return content.startswith('hello')