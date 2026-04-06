from tools import get_test_history, get_test_source_code


def test_get_test_history_structure():
    data = get_test_history.run()
    assert isinstance(data, dict)

    for test, history in data.items():
        assert isinstance(test, str)
        assert isinstance(history, list)
        assert len(history) == 10
        assert all(isinstance(x, bool) for x in history)


def test_get_test_source_code():
    code = get_test_source_code.run("test_login")
    assert "login" in code

    default_code = get_test_source_code.run("unknown_test")
    assert default_code == "assert True"