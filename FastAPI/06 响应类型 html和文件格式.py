from fastapi import FastAPI
from fastapi.responses import HTMLResponse,FileResponse
from pathlib import Path

app = FastAPI()
@app.get("/html", response_class=HTMLResponse)
async def head_html():
    return "<h1>此为一级标题</h1>"
@app.get("/file")
async def download_file():
    BASE_DIR = Path(__file__).resolve().parent
    path = BASE_DIR / "resource" / "picture.png"
    return FileResponse(path, )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
#127.0.0.1 是监听本地回环  0.0.0.0 是监听所有网卡的意思
