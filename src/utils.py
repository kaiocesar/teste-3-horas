from yaml import safe_load, YAMLError


def complete_space(value):
    space = ''
    if len(value) < 11:
        space = " " * (11 - len(value))
    else:
        value = value[0:11]
    return f"{value}{space}"


def question1_rule(values):
    """Creating fields with 11 spaces and truncate it"""
    final_str = ''
    items = values[1]
    allowed_keys = ['name', 'cpf', 'state', 'value']

    for item in items:
        if (len(item.keys()) == 4
                and sorted(item.keys()) == sorted(allowed_keys)):
            for key in item:
                item[key] = complete_space(item[key])
            final_str += \
                f"{item['name']}{item['cpf']}{item['state']}{item['value']}\n"

    return final_str


def question2_rule(**kwargs):
    pass


def list_to_string(*params):
    """Receive a list and return a concateneted string"""
    if not params:
        raise IndexError(
            'The function args should receive some parameters.')

    if (len(params) < 1 or
        not isinstance(params[1], list)
            or not callable(params[0])):
        raise TypeError(
            'The function arg should be a function, and list of items.'
            )

    return params[0](params)


def get_format_parameters(file):
    """Getting a list of parameters from a file"""
    with open(file, 'r') as stream:
        try:
            return safe_load(stream)
        except YAMLError as exc:
            raise exc
