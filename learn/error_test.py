from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "the doo"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code = 404,
            detail= "item not found",
            headers= {'Error-Heading': 'here is an error'}
            )
    return {'item': items[item_id]}
