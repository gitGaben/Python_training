# 0_5_FastAPI.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Example data model
class Item2:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

# In-memory storage for example data
storage = []

# POST endpoint to create an item
@app.post("/items/")
async def create_item(name, description):
    item = Item2(name, description)
    storage.append(item)
    return {"message": "Item created successfully", "item": item}

# PUT endpoint to update an item or create it if it doesn't exist
@app.put("/items/{name}")
async def update_item(name: str, new_name: str, description: str):
    for existing_item in storage:
        if existing_item.name == name:
            existing_item.name = new_name
            existing_item.description = description
            return {"message": "Item updated successfully", "item": existing_item}

    # If item does not exist, create it
    item = Item2(new_name, description)
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

    # If item does not exist, raise HTTPException with 404 status code
    raise HTTPException(status_code=404, detail="Item not found")