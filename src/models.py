from pydantic import BaseModel, Field
from typing import List, Literal


class GenerateRequest(BaseModel):
    requirement_text: str = Field(..., min_length=10)
    num_cases: int = Field(3, ge=1, le=20)
    style: Literal["plain", "gherkin"] = "plain"


class TestCase(BaseModel):
    id: str
    title: str
    preconditions: List[str]
    steps: List[str]
    expected_result: str
    priority: Literal["Low", "Medium", "High", "Critical"] = "Medium"
    tags: List[str] = []


class GenerateResponse(BaseModel):
    test_cases: List[TestCase]

