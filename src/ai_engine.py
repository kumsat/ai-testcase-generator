from typing import List
from .models import GenerateRequest, TestCase


def generate_test_cases(req: GenerateRequest) -> List[TestCase]:
    """
    Simple placeholder implementation.
    Later we will replace this with a real LLM-based generator.
    """
    base_id = "TC-001"

    demo_case = TestCase(
        id=base_id,
        title="Successful operation based on requirement",
        preconditions=[
            "System is up and running",
            "User has necessary permissions (if applicable)",
        ],
        steps=[
            "Read and understand the requirement",
            "Perform the main action that the requirement describes",
            "Verify the outcome in the system",
        ],
        expected_result="System behaves according to the described requirement without errors.",
        priority="High",
        tags=["demo", "auto-generated"],
    )

    # Return at least one case; later we can expand based on req.num_cases
    return [demo_case]

