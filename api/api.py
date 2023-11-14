from fastapi import FastAPI
from fastapi.responses import FileResponse  #wird benötigt um Dateien zu senden

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("index.html")
