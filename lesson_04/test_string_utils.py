import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("no_spaces", "no_spaces"),
    ("  много   пробелов  ", "много   пробелов  "),  # trim убирает только слева
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                        # пустая строка
    ("   ", ""),                    # строка из пробелов (должны удалиться все)
    (None, None),                    # None — это вызовет ошибку, но мы её ожидаем
])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    ("12345", "3", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),                # пустая строка не содержит символ
    ("abc", "", False),              # пустой символ — спорный кейс, но по логике False
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaa", "a", ""),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),       # символа нет — строка не должна меняться
    ("", "a", ""),                   # пустая строка
    (None, "a", None),                # None — ожидаем ошибку
])
def test_delete_symbol_negative(string, symbol, expected):
    if string is None:
        with pytest.raises(AttributeError):
            string_utils.delete_symbol(string, symbol)
    else:
        assert string_utils.delete_symbol(string, symbol) == expected
