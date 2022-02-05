from src.utils import ArrayToString
import pytest


def test_array_to_string_with_invalid_parameter():
    """Sending a invalid parameter"""
    input = None        
    with pytest.raises(TypeError) as type_error:
        ArrayToString(input)
    
    assert type_error.type is TypeError
    assert type_error.value.args[0] == 'The function arg should be a list.'


def test_array_to_string_success():
    """Send a array and return a string"""
    input = [{
        "name":"Maria Neusa de Aparecida",
        "cpf": "97905796671",
        "state": "Sao Paulo",
        "value": "1234"
        }]

    result = ArrayToString(input)

    assert len(result) == 44
    assert result == 'Maria Neusa97905796671Sao Paulo  1234       '
