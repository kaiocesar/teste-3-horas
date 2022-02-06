from yaml import safe_load, YAMLError


def complete_space(value):
    space = ''
    if len(value) < 11:
        space = " " * (11 - len(value))
    else:
        value = value[0:11]
    return f"{value}{space}"


def particular_rule(values):
    """Creating fields with 11 spaces and truncate it"""
    for key in values:
        values[key] = complete_space(values[key])
    return f"{values['name']}{values['cpf']}{values['state']}{values['value']}"


def list_to_string(items):
    """Receive a list and return a concateneted string"""
    allowed_keys = ['name', 'cpf', 'state', 'value']
    final_str = ''
    if not isinstance(items, list):
        raise TypeError('The function arg should be a list.')

    for item in items:
        if len(item.keys()) == 4 and sorted(item.keys()) == sorted(allowed_keys):
            final_str += particular_rule(item) + "\n"

    return final_str


def get_format_parameters(file):
    """Getting a list of parameters from a file"""
    with open(file, 'r') as stream:
        try:
            return safe_load(stream)
        except YAMLError as exc:
            raise exc
