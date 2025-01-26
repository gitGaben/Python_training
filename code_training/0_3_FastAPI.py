from fastapi import FastAPI, HTTPException

app = FastAPI()

# Example data model
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

# In-memory storage for example data
storage = [
    Item(name="item1", description="Description for item 1"),
    Item(name="item2", description="Description for item 2"),
]

# GET endpoint to retrieve item details
@app.get("/items/{name}")
async def read_item(name: str):
    for item in storage:
        if item.name == name:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# HEAD endpoint to check item existence
@app.head("/items/{name}")
async def check_item_existence(name: str):
    for item in storage:
        if item.name == name:
            return
    raise HTTPException(status_code=404, detail="Item not found")