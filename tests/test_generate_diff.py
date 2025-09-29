import pytest
from gendiff.scripts.generate_diff import generate_diff
from gendiff.formatters.stylish import format_value


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
    expected = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff(json_file1, json_file2) == expected


def test_empty_json_generate_diff(json_empty, json_file2):
    expected = '{\n  + host: hexlet.io\n  + timeout: 20\n  + verbose: true\n}'
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
    expected = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff(yaml_file1, yaml_file2) == expected


def test_empty_yaml_generate_diff(yaml_file1, yaml_empty):
    expected = '{\n  - follow: false\n  - host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n}'
    assert generate_diff(yaml_file1, yaml_empty) == expected


@pytest.fixture
def json_file21():
    return 'tests/fixtures/file21.json'


@pytest.fixture
def json_file22():
    return 'tests/fixtures/file22.json'


def test_json_generate_diff_nested(json_file21, json_file22):
    expected = '{\n    common: {\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting3: null\n      + setting4: blah blah\n      + setting5: {\n            key5: value5\n        }\n        setting6: {\n            doge: {\n              - wow: \n              + wow: so much\n            }\n            key: value\n          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n        }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n            }\n        }\n        fee: 100500\n    }\n}'
    assert generate_diff(json_file21, json_file22) == expected


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(55) == '55'


def test_generate_diff_plain(json_file21, json_file22):
    expected = "Property 'common.follow' was added with value: false\nProperty 'common.setting2' was removed\nProperty 'common.setting3' was updated. From true to null\nProperty 'common.setting4' was added with value: 'blah blah'\nProperty 'common.setting5' was added with value: [complex value]\nProperty 'common.setting6.doge.wow' was updated. From '' to 'so much'\nProperty 'common.setting6.ops' was added with value: 'vops'\nProperty 'group1.baz' was updated. From 'bas' to 'bars'\nProperty 'group1.nest' was updated. From [complex value] to 'str'\nProperty 'group2' was removed\nProperty 'group3' was added with value: [complex value]"
    assert generate_diff(json_file21, json_file22, 'plain') == expected
