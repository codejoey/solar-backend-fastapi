from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

import time

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

items = {"foo": "the doo"}

@app.middleware('http') #tells function below to be registered as a middleware component
async def add_process_time_handler (request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request) #! no need to define explicitly yourself, it comes with when using middleware
    process_time = time.perf_counter() - start_time

    response.headers['Process-Time'] = str(process_time)
    return response

@app.exception_handler(UnicornException)
async def custom_unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code = 418,
        content={
            'message': f"Oops! {exc.name} messed up. Rainbow~"
        },
    )

@app.get('/')
async def root():
    return {'message': 'hello'}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code = 404,
            detail= "item not found",
            headers= {'Error-Heading': 'here is an error'}
            )
    return {'item': items[item_id]}

@app.get('/unicorn/{name}')
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name = name)
    return {'unicorn_name': name}
