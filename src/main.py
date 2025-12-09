from fastapi import FastAPI
from .models import GenerateRequest, GenerateResponse
from .ai_engine import generate_test_cases

app = FastAPI(
    title="AI Test Case Generator",
    description="Generate software test cases from natural language requirements.",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/generate-testcases", response_model=GenerateResponse)
def generate_testcases_endpoint(request: GenerateRequest):
    """
    Accepts a requirement text and returns generated test cases.
    Right now it uses a simple placeholder implementation.
    Later we plug in a real LLM.
    """
    test_cases = generate_test_cases(request)
    return GenerateResponse(test_cases=test_cases)

