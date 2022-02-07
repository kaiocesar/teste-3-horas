from src.utils import list_to_string, question1_rule
import pytest


def test_list_to_string_with_invalid_parameter():
    """Sending a invalid parameter"""
    items = None
    with pytest.raises(TypeError) as type_error:
        list_to_string(question1_rule, items)
    expected_msg = 'The function arg should be a function, and list of items.'
    assert type_error.type is TypeError
    assert type_error.value.args[0] == expected_msg


def test_empty_list():
    """Sending a empty list as parameter"""
    items = []
    assert list_to_string(question1_rule, items) == ''


def test_list_with_one_dictionary_to_string_success():
    """Send an list with one dictionary and return a string"""
    items = [{
        "name": "Maria Neusa de Aparecida",
        "cpf": "97905796671",
        "state": "Sao Paulo",
        "value": "1234"
        }]

    result = list_to_string(question1_rule, items)

    assert len(result) == 45
    assert result == 'Maria Neusa97905796671Sao Paulo  1234       \n'


def test_unordered_list():
    """send an unordered list and receive the correct string"""
    items = [{
        "state": "Sao Paulo",
        "cpf": "97905796671",
        "value": "1234",
        "name": "Maria Neusa de Aparecida",
        }]

    result = list_to_string(question1_rule, items)

    assert result == 'Maria Neusa97905796671Sao Paulo  1234       \n'


def test_uncompleted_dictionary():
    """Sending an uncompleted dictionary"""
    items = [{
        "name": "Maria Neusa de Aparecida",
        "cpf": "97905796671",
        }]

    result = list_to_string(question1_rule, items)

    assert result == ''


def test_list_with_two_dictionaries_to_string_success():
    """Send an list with two dictionaries and return a string"""
    items = [
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

    result = list_to_string(question1_rule, items)

    assert len(result) == 90
    assert result == 'Maria Neusa97905796671Sao Paulo  1234       \nRicardo Fon44010762900Rio Grande 567        \n'
