from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str  = None #None 是預設值

@app.get("/")#定義路徑
def read_root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: Item):
    print(f"Recevied item: {item}")
    return {"message": "Item received","item": item}