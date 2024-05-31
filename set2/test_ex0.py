import pytest
from exercise0 import add_1, add_5, adder, shout, really_shout, shout_with_a_number

@pytest.mark.parametrize("input_number, expected_result", [(1, 2), (6, 11), (-3, 2), (0.5, 5.5)])
def test_add_5(input_number, expected_result):
    assert add_5(input_number) == expected_result

@pytest.mark.parametrize("input_numbers, expected_result", [([-0.5, -0.5], -1), ([2, 2], 4), ([2, -2], 0)])
def test_adder(input_numbers, expected_result):
    assert adder(*input_numbers) == expected_result

@pytest.mark.parametrize("input_string, expected_result", [("hello", "HELLO"), ("", "")])
def test_shout(input_string, expected_result):
    assert shout(input_string) == expected_result

@pytest.mark.parametrize("input_string, expected_result", [("hello", "HELLO!"), ("", "!"), ("!", "!!")])
def test_really_shout(input_string, expected_result):
    assert really_shout(input_string) == expected_result

@pytest.mark.parametrize("input_string, input_number, expected_result", [("hello", 42, "HELLO 42")])
def test_shout_with_a_number(input_string, input_number, expected_result):
    assert shout_with_a_number(input_string, input_number) == expected_result

def test_minitest():
    from helper import minitest
    
    minitest(add_1, [1], 2)
    minitest(add_5, [1], 6)
    minitest(add_5, [6], 11)
    minitest(add_5, [-3], 2)
    minitest(add_5, [0.5], 5.5)
    minitest(adder, [-0.5, -0.5], -1)
    minitest(adder, [2, 2], 4)
    minitest(adder, [2, -2], 0)
    minitest(shout, ["hello"], "HELLO")
    minitest(really_shout, ["hello"], "HELLO!")
    minitest(really_shout, [""], "!")
    minitest(really_shout, ["!"], "!!")
    minitest(shout_with_a_number, ("hello", 42), "HELLO 42")
