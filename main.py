from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items: List[Item] = []

@app.get("/")
def home_page():
    return "This is homepage"

@app.get("/items")
def get_items():
    return items

@app.get("/teas")
def add_items(item: Item):
    items.append(item)
    return 

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = update_item
            return update_item
    return {"error":"item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    return {"error": "item not found"}
