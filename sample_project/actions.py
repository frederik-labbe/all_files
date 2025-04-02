import logging

def action_custom_foo(filepath: str) -> bool:
    logging.info('Checking if file starts with foo')
    
    with open(filepath, 'r') as f:
        content = f.read()

    return content.startswith('foo')