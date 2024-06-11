import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Capitilize
def test_capitilize_positive():
   string_utils = StringUtils()
   res = string_utils.capitilize("строка")
   assert res == "Строка"


def test_capitilize_positive():
   string_utils = StringUtils()
   res = string_utils.capitilize("string")
   assert res == "String"


def test_capitilize_negative():
   string_utils = StringUtils()
   res = string_utils.capitilize("_____")
   assert res == "_____"


def test_capitilize_negative():
   string_utils = StringUtils()
   res = string_utils.capitilize("   ")
   assert res == "   "


#trim
def test_trim_positive():
   string_utils = StringUtils()
   res = string_utils.trim("     Хорошая погода")
   assert res == "Хорошая погода"


def test_trim_positive():
   string_utils = StringUtils()
   res = string_utils.trim("    Notions  ")
   assert res == "Notions  "


def test_trim_negative():
   string_utils = StringUtils()
   res = string_utils.trim("")
   assert res == ""


@pytest.mark.xfail()
def test_trim_numbers():
   string_utils = StringUtils()
   res = string_utils.trim("46544")
   assert res == "46544"


#list


def test_to_list_positive():
   string_utils = StringUtils()
   res = string_utils.to_list("33,44,55,66")
   assert res == ["33","44","55","66"]


def test_to_list_positive():
   string_utils = StringUtils()
   res = string_utils.to_list("Moscow,Samara,Saratov,Kazan")
   assert res == ["Moscow","Samara","Saratov","Kazan"]


def test_to_list_negative():
   string_utils = StringUtils()
   res = string_utils.to_list("")
   assert res == []


def test_to_list_negative():
   string_utils = StringUtils()
   res = string_utils.to_list("")
   assert res == []


def test_to_list_negative():
   string_utils = StringUtils()
   res = string_utils.to_list("")
   assert res == []


#contains


def test_contains_positive():
   string_utils = StringUtils()
   res = string_utils.contains("pepper", "p")
   assert res == True


def test_contains_positive():
   string_utils = StringUtils()
   res = string_utils.contains("привет", "р")
   assert res == True


def test_contains_positive():
   string_utils = StringUtils()
   res = string_utils.contains("cucumber", "7")
   assert res == False


def test_contains_positive():
   string_utils = StringUtils()
   res = string_utils.contains("abrakadabra ", " ")
   assert res == True


def test_contains_positive():
   string_utils = StringUtils()
   res = string_utils.contains("____??/", "?")
   assert res == True


#delete_symbol
def test_delete_symbol_positive():
   string_utils = StringUtils()
   res = string_utils.delete_symbol("Питон", "т")
   assert res == "Пион"


def test_delete_symbol_positive():
   string_utils = StringUtils()
   res = string_utils.delete_symbol("234-", "-")
   assert res == "234"


def test_delete_symbol_positive():
   string_utils = StringUtils()
   res = string_utils.delete_symbol("Афина", "а")
   assert res == "Афин"


def test_delete_symbol_negative():
   string_utils = StringUtils()
   res = string_utils.delete_symbol(" ", " ")
   assert res == ""


def test_delete_symbol_negative():
   string_utils = StringUtils()
   res = string_utils.delete_symbol("123", "6")
   assert res == "123"   


# starts_with
def test_def_starts_with_positive():
   string_utils = StringUtils()
   res = string_utils.starts_with("Electra", "E")
   assert res == True   


def test_def_starts_with_positive():
   string_utils = StringUtils()
   res = string_utils.starts_with("123678", "1")
   assert res == True


def test_def_starts_with_positive():
   string_utils = StringUtils()
   res = string_utils.starts_with("Микромир", "п")
   assert res == False


def test_def_starts_with_positive():
   string_utils = StringUtils()
   res = string_utils.starts_with(" zuma", " ")
   assert res == True


def test_def_starts_with_positive():
   string_utils = StringUtils()
   res = string_utils.starts_with("//5", "?")
   assert res == False


#end_with


def test_end_with():
   string_utils = StringUtils()
   res = string_utils.end_with("ретромарафон", "н")
   assert res  == True


def test_end_with():
   string_utils = StringUtils()
   res = string_utils.end_with("Google_", "_")
   assert res  == True


def test_end_with():
   string_utils = StringUtils()
   res = string_utils.end_with("723237239>>", ">")
   assert res  == True


def test_end_with():
   string_utils = StringUtils()
   res = string_utils.end_with("  __  ", "?")
   assert res  == False


def test_end_with():
   string_utils = StringUtils()
   res = string_utils.end_with("  8", ".")
   assert res  == False


#is_empty


def test_is_empty():
   string_utils = StringUtils()
   res = string_utils.is_empty("")
   assert res == True


def test_is_empty():
   string_utils = StringUtils()
   res = string_utils.is_empty("   ")
   assert res == True


def test_is_empty():
   string_utils = StringUtils()
   res = string_utils.is_empty("EEEEEEE")
   assert res == False


def test_is_empty():
   string_utils = StringUtils()
   res = string_utils.is_empty("e62863")
   assert res == False


#list_to_string
def test_list_to_string():
   string_utils = StringUtils()
   res = string_utils.list_to_string(["Попугай", "Кеша"])
   assert res == "Попугай, Кеша"


def test_list_to_string():
   string_utils = StringUtils()
   res = string_utils.list_to_string(["56", "66", "76"])
   assert res == "56, 66, 76"


def test_list_to_string():
   string_utils = StringUtils()
   res = string_utils.list_to_string([])
   assert res == ""
