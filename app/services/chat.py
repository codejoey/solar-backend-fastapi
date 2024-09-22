"""
- Service layer, which defines the business logic or main logic of the function to call
    - Define the methods needed for the functionality you want to implement, and call them from Router.
    - If you want to add other features to the chat functionality, you can put the additional logic into `chat` and `stream_chat` methods or implement separate methods.
- Good to know
    - https://developers.upstage.ai/docs/apis/chat#example
"""
from typing import List, Dict, AsyncGenerator

from app.clients import OpenAIClient

class ChatService:

    def __init__(self, client: OpenAIClient):
        self.client = client

    def get_message(self, messages: str) -> List[Dict[str, str]]:
        """
        Generate message for chat

        Args:
            messages (str): List of messages

        Returns:
            List[Dict[str, str]]: List of messages
        """
        message=[
            {
                "role": "system",
                "content": "You are a helpful assistant." # Please Put Default Prompt Here
            },
            {
                "role": "user",
                "content": "\n".join(messages)
            }
        ]

        return message

    async def chat(self, messages: List[str], model: str='solar-1-mini-chat') -> str:
        """
        Request completion from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            messages (List[str]): List of messages
            model (str, optional): Model name. Defaults to 'solar-1-mini-chat'.

        Returns:
            str: Completion response
        """
        response = await self.client.generate(messages=self.get_message(messages), model=model)

        return response

    async def stream_chat(self, messages: List[str], model: str='solar-1-mini-chat') -> AsyncGenerator:
        """
        Request stream completion from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            messages (List[str]): List of messages
            model (str, optional): Model name. Defaults to 'solar-1-mini

        Returns:
            AsyncGenerator: Stream completion response
        """

        response = self.client.stream_generate(messages=self.get_message(messages), model=model)

        return response
