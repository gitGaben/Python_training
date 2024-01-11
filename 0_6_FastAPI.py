from fastapi import FastAPI, HTTPException, APIRouter

app = FastAPI()

# Example data model
class Item2:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Person:
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age


# In-memory storage for example data
item_storage = []
user_storage = []

# --- Item Router ---
item_router = APIRouter()


# POST endpoint to create an item
@item_router.post("/")
async def create_item(name, description):
    item = Item2(name, description)
    item_storage.append(item)
    return {"message": "Item created successfully", "item": item}

# GET endpoint to retrieve item details
@item_router.get("/{name}")
async def read_item(name: str):
    for item in item_storage:
        if item.name == name:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# --- User Router ---
user_router = APIRouter()

# POST endpoint to create an item
@user_router.post("/")
async def create_item(name, age):
    user = Person(name, age)
    user_storage.append(user)
    return {"message": "User created successfully", "user": user}

# GET endpoint to retrieve item details
@user_router.get("/{name}")
async def read_item(name: str):
    for user in user_storage:
        if user.name == name:
            return user
    raise HTTPException(status_code=404, detail="Item not found")


app.include_router(item_router, prefix="/items")
app.include_router(user_router, prefix="/users")


