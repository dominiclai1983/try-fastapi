from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
async def root():
  return {"message":"hello world"}

@app.post('/')
async def post():
  return {"message":"hello from the post world"}

@app.put('/')
async def put():
  return {"message":"hello from the put world"}

@app.get('/items')
async def list_item():
  return {"message":"list items route"}

@app.get('/items/{item_id}')
async def get_item(item_id: int):
  return {"item_id":item_id}

@app.get('/users/me')
async def get_current_user():
  return {"message":"this is the current user"}

@app.get('/users/{user_id}')
async def get_user(user_id: str):
  return {"user_id": user_id}

class FoodEnum(str, Enum):
  fruits = 'fruits'
  veggie = 'veggie'
  dairy = 'dairy'

@app.get('/food/{food_name}')
async def get_food(food_name: FoodEnum):
  if food_name == FoodEnum.veggie:
    return {"food_name":food_name, "message":"you are healthy"}
  
  if food_name.value == 'fruits':
    return {"food_name":food_name, "message":"you are still healthy, but like sweat things"}
  
  return {"food_name": food_name, "message":"yeah, you hit the spot"}