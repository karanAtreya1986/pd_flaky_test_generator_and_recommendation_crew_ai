Build a CrewAI crew with three agents that investigates flaky tests in a CI/CD pipeline. 

Agent 1 is a "Flaky Test Detector" that receives a list of test names with their pass/fail history over the last 10 runs (you will create a custom @tool that returns mock data — a dictionary of test names mapped to a list of pass/fail booleans). This agent identifies which tests are flaky (passed and failed in the same window). 

Agent 2 is a "Root Cause Analyst" that takes the flaky tests identified and hypothesizes why each test is flaky (timing issues, shared state, environment dependency, test data pollution, etc.). 

Agent 3 is a "Fix Recommender" that produces a concrete action plan for each flaky test — what to fix, how to stabilize it, and whether to quarantine it. Use the context parameter so each task feeds into the next. 


Create at least 2 custom tools (the test history tool and a mock "get test source code" tool). Define a Pydantic model FlakyTestReport with fields for test_name, flakiness_rate, probable_cause, recommended_action, and quarantine (bool), and use output_json on the final task. 

Write pytest tests for both your custom tools and your agent configurations.