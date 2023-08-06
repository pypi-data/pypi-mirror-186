from orderlyweb_api.orderly_web_api import OrderlyWebAPI
from orderlyweb_api.orderly_web_response_error import OrderlyWebResponseError
import requests_mock
import pytest

base_url = 'http://test'
api_base_url = base_url + "/api/v2/"
error_response_text = '{"errors": ' + \
                      '[{"detail": "test-err-msg"}]' + \
                      '}'


def test_init():
    with requests_mock.mock() as m:
        m.post("{}login/".format(api_base_url),
               text='{"access_token": "fake_token"}')

        api = OrderlyWebAPI(base_url, "fake_montagu_token")
        assert api.access_token == "fake_token"

        request = m.request_history[0]
        assert request.headers["Authorization"] == "token fake_montagu_token"


def test_init_error():
    with requests_mock.mock() as m:
        m.post("{}login/".format(api_base_url), status_code=500,
               text=error_response_text)

        with pytest.raises(OrderlyWebResponseError) as ex:
            OrderlyWebAPI(base_url, "fake_montagu_token")
        assert str(ex.value) == "test-err-msg"
        assert ex.value.response.status_code == 500


def test_run_report():
    params = {"p1": "v1", "p2": 2}
    api = get_test_api()
    with requests_mock.mock() as m:
        m.post("{}reports/test-report/run/?timeout=480".format(api_base_url),
               text='{"data": {"key": "test-key"}}')

        key = api.run_report("test-report", params, 480)
        assert key == "test-key"

        request = m.request_history[0]
        assert request.body == "{\"params\": {\"p1\": \"v1\", \"p2\": 2}}"


def test_run_report_error():
    params = {}
    api = get_test_api()
    with requests_mock.mock() as m:
        m.post("{}reports/test-report/run/?timeout=600".format(api_base_url),
               status_code=403, text=error_response_text)
        with pytest.raises(OrderlyWebResponseError) as ex:
            api.run_report("test-report", params)
        assert str(ex.value) == "test-err-msg"
        assert ex.value.response.status_code == 403


def test_report_status():
    api = get_test_api()
    with requests_mock.mock() as m:
        m.get("{}reports/test-key/status/".format(api_base_url),
              text='{"data": {"status": "success", "version": "v1", '
                   '"output": {}}}')
        result = api.report_status("test-key")
        assert result.status == "success"
        assert result.success
        assert result.version == "v1"
        assert result.output == {}


def test_kill_report():
    api = get_test_api()
    with requests_mock.mock() as m:
        url = "{}reports/test-key/kill/".format(api_base_url)
        m.delete(url, text="")
        api.kill_report("test-key")
        assert m.request_history[0].method == 'DELETE'
        assert m.request_history[0].url == url


def test_report_status_error():
    api = get_test_api()
    with requests_mock.mock() as m:
        m.get("{}reports/test-key/status/".format(api_base_url),
              status_code=500, text=error_response_text)
        with pytest.raises(OrderlyWebResponseError) as ex:
            api.report_status("test-key")
        assert str(ex.value) == "test-err-msg"
        assert ex.value.response.status_code == 500


def test_kill_report_error():
    api = get_test_api()
    with requests_mock.mock() as m:
        url = "{}reports/test-key/kill/".format(api_base_url)
        m.delete(url,  status_code=500, text=error_response_text)
        with pytest.raises(OrderlyWebResponseError) as ex:
            api.kill_report("test-key")
        assert str(ex.value) == "test-err-msg"
        assert ex.value.response.status_code == 500


def get_test_api():
    with requests_mock.mock() as m:
        m.post("{}login/".format(api_base_url),
               text='{"access_token": "fake_token"}')

        return OrderlyWebAPI(base_url, "fake_montagu_token")
