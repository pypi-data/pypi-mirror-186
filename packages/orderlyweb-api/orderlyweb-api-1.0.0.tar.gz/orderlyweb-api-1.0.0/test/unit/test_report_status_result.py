from orderlyweb_api.result_models import ReportStatusResult

test_result_success = ReportStatusResult({"status": "success",
                                          "version": "test-version",
                                          "output": ["test-out"]})

test_result_running = ReportStatusResult({"status": "running",
                                          "version": None, "output": {}})

test_result_runtimeerror = ReportStatusResult({"status": "RuntimeError",
                                               "version": None, "output": {}})

test_result_error = ReportStatusResult({"status": "error",
                                        "version": None, "output": {}})

test_result_killed = ReportStatusResult({"status": "killed",
                                         "version": None, "output": {}})

test_result_queued = ReportStatusResult({"status": "queued",
                                         "version": None, "output": {}})

test_result_unknown = ReportStatusResult({"status": "unknown",
                                          "version": None, "output": {}})


def test_status():
    assert test_result_success.status == "success"


def test_version():
    assert test_result_success.version == "test-version"


def test_output():
    assert test_result_success.output == ["test-out"]


def test_success():
    assert test_result_success.success
    assert not test_result_queued.success
    assert not test_result_running.success
    assert not test_result_error.success
    assert not test_result_runtimeerror.success
    assert not test_result_killed.success
    assert not test_result_unknown.success


def test_fail():
    assert not test_result_success.fail
    assert not test_result_running.fail
    assert not test_result_queued.fail
    assert test_result_error.fail
    assert test_result_runtimeerror.fail
    assert test_result_killed.fail
    assert test_result_unknown.fail


def test_finished():
    assert not test_result_queued.finished
    assert not test_result_running.finished
    assert test_result_success.finished
    assert test_result_error.finished
    assert test_result_runtimeerror.finished
    assert test_result_killed.finished
    assert test_result_unknown.finished
