import sys
import pytest

sys.path.append('..')
from module import check_payload, load_settings

@pytest.fixture(scope='module')
def settings():
    return load_settings('./test_settings.yaml')

def test_check_payload_ignore(settings):
    with pytest.raises(ValueError) as exc_info:
        check_payload('API_KEY="foo"', settings)
    assert 'API_KEY="' in str(exc_info.value)

def test_check_payload_replace(settings):
    payload = 'The ph is a powerful tool'
    expected = 'The myorg is a powerful tool'
    result = check_payload(payload, settings)
    assert result == expected

def test_check_payload_noop(settings):
    payload = 'This is a test'
    result = check_payload(payload, settings)
    assert result == payload