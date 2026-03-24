from fastapi import APIRouter, HTTPException, UploadFile, File
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
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/correct-file")
async def correct_grammar_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.txt'):
        raise HTTPException(status_code=400, detail="Only .txt files are supported")

    try:
        # Read file content
        content = await file.read()
        lines = content.decode("utf-8").splitlines()

        results = []
        for line in lines:
            text = line.strip()
            if not text or text.startswith('='):
                continue
            
            try:
                corrected = correct_text(text)
                results.append({
                    "original": text,
                    "corrected": corrected
                })
            except Exception:
                # Still add to results even if it fails, but maybe mark it
                results.append({
                    "original": text,
                    "corrected": "N/A (Error during processing)"
                })

        return {
            "filename": file.filename,
            "total_lines": len(results),
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")