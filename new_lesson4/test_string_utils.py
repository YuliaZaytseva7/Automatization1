import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Capitilize


@pytest.mark.parametrize("input_str, output_str", [
   ("строка", "Строка"),
   ("string", "String"),
   ("____", "____"),
   ("  ", "  ")
   ])
def test_capitilize(input_str, output_str):
    res = string_utils.capitilize(input_str)
    assert res == output_str


# trim


def test_trim():
    # POSITIVE
    assert string_utils.trim("     Хорошая погода") == "Хорошая погода"
    assert string_utils.trim("    Notions  ") == "Notions  "
    # NEGATIVE
    assert string_utils.trim("") == ""


@pytest.mark.xfail()
def test_trim_numbers():
    string_utils = StringUtils()
    res = string_utils.trim("46544")
    assert res == "46544"


# to_list


@pytest.mark.parametrize("string, delimeter, result", [
   # POSITIVE
   ("33,44,55,66", ",", ["33", "44", "55", "66"]),
   ("Moscow,Samara,Saratov,Kazan", ",",  ["Moscow", "Samara", "Saratov",
                                          "Kazan"]),
   # NEGATIVE
   ("", None, [])
   ])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = string_utils.to_list(string)
    else:
        res = string_utils.to_list(string, delimeter)
    assert res == result


# contains


@pytest.mark.parametrize("string, symbol, result", [
   ("pepper", "p", True),
   ("привет", "р", True),
   ("cucumber", "7", False),
   ("abrakadabra ", " ", True),
   ("____??/", "?", True),
])
def test_contains(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result

# delete_symbol


@pytest.mark.parametrize("string, symbol, result", [
   # POSITIVE
   ("Питон", "т", "Пион"),
   ("234-", "-", "234"),
   ("Афина", "а", "Афин"),
   # NEGATIVE
   (" ", " ", ""),
   ("123", "6", "123"),
])
def test_delite_simbol(string, symbol, result):
    res = string_utils.delete_symbol(string, symbol)
    assert res == result


# starts_with


@pytest.mark.parametrize("string, symbol, result", [
   ("Electra", "E", True),
   ("123678", "1", True),
   ("Микромир", "п", False),
   (" zuma", " ", True),
   ("//5", "?", False),
])
def test_starts_with(string, symbol, result):
    res = string_utils.starts_with(string, symbol)
    assert res == result

# end_with


@pytest.mark.parametrize("string, symbol, result", [
   ("ретромарафон", "н", True),
   ("Google_", "_", True),
   ("723237239>>", ">", True),
   ("  __  ", "?", False),
   ("  8", ".", False),
])
def test_end_with(string, symbol, result):
    res = string_utils.end_with(string, symbol)
    assert res == result

# is_empty


@pytest.mark.parametrize("string, result", [
   ("", True),
   ("  ", True),
   ("TTT", False),
   ("  8", False),
])
def test_is_empty(string, result):
    res = string_utils.is_empty(string)
    assert res == result

# list_to_string


@pytest.mark.parametrize("lst, joiner, result", [
   (["Попугай", "Кеша"], "-", "Попугай-Кеша"),
   ([56, 66, 76], None, "56, 66, 76"),
   ([], None, ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)
    assert res == result
