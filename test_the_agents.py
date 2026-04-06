from agents import flaky_test_detector, root_cause_analyst, fix_recommender


def test_flaky_detector_agent():
    agent = flaky_test_detector()
    assert agent.role == "Flaky Test Detector"
    assert len(agent.tools) > 0


def test_root_cause_agent():
    agent = root_cause_analyst()
    assert agent.role == "Root Cause Analyst"
    assert len(agent.tools) > 0


def test_fix_recommender_agent():
    agent = fix_recommender()
    assert agent.role == "Fix Recommender"
    assert agent.tools == [] or agent.tools is not None