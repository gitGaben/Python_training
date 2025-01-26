from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}

@app.get("/hello2/{name}/{age}/{salary}")
async def hello2(name:str,age:int, salary: int):
   return {"name": name, "age":age, "salary":salary} 

@app.get("/hello3")
async def hello3(name:str,age:int, salary: int):
   return {"name": name, "age":age, "salary":salary}