from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Example Pydantic model
class Item(BaseModel):
    name: str
    description: str

# In-memory storage for example data
storage = []

# POST endpoint to create an item
@app.post("/items/")
async def create_item(item: Item):
    storage.append(item)
    return {"message": "Item created successfully", "item": item}

# PUT endpoint to update an item or create it if it doesn't exist
@app.put("/items/{name}")
async def update_item(name: str, item: Item):
    for existing_item in storage:
        if existing_item.name == name:
            existing_item.name = item.name
            existing_item.description = item.description
            return {"message": "Item updated successfully", "item": existing_item}

    # If item does not exist, create it
    storage.append(item)
    return {"message": "Item created successfully", "item": item}

# GET endpoint to retrieve item details
@app.get("/items/{name}")
async def read_item(name: str):
    for item in storage:
        if item.name == name:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE endpoint to remove an item
@app.delete("/items/{name}")
async def delete_item(name: str):
    for index, item in enumerate(storage):
        if item.name == name:
            # Remove the item from the list
            deleted_item = storage.pop(index)
            return {"message": "Item deleted successfully", "deleted_item": deleted_item}