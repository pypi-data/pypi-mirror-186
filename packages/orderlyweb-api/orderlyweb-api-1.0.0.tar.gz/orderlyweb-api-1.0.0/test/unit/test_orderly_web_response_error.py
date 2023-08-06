from orderlyweb_api.orderly_web_response_error import OrderlyWebResponseError


def test_init_with_error_message():
    response = MockResponse({
        "errors": [{"error": "test-code", "detail": "test-msg"}]
    })
    sut = OrderlyWebResponseError(response)
    assert str(sut) == "test-msg"
    assert sut.response is response


def test_init_with_error_code():
    response = MockResponse({
        "errors": [{"code": "test-code"}]
    })
    sut = OrderlyWebResponseError(response)
    assert str(sut) == "test-code"
    assert sut.response is response


def test_init_with_default_message():
    response = MockResponse({
        "errors": []
    })
    sut = OrderlyWebResponseError(response)
    assert str(sut) == "An OrderlyWeb error occurred"
    assert sut.response is response


class MockResponse:
    def __init__(self, json):
        self.__json = json

    def json(self):
        return self.__json
