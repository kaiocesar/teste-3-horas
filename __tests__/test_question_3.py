from src.utils import list_to_string,\
    question2_rule, get_format_parameters


def test_convert_string_to_list():
    """Sending a string and return a list of items by a format file"""
    str_items = '0009790579667100001234Sao Paulo     \n'
    format_rule = get_format_parameters('src/temp/format-2.yaml')