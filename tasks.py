from crewai import Task
from models import FlakyTestReports


def detect_flaky_tests(agent):
    return Task(
        description=(
            "Fetch test history and identify flaky tests. "
            "A flaky test is one that has both pass and fail in last 10 runs. "
            "Also compute flakiness rate = failures / total runs."
        ),
        expected_output="List of flaky tests with flakiness rates",
        agent=agent,
    )


def analyze_root_cause(agent):
    return Task(
        description=(
            "For each flaky test, analyze possible causes such as timing issues, "
            "shared state, environment dependency, or test data pollution."
        ),
        expected_output="Flaky tests with probable causes",
        agent=agent,
    )


def recommend_fixes(agent):
    return Task(
        description=(
            "Provide a concrete action plan for each flaky test. "
            "Include stabilization steps and whether to quarantine."
        ),
        expected_output="Structured JSON report of flaky tests",
        agent=agent,
        output_json=FlakyTestReports,
    )