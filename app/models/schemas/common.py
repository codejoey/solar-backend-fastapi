"""
- You can define and manage the request and response model for FastAPI.
    - You can define your model by inheriting from `pydantic`'s `BaseModel` class.
    - `ChatRequest` is a chat request model that takes as input the message entered by the user, the name of the model to invoke, and whether a stream response is present.
    - `ChatResponse` is the chat response model when `stream=False`, with the text output in the data field.
        - If `stream=True`, the response will be handled as a `StreamResponse`, and the requesting client will receive a byte stream as the response.
- Good to know
    - https://fastapi.tiangolo.com/tutorial/body/
    - https://fastapi.tiangolo.com/tutorial/response-model/
"""
from typing import List, Optional
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str
    statusCode: str

class ChatRequest(BaseModel):
    messages: List[str]
    model: str = "solar-1-mini-chat"
    stream: bool = False

class ChatResponse(BaseModel):
    message: str = "OK"
    statusCode: str = "200"
    data: Optional[str]
