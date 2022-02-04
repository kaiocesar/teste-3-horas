from src.utils import ArrayToString


def test_array_to_string_success():
    """Send a array and return a string"""
    input = [{
        "name":"Maria Neusa de Aparecida",
        "cpf": "97905796671",
        "state": "Sao Paulo",
        "value": "1234"
        }]
    result = ArrayToString(input)
    assert result == 'Maria Neusa97905796671234'
