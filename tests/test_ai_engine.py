from src.models import GenerateRequest
from src.ai_engine import generate_test_cases


def test_generate_test_cases_returns_at_least_one_case():
    req = GenerateRequest(
        requirement_text=(
            "As a user, I want to reset my password so that "
            "I can regain access to my account."
        ),
        num_cases=3,
        style="plain",
    )

    cases = generate_test_cases(req)

    assert len(cases) >= 1
    first = cases[0]

    assert first.id
    assert first.title
    assert len(first.steps) > 0
    assert first.expected_result

