import pytest

from main import encrypting, decrypting


@pytest.mark.parametrize("text", ["abcdefg"])
@pytest.mark.parametrize("shift", [2])
def test_encrypt_for_single_word(text, shift):
    expected = "cdefghi"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Triangle cube cirlce"])
@pytest.mark.parametrize("shift", [10])
def test_encrypt_for_few_words(text, shift):
    expected = "Dbskxqvo melo msbvmo"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["QWERTY"])
@pytest.mark.parametrize("shift", [8])
def test_encrypt_for_upper_case(text, shift):
    expected = "YEMZBG"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["1234"])
@pytest.mark.parametrize("shift", [4])
def test_encrypt_for_string_of_digits(text, shift):
    expected = "Error: Digits does not supported"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["!@#$%^&*()_+=:;|/><,.?`~§±][{}"])
@pytest.mark.parametrize("shift", [2])
def test_encrypt_for_special_chars(text, shift):
    expected = "Error: Special characters does not supported"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [1])
@pytest.mark.parametrize("shift", [0])
def test_encrypt_wrong_type_of_text(text, shift):
    expected = "Error: Wrong type of text"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Hola amigo"])
@pytest.mark.parametrize("shift", ["hi"])
def test_encrypt_wrong_type_of_shift(text, shift):
    expected = "Error: Wrong type of shift"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["abcd"])
@pytest.mark.parametrize("shift", [-1])
def test_encrypt_for_negative_shift(text, shift):
    expected = "Error: Shift should be between 0 and 25"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["abcd"])
@pytest.mark.parametrize("shift", [26])
def test_encrypt_for_over_shift(text, shift):
    expected = "Error: Shift should be between 0 and 25"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [""])
@pytest.mark.parametrize("shift", [0])
def test_encrypt_for_empty_text(text, shift):
    expected = "Error: Text should be not empty"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["   "])
@pytest.mark.parametrize("shift", [0])
def test_encrypt_for_only_spaces_text(text, shift):
    expected = "Error: Text should not contain only spaces"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [None])
@pytest.mark.parametrize("shift", [2])
def test_encrypt_for_none_text(text, shift):
    expected = "Error: Wrong type of text"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Привет"])
@pytest.mark.parametrize("shift", [3])
def test_encrypt_for_cyrillic_chars(text, shift):
    expected = "Error: Cyrillic characters does not supported"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["cdefghi"])
@pytest.mark.parametrize("shift", [2])
def test_decrypt_for_single_word(text, shift):
    expected = "abcdefg"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Dbskxqvo melo msbvmo"])
@pytest.mark.parametrize("shift", [10])
def test_decrypt_for_few_words(text, shift):
    expected = "Triangle cube cirlce"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["YEMZBG"])
@pytest.mark.parametrize("shift", [8])
def test_decrypt_for_upper_case(text, shift):
    expected = "QWERTY"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["1234"])
@pytest.mark.parametrize("shift", [4])
def test_dencrypt_for_string_of_digits(text, shift):
    expected = "Error: Digits does not supported"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["!@#$%^&*()_+=:;|/><,.?`~§±][{}"])
@pytest.mark.parametrize("shift", [2])
def test_decrypt_for_special_chars(text, shift):
    expected = "Error: Special characters does not supported"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", [1])
@pytest.mark.parametrize("shift", [0])
def test_decrypt_wrong_type_of_text(text, shift):
    expected = "Error: Wrong type of text"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Hi dude"])
@pytest.mark.parametrize("shift", ["hi"])
def test_decrypt_wrong_type_of_text(text, shift):
    expected = "Error: Wrong type of shift"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["abcd"])
@pytest.mark.parametrize("shift", [-1])
def test_decrypt_for_negative_shift(text, shift):
    expected = "Error: Shift should be between 0 and 25"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["Рскгду"])
@pytest.mark.parametrize("shift", [1])
def test_decrypt_for_cyrillic_chars(text, shift):
    expected = "Error: Cyrillic characters does not supported"
    result = decrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["sometext"])
@pytest.mark.parametrize("shift", [None])
def test_encrypt_for_none_shift(text, shift):
    expected = "Error: Wrong type of shift"
    result = encrypting(text, shift)

    assert expected == result


@pytest.mark.parametrize("text", ["sometext"])
@pytest.mark.parametrize("shift", [None])
def test_decrypt_for_none_shift(text, shift):
    expected = "Error: Wrong type of shift"
    result = decrypting(text, shift)

    assert expected == result
