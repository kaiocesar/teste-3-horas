from src.utils import list_to_string
import pytest


def test_array_to_string_with_invalid_parameter():
    """Sending a invalid parameter"""
    input = None        
    with pytest.raises(TypeError) as type_error:
        list_to_string(input)
    
    assert type_error.type is TypeError
    assert type_error.value.args[0] == 'The function arg should be a list.'


def test_empty_list():
    """Sending a empty list as parameter"""
    input = []
    assert list_to_string(input) == ''


def test_list_with_one_dictionary_to_string_success():
    """Send an list with one dictionary and return a string"""
    input = [{
        "name":"Maria Neusa de Aparecida",
        "cpf": "97905796671",
        "state": "Sao Paulo",
        "value": "1234"
        }]

    result = list_to_string(input)

    assert len(result) == 44
    assert result == 'Maria Neusa97905796671Sao Paulo  1234       '

def test_unordered_list():
    """send an unordered list and receive the correct string"""
    input = [{
        "state": "Sao Paulo",
        "cpf": "97905796671",
        "value": "1234",
        "name":"Maria Neusa de Aparecida",
        }]

    result = list_to_string(input)

    assert result == 'Maria Neusa97905796671Sao Paulo  1234       '


def test_uncompleted_dictionary():
    """Sending an uncompleted dictionary"""
    input = [{
        "name":"Maria Neusa de Aparecida",
        "cpf": "97905796671",
        }]

    result = list_to_string(input)

    assert result == ''


def test_list_with_two_dictionaries_to_string_success():
    """Send an list with two dictionaries and return a string"""
    input = [
        {
            "name": "Maria Neusa de Aparecida",
            "cpf": "97905796671",
            "state": "Sao Paulo",
            "value": "1234"
        },
        {
            "name": "Ricardo Fontes",
            "cpf": "44010762900",
            "state": "Rio Grande do Sul",
            "value": "567"
        }
    ]

    result = list_to_string(input)

    assert len(result) == 88
    assert result == 'Maria Neusa97905796671Sao Paulo  1234       Ricardo Fon44010762900Rio Grande 567        '
