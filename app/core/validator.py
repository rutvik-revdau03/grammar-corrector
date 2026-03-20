import re
from fastapi import HTTPException

def validate_text(text: str):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Input cannot be empty")

    if len(text) > 1000:
        raise HTTPException(status_code=400, detail="Text too long (max 1000 chars)")

    # Allow only basic characters
    if not re.match(r'^[a-zA-Z0-9\s.,!?\'"-]+$', text):
        raise HTTPException(status_code=400, detail="Invalid characters in input")