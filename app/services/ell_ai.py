from ..core.config import settings
import ell_ai

class EllAIService:
    def __init__(self):
        self.client = ell_ai.Client(api_key=settings.ELL_AI_API_KEY)

    async def process_message(self, message: str):
        return await self.client.chat(message)

    async def create_submind(self, config: dict):
        return await self.client.create_submind(config)

    async def list_subminds(self):
        return await self.client.list_subminds()

ell_ai_service = EllAIService()