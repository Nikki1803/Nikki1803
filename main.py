# Create a Pydantic model for incoming JSON requests
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

# Create a new FastAPI endpoint for text processing
from fastapi import FastAPI

app = FastAPI()

@app.post("/generate_tokens")
async def generate_tokens(request: TextRequest):
    # Use the generate() function to process the text
    tokens = generate(request.text)  # Assuming generate() returns tokens
    return {"tokens": tokens}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Token Generation API! Developed by [Nikitha Eslavath]"}
@app.post("/generate_tokens", summary="Generate Tokens from Text")
async def generate_tokens(request: TextRequest):
    """
    Endpoint to generate tokens from the provided text.
    
    - **text**: The text input to be processed for token generation.
    
    Returns a JSON object containing the list of generated tokens.
    """
    tokens = generate(request.text)  # Call the generate function
    return {"tokens": tokens}

from fastapi.testclient import TestClient

client = TestClient(app)

def test_generate_tokens():
    response = client.post("/generate_tokens", json={"text": "Sample text"})
    assert response.status_code == 200
    assert "tokens" in response.json()


