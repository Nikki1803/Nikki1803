# Create a Pydantic model for incoming JSON requests
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
