from src.utils import get_format_parameters


def test_read_file_success():
    """Send a valid yml file and read its parameters"""
    result = get_format_parameters('src/temp/format-1.yaml')
    assert isinstance(result, dict)
    assert 'name' in result
    assert 'length' in result['name']
    assert list(result.keys()) == ['cpf', 'name', 'value']
