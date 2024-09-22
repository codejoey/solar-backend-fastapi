"""
- You can define and manage endpoint paths for FastAPIs.
    - Use `FastAPI`'s `Depends` to inject and use the required service dependencies.
        - You can use a dependency injection library like `dependency_injector`, or you can inject the required classes with a class like `ServiceFactory`, as written in the example.
- Good to know
    - https://fastapi.tiangolo.com/tutorial/dependencies/
"""
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.models.schemas.common import ChatRequest, ChatResponse, ErrorResponse
from app.services.chat import ChatService
from app.services.chat_service_factory import ChatServiceFactory

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, responses={400: {"model": ErrorResponse}})
async def chat(chat_request: ChatRequest, chat_service: ChatService = Depends(ChatServiceFactory.get_chat_service)) -> ChatResponse | StreamingResponse:
    """
    Chat with OpenAI API

    Args:
    - chat_request (ChatRequest): Request body

    Returns:
    - ChatResponse | StreamingResponse: Chat response
    """

    if chat_request.stream:
        response = await chat_service.stream_chat(messages=chat_request.messages, model=chat_request.model)

        return StreamingResponse(
            content=response,
            media_type="text/event-stream")
    else:
        response = await chat_service.chat(messages=chat_request.messages, model=chat_request.model)

        return ChatResponse(data=response)
