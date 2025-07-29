from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Kazap está online!"}

# Página com seu chatbot
@app.get("/chat")
def serve_chat():
    return FileResponse("static/index.html")
