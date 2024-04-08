
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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
