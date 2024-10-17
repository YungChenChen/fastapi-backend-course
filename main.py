from fastapi import FastAPI

app = FastAPI()


@app.get("/")#定義路徑
async def root():
    return {"message": "Hello World"}

@app.get("/lol")#定義路徑
async def lol():
    return 'LOOOOL'