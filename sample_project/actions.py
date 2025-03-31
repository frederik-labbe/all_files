def action_custom_foo(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        content = f.read()

    return content.startswith('foo')