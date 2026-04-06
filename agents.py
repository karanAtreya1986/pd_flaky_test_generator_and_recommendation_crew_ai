from crewai import Agent
from tools import get_test_history, get_test_source_code
from crewai import LLM

import os
from dotenv import load_dotenv

load_dotenv()

# Step 0 - set the llm. brain
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def flaky_test_detector():
    return Agent(
        role="Flaky Test Detector",
        goal="Identify flaky tests based on pass/fail history",
        backstory="Expert in CI/CD reliability and test stability analysis",
        tools=[get_test_history],
        llm=llm,
        verbose=True,
    )


def root_cause_analyst():
    return Agent(
        role="Root Cause Analyst",
        goal="Determine why tests are flaky",
        backstory="Specialist in debugging flaky tests and CI environments",
        tools=[get_test_source_code],
        llm=llm,
        verbose=True,
    )


def fix_recommender():
    return Agent(
        role="Fix Recommender",
        goal="Provide actionable fixes for flaky tests",
        backstory="Senior SDET focused on stabilizing pipelines",
        llm=llm,
        verbose=True,
    )