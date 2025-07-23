from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel

app = FastAPI()

# Dummy database
items = {
    1: {"name": "Laptop", "description": "A high-end gaming laptop"},
    2: {"name": "Phone", "description": "A smartphone with great camera"}
}

# Pydantic model for POST
class Item(BaseModel):
    name: str
    description: str

# GET with path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# GET with query parameter
@app.get("/search/")
def search_items(keyword: str = ""):
    return {k: v for k, v in items.items() if keyword.lower() in v["name"].lower()}

# POST with request body
@app.post("/items/")
def create_item(item: Item):
    new_id = max(items.keys()) + 1
    items[new_id] = item.dict()
    return {"id": new_id, "item": item}

# File upload
@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type}
