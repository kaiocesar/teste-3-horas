from yaml import safe_load, YAMLError


def complete_space(value):
    space = ''
    if len(value) < 11:
        space = " " * (11 - len(value))
    else:
        value = value[0:11]
    return f"{value}{space}"


def format_field(value, rule):
    """Custom format string"""
    length = rule['length']
    align = rule['align']
    padding = '0' if rule['padding'] == 'zeroes' else ' '

    if len(value) > length:
        value = value[0:length].strip()

    if len(value) < length:
        space = padding * (length - len(value))
        if align == 'left':
            value = f"{value}{space}"
        else:
            value = f"{space}{value}"
    return value


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


def question2_rule(params):
    """Creating string based on a list and using a format rule"""
    final_str = ''
    items = params[1]
    format_value = params[2]
    for item in items:
        for key in item:
            if key in format_value.keys():
                item[key] = format_field(item[key], format_value[key])
            else:
                item[key] = complete_space(item[key])
        # final_str += \
        #     f"{item['name']}{item['cpf']}{item['state']}{item['value']}\n"
        for format_key in format_value.keys():
            final_str += item[format_key]

    return f"{final_str}\n"


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
