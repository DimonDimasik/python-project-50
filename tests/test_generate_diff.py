import pytest
from gendiff.modules.generate_diff import key_sort, convert, generate_diff


def test_key_sort():
    assert key_sort([('+', 'c', '-'),('z', 'a', 'b'), ('1', 'b', '9')]) == [('z', 'a', 'b'), ('1', 'b', '9'), ('+', 'c', '-')]


def test_convert():
    assert convert([('he', 'll', 'o, '), ('wo', 'rl', 'd!!')]) == 'hello, world!'

@pytest.fixture
def json_file1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def json_file2():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def json_empty():
    return 'tests/fixtures/empty.json'


def test_json_generate_diff(json_file1, json_file2):
    expected = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'
    assert generate_diff(json_file1, json_file2) == expected


def test_empty_json_generate_diff(json_empty, json_file2):
    expected = '+ host: hexlet.io\n+ timeout: 20\n+ verbose: true'
    assert generate_diff(json_empty, json_file2) == expected


@pytest.fixture
def yaml_file1():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def yaml_file2():
    return 'tests/fixtures/file2.yml'


@pytest.fixture
def yaml_empty():
    return 'tests/fixtures/empty.yml'


def test_yaml_generate_diff(yaml_file1, yaml_file2):
    expected = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'
    assert generate_diff(yaml_file1, yaml_file2) == expected


def test_empty_yaml_generate_diff(yaml_file1, yaml_empty):
    expected = '- follow: false\n- host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50'
    assert generate_diff(yaml_file1, yaml_empty) == expected
