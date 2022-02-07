from src.utils import list_to_string,\
    question2_rule, get_format_parameters


def test_read_file_success():
    """Send a valid yml file and read its parameters"""
    result = get_format_parameters('src/temp/format-1.yaml')
    assert isinstance(result, dict)
    assert 'name' in result
    assert 'length' in result['name']
    assert list(result.keys()) == ['cpf', 'name', 'value']


def test_list_with_one_dictionary_to_string_format1_success():
    """Send an list with one dictionary and return a string"""
    items = [{
        "name": "Maria Neusa de Aparecida",
        "cpf": "97905796671",
        "state": "Sao Paulo",
        "value": "1234"
        }]
    format_rule = get_format_parameters('src/temp/format-1.yaml')
    result = list_to_string(question2_rule, items, format_rule)

    assert len(result) == 34
    assert result == '97905796671Maria Neusa de00001234\n'


def test_list_with_one_dictionary_to_string_format2_success():
    """Send an list with one dictionary and return a string"""
    items = [{
        "name": "Maria Neusa de Aparecida",
        "cpf": "97905796671",
        "state": "Sao Paulo",
        "value": "1234"
        }]
    format_rule = get_format_parameters('src/temp/format-2.yaml')
    result = list_to_string(question2_rule, items, format_rule)

    assert len(result) == 37
    assert result == '0009790579667100001234Sao Paulo     \n'
