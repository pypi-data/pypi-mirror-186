import pytest
from .compare_version import compare_version
from .parse_version import parse_version_string_to_array


@pytest.mark.parametrize("v_0, operator, v_1, kwargs, result",
                         [([1, 2, 3], ">=", [1, 3], dict(), False),
                          ([1, 2, 3], "<", [1, 3], dict(), True),
                          ([1, 2, 3], "==", [1, 2, 3, 0, 0], dict(), True),
                          # 测试 sep
                          ("1.2.3", "<", [1, 3], dict(sep='.'), True),
                          ("n_7.3", "<", [1, 3], dict(sep='.'), True),
                          ("1_2_3", "==", "1_2_3_0_0", dict(sep='_'), True),
                          # 测试 mode
                          ("1_2_3", "==", "1_2_3_4_5", dict(sep='_', mode='short'), True), ])
def test__compare_version(v_0, operator, v_1, kwargs, result):
    assert compare_version(v_0, operator, v_1, **kwargs) == result


@pytest.mark.parametrize("string, sep, result",
                         [("1,2,3", ',', [1, 2, 3]),
                          ("1_2.3", '.', [0]),
                          ("neg", '_', [0])])
def test__parse_version_string_to_array(string, sep, result):
    assert parse_version_string_to_array(string, sep=sep) == result
