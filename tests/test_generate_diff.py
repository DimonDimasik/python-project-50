import pytest
from gendiff.modules.generate_diff import assort, convert, generate_diff


def test_assort():
    assert assort([('+', 'c', '-'),('z', 'a', 'b'), ('1', 'b', '9')]) == [('z', 'a', 'b'), ('1', 'b', '9'), ('+', 'c', '-')]


def test_convert():
    assert convert([('he', 'll', 'o, '), ('wo', 'rl', 'd!!')]) == 'hello, world!'

@pytest.fixture
def json_file1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def json_file2():
    return 'tests/fixtures/file2.json'

def test_generate_diff(json_file1, json_file2):
    expected = (
        r'- follow: false\n'
        r'  host: hexlet.io\n'
        r'- proxy: 123.234.53.22\n'
        r'- timeout: 50\n'
        r'+ timeout: 20\n'
        r'+ verbose: true'
    )
    assert generate_diff(json_file1, json_file2) == expected
