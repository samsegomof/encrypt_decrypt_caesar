import pytest

from main import encrypting


@pytest.mark.parametrize("text", ["abcdefg"])
@pytest.mark.parametrize("shift", [2])
def test_for_single_word(text, shift):
    expected = "cdefghi"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Triangle, cube, cirlce"])
@pytest.mark.parametrize("shift", [10])
def test_for_few_words(text, shift):
    expected = "Dbskxqvo6*melo6*msbvmo"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["1234"])
@pytest.mark.parametrize("shift", [4])
def test_for_string_of_digits(text, shift):
    expected = "5678"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["QWERTY"])
@pytest.mark.parametrize("shift", [8])
def test_for_upper_case(text, shift):
    expected = "YEMZBG"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["!@#$%^&*()_+=:;|/><,.?`~§±][{}"])
@pytest.mark.parametrize("shift", [2])
def test_for_special_chars(text, shift):
    expected = "#B%&'`(,*+a-?<=~1@>.0Ab©³_]}"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [1])
@pytest.mark.parametrize("shift", [0])
def test_wrong_type_of_text(text, shift):
    expected = "Error: Wrong type of text"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["abcd"])
@pytest.mark.parametrize("shift", [-1])
def test_for_negative_shift(text, shift):
    expected = "Error: Shift should be between 0 and 25"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["abcd"])
@pytest.mark.parametrize("shift", [26])
def test_for_over_shift(text, shift):
    expected = "Error: Shift should be between 0 and 25"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [""])
@pytest.mark.parametrize("shift", [0])
def test_for_empty_text(text, shift):
    expected = "Error: Text should be not empty or none"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["   "])
@pytest.mark.parametrize("shift", [0])
def test_for_only_spaces_text(text, shift):
    expected = "Error: Text should not contain only spaces"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [None])
@pytest.mark.parametrize("shift", [2])
def test_for_none_text(text, shift):
    expected = "Error: Text should be not empty or none"


@pytest.mark.parametrize("text", ["Привет"])
@pytest.mark.parametrize("shift", [3])
def test_for_cyrillic_chars(text, shift):
    expected = "Error: Cyrillic characters is not supported"
    result = encrypting(text, shift)

    assert expected == result
