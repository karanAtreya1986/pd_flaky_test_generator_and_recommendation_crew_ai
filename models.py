from pydantic import BaseModel
from typing import List

class FlakyTestReport(BaseModel):
    test_name: str
    flakiness_rate: float
    probable_cause: str
    recommended_action: str
    quarantine: bool

class FlakyTestReports(BaseModel):
    reports: List[FlakyTestReport]