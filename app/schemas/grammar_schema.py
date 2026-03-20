from pydantic import BaseModel, Field

class GrammarRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Text to be corrected"
    )

class GrammarResponse(BaseModel):
    original: str
    corrected: str

