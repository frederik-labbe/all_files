def action_extra_bar(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        content = f.read()

    return content.startswith('bar')