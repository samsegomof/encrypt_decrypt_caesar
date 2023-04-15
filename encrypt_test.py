import pytest

from main import encrypting


@pytest.mark.parametrize("text", ["abcdefg"])
@pytest.mark.parametrize("shift", [2])
def test_should_pass_for_single_word(text, shift):
    expected = "IJKLMNO"
    result = encrypting(text, shift)

    assert expected == result



