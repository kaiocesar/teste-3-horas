from src.utils import string_to_list, get_format_parameters
import pytest


def test_empty_string():
    """Sending a empty string and receive empty value"""
    str_items = ''
    format_rule = get_format_parameters('src/temp/format-1.yaml')
    result = string_to_list(str_items, format_rule)

    assert sorted(result) == sorted(['cpf', 'name', 'value'])

def test_none_parameters():
    """Sending nullable parameters"""
    with pytest.raises(IndexError) as index_error:
        string_to_list(None, string_to_list)
        
    expected_msg = 'The function parameters should be filled.'
    assert index_error.type is IndexError
    assert index_error.value.args[0] == expected_msg


def test_convert_string_to_list_format1():
    """Sending a string and return a list of items by a format file"""
    str_items = '97905796671Maria Neusa de00001234\n'
    format_rule = get_format_parameters('src/temp/format-1.yaml')
    result = string_to_list(str_items, format_rule)

    assert isinstance(result, dict)
    assert sorted(result.keys()) == sorted(['cpf', 'name', 'value'])
    assert result['cpf'] == '97905796671'
    assert result['name'] == 'Maria Neusa de'
    assert result['value'] == '00001234'


def test_convert_string_to_list_format2():
    """Sending a string and return a list of items by a format file"""
    str_items = '0009790579667100001234Sao Paulo     \n'
    format_rule = get_format_parameters('src/temp/format-2.yaml')
    result = string_to_list(str_items, format_rule)

    assert isinstance(result, dict)
    assert sorted(result.keys()) == sorted(['cpf', 'state', 'value'])
    assert result['cpf'] == '00097905796671'
    assert result['state'] == 'Sao Paulo     '
    assert result['value'] == '00001234'
