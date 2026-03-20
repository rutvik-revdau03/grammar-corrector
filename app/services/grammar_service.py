import language_tool_python

# Initialize once (important for performance)
tool = language_tool_python.LanguageTool('en-US')

def correct_text(text: str) -> str:
    return tool.correct(text)