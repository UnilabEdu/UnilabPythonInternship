import pytest

"""
Pytest Fixtures, fixture არის ფუნქცია რომელიც შეგიძლია ტესტებს გადასცე და გამოიყენო.
შესაძლებელია გადასცე ნებისმიერი ტიპის მონაცემი, კლასი, სია და ა.შ
"""
@pytest.fixture()
def personal_data():
    name = "Giorgi"
    age = 22

    return [name, age]


def test_renaming(personal_data):
    personal_data[0] = "Dato"
    assert personal_data[0] == "Dato"


""" Fixture-ი ყოველ ფუნქციაში გამოიძახება თავიდან, ანუ თუ fixture-ის მიერ მოწოდებული მონაცემები შეცვალე, ახალ ტესტში
ის ისევ ძველ მონაცემებს დაუბრუნდება. მაგალითად, ზემოთ ჩვენ სახელში გიორგის ნაცვლად შევინახით დათო, მაგრამ ქვედა
ტესტში ისევ გიორგი გახდა
"""
def test_name(personal_data):
    assert personal_data[0] == "Giorgi"
    assert personal_data[0] != "Dato"


"""
თუ არ გვინდა რომ ყოველ ჯერზე თავიდან იქმნებოდეს Fixture-ი, მაშინ scope არგუმენტში გაუწერ sessions-ს, ანუ მთელი ტესტის
მანძილზე fixture-ი შეიქმნება მხოლოდ ერთი და ყველასთვის იქნება საერთო.
"""
@pytest.fixture(scope="session")
def scoped_personal_data():
    name = "Giorgi"
    age = 22

    return [name, age]


def test_scoped_rename(scoped_personal_data):
    scoped_personal_data[0] = "Dato"
    assert scoped_personal_data[0] == "Dato"


def test_scoped_name(scoped_personal_data):
    assert scoped_personal_data[0] == "Dato"

#კლასის მაგალითი
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@pytest.fixture()
def person():
    return Person("Vaxo", 21)


def test_person_object(person):
    assert person.name == "Vaxo"


"""
Pytest Parametrize, გვეხმარება ფუნქცია გავტესტოთ რამოდენიმე სხვადასხვა მონაცემეზე. ბრჭყალებში ვწერთ არგუმენტის სახელს, ხოლო
შემდეგ ვქმნით tuple-ბის სიას, რომელიც განსაზღვრავს თუ რა მნიშვნელობები უნდა მიიღონ არგუმენტებმა
"""
def division(num1, num2):
    return num1 / num2


@pytest.mark.parametrize("number1, number2, result", [(10, 2, 5), (4, 2, 2), (5, 5, 1)])
def test_division(number1, number2, result):
    assert division(number1, number2) == result


# თუ ფუნქცია აბრუნებს exception-ს, და ასე უნდა იყოს კიდეც, შეგვიძლია გავტესტოთ pytest.raises მეთოდით
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert division(2, 0)


"""
Pytest grouping, შეგვიძლია ტესტები დავყოთ სხვადასხვა ნაკრებად, ამის სინტაქსია @pytest.mark.GROUPNAME
ეს გვაძლევს საშუალებას რომ ყველა ტესტის ნაცვლად გავუშვათ რამოდენიმე სპეციფიკური ტესტი.

ტესტის გასაშვებათ უთითებთ -m არგუმენტს და გადასცემთ ჯგუფის სახელს. მაგალითად:
pytest fixtures.py -m arithmetic1.

ჯგუფის სახელები უნდა იყოს დარეგისტრირებული pytest.ini ფაილში.
"""
@pytest.mark.arithmetic1
def test_multiplitcation():
    assert 5 * 2 == 10


@pytest.mark.arithmetic1
def test_division():
    assert 10 / 2 == 5


@pytest.mark.arithmetic2
def test_addition():
    assert 2 + 2 == 4


@pytest.mark.arithmetic2
def test_subtraction():
    assert 10 - 2 == 8


# თუ ფუნქციას მივუთითებთ შემდეგ დეკორატორს, მაშინ ტესტირებისას მას გამოტოვებს
@pytest.mark.skip
def test_ignore():
    name = "Temo"
    assert name == "Temo"


# შეიძლება გვქონდეს ფუნქცია რომელიც ვიცით რომ არ მუშაობს და ტყუილად დრო რომ არ დავხარჯოთ, პირდაპირვე ვა-fail-ებთ.
#skip-საც და fail-საც შეგვიძლია მიზეზი მივუთითოთ
@pytest.mark.xfail(reason="Not working since v2.3.1")
def test_known_to_fail():
    name = "Temo"
    assert name == "Giorgi"