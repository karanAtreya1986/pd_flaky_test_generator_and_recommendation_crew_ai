from crewai.tools import tool
import random

@tool("get_test_history")
def get_test_history(dummy: str = ""):
    """
    Returns mock test history for last 10 runs.
    True = pass, False = fail
    """
    return {
        "test_login": [True, True, False, True, False, True, True, False, True, True],
        "test_payment": [True] * 10,
        "test_checkout": [True, False, True, False, True, False, True, False, True, False],
        "test_profile_update": [True, True, True, True, True, True, True, True, True, True],
    }


@tool("get_test_source_code")
def get_test_source_code(test_name: str):
    """
    Returns mock source code for a given test.
    """
    mock_sources = {
        "test_login": "time.sleep(2); assert login()",
        "test_payment": "assert process_payment()",
        "test_checkout": "assert checkout(cart)",
        "test_profile_update": "assert update_profile(user)",
    }
    return mock_sources.get(test_name, "assert True")