from gendiff.modules.generate_diff import assort, convert


def test_assort():
    assert assort(['cotlin', 'rust', 'dart']) == ['dart', 'cotlin', 'rust']
    assert assort([['+', 'c', '-'],['z', 'a', 'b'], ['1', 'b', '9']]) == [['z', 'a', 'b'], ['1', 'b', '9'], ['+', 'c', '-']]


def test_convert():
    assert convert([['he', 'll', 'o, '], ['wo', 'rl', 'd!!!']]) == 'hello, world!'


test_assort()
test_convert()