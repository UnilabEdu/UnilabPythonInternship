BASE_URL = "localhost:5000"
endpoints_tuple = "/home", "/about", "/contact"


def mockAPIchecker(url=None):
    # pretend get request was made
    if "admin" in url:
        # pretend status 200 ok has returned
        return 404
    return 200


def testAPI():
    for endpoint in endpoints_tuple:
        url = BASE_URL + endpoint
        assert mockAPIchecker(url) == 200, f"Can't reach endpoint at {url}"


def testMock1():
    assert 22 <= 22


def testSomethingElse():
    assert len("python") == 6

# if __name__ == "__main__":
#     assert a + b == 30
