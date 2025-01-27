from gendiff.modules.generate_diff import assort


def test_assort():
    assert assort(['cotlin', 'rust', 'dart']) == ['dart', 'cotlin', 'rust']