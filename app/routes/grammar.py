from fastapi import APIRouter, HTTPException
from app.schemas.grammar_schema import GrammarRequest, GrammarResponse
from app.services.grammar_service import correct_text
from app.core.validator import validate_text

router = APIRouter()

@router.post("/correct", response_model=GrammarResponse)
def correct_grammar(request: GrammarRequest):

    try:
        # Custom validation
        validate_text(request.text)

        corrected = correct_text(request.text)

        return {
            "original": request.text,
            "corrected": corrected
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))