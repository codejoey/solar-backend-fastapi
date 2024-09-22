from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()


@app.exception_handler(UnicornException)
async def custom_unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code = 418,
        content={
            'message': f"Oops! {exc.name} messed up. Rainbow~"
        },
    )

@app.get('/unicorn/{name}')
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name = name)
    return {'unicorn_name': name}
