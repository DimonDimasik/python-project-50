import pytest
from gendiff.scripts.generate_diff import generate_diff
from gendiff.formatters.stylish import format_value


@pytest.fixture
def json_file1():
    return 'tests/tests_data/file1.json'


@pytest.fixture
def json_file2():
    return 'tests/tests_data/file2.json'


@pytest.fixture
def json_empty():
    return 'tests/tests_data/empty.json'


def test_json_generate_diff(json_file1, json_file2):
    expected = ('{\n  - follow: false\n    host: hexlet.io\n'
                '  - proxy: 123.234.53.22\n  - timeout: 50\n'
                  '  + timeout: 20\n  + verbose: true\n}')
    assert generate_diff(json_file1, json_file2) == expected


def test_empty_json_generate_diff(json_empty, json_file2):
    expected = '{\n  + host: hexlet.io\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff(json_empty, json_file2) == expected


@pytest.fixture
def yaml_file1():
    return 'tests/tests_data/file1.yml'


@pytest.fixture
def yaml_file2():
    return 'tests/tests_data/file2.yml'


@pytest.fixture
def yaml_empty():
    return 'tests/tests_data/empty.yml'


def test_yaml_generate_diff(yaml_file1, yaml_file2):
    expected = ('{\n  - follow: false\n    host: hexlet.io\n'
                '  - proxy: 123.234.53.22\n  - timeout: 50\n'
                  '  + timeout: 20\n  + verbose: true\n}')
    assert generate_diff(yaml_file1, yaml_file2) == expected


def test_empty_yaml_generate_diff(yaml_file1, yaml_empty):
    expected = ('{\n  - follow: false\n  - host: hexlet.io\n'
                '  - proxy: 123.234.53.22\n  - timeout: 50\n}')
    assert generate_diff(yaml_file1, yaml_empty) == expected


@pytest.fixture
def json_file21():
    return 'tests/tests_data/file21.json'


@pytest.fixture
def json_file22():
    return 'tests/tests_data/file22.json'


def test_json_generate_diff_nested(json_file21, json_file22):
    expected = ('{\n    common: {\n      + follow: false\n'
                '        setting1: Value 1\n'
                    '      - setting2: 200\n      - setting3: true\n'
                    '      + setting3: null\n'
                    '      + setting4: blah blah\n      + setting5: {\n'
                    '            key5: value5\n        }\n        setting6: {\n'
                    '            doge: {\n              - wow: \n'
                    '              + wow: so much\n'
                    '            }\n            key: value\n          + ops: vops\n'
                    '        }\n'
                    '    }\n    group1: {\n      - baz: bas\n      + baz: bars\n'
                    '        foo: bar\n'
                    '      - nest: {\n            key: value\n        }\n'
                    '      + nest: str\n'
                    '    }\n  - group2: {\n        abc: 12345\n        deep: {\n'
                    '            id: 45\n        }\n    }\n  + group3: {\n'
                    '        deep: {\n'
                    '            id: {\n                number: 45\n'
                    '            }\n'
                    '        }\n'
                    '        fee: 100500\n    }\n}')
    assert generate_diff(json_file21, json_file22) == expected


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(55) == '55'


def test_generate_diff_plain(json_file21, json_file22):
    expected = ("Property 'common.follow' was added with value: false\n"
    "Property 'common.setting2' was removed\n"
    "Property 'common.setting3' was updated. From true to null\n"
    "Property 'common.setting4' was added with value: 'blah blah'\n"
    "Property 'common.setting5' was added with value: [complex value]\n"
    "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
    "Property 'common.setting6.ops' was added with value: 'vops'\n"
    "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
    "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
    "Property 'group2' was removed\n"
    "Property 'group3' was added with value: [complex value]")
    assert generate_diff(json_file21, json_file22, 'plain') == expected


def test_generate_diff_json(json_file1, json_file2):
    expected = ("[\n    {\n        \"action\": \"deleted\",\n"
                "        \"name\": \"follow\",\n"
                "        \"old_value\": false\n    },\n    {\n"
                "        \"action\": \"unchanged\",\n"
                "        \"name\": \"host\",\n"
                "        \"value\": \"hexlet.io\"\n    },\n    {\n"
                "        \"action\": \"deleted\",\n"
                "        \"name\": \"proxy\",\n"
                "        \"old_value\": \"123.234.53.22\"\n"
                "    },\n    {\n"
                "        \"action\": \"changed\",\n"
                "        \"name\": \"timeout\",\n"
                "        \"old_value\": 50,\n        \"new_value\": 20\n"
                "    },\n    {\n"
                "        \"action\": \"added\",\n"
                "        \"name\": \"verbose\",\n"
                "        \"new_value\": true\n    }\n]")
    assert generate_diff(json_file1, json_file2, 'json') == expected
