from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from model import GeminiProInterface

app = FastAPI()
gemini_interface = GeminiProInterface()

class Prompt(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    ollama_ui_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ollama WebUI</title>
    </head>
    </html>
    """
    return ollama_ui_html

@app.post("/generate", response_class=JSONResponse)
def generate(prompt: Prompt):
    try:
        response_text = gemini_interface.generate_response(prompt.text)
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 