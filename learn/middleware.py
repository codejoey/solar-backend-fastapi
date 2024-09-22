import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware('http') #tells function below to be registered as a middleware component
async def add_process_time_handler (request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request) #! no need to define explicitly yourself, it comes with when using middleware
    process_time = time.perf_counter() - start_time

    response.headers['Process-Time'] = str(process_time)
    return response
