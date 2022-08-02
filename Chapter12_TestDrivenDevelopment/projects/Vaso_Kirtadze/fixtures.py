import pytest

@pytest.fixture(scope="session")
def personal_data():
    name = "Giorgi"
    age = 22

    return [name, age]

def test_name(personal_data):
    personal_data[0] = "Dato"
    assert personal_data[0] == "Dato"


def test_name_again(personal_data):
    assert personal_data[0] == "Dato"

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


@pytest.fixture()
def create_person():
    return Person("Vaxo", 221)


def test_peron(create_person):
    assert create_person.name == "Vaxo"


"""

Paramteters

"""

def division(num1, num2):
    return num1 / num2

@pytest.mark.parametrize("number1, number2, result", [(10, 2, 5), (18, 9, 2), (45, 9, 5)])
def test_division(number1, number2, result):
    assert division(number1, number2) == result



def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert division(2, 0)


"""
groping Tests
"""
@pytest.mark.arithmetic1
def test_multiplication():
    assert 5 * 5 == 25

@pytest.mark.arithmetic1
def test_division_2():
    assert 10 / 2 == 5

@pytest.mark.arithmetic2
@pytest.mark.xfail
def test_addition():
    assert 10 + 2 == 500

@pytest.mark.arithmetic2
def test_subtraction():
    assert 10 - 2 == 8











