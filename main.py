from fastapi import FastAPI
from sockets import router as socket_router

app = FastAPI()
app.include_router(socket_router)

# 경로, HTML Response
from fastapi.responses import HTMLResponse
from pathlib import Path
@app.get('/')
def index():
    index_html = Path('index.html').read_text()
    return HTMLResponse(index_html)

# uvicorn main:app --reload