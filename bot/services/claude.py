from anthropic import AsyncAnthropic

from config import ANTHROPIC_API_KEY, CLAUDE_MODEL, MAX_TOKENS


class ClaudeService:
    def __init__(self):
        self.client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

    async def get_response(self, message: str) -> str:
        try:
            response = await self.client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=MAX_TOKENS,
                messages=[{"role": "user", "content": message}],
            )
            return response.content[0].text
        except Exception as e:
            return f"An error occurred while receiving a reply from Claude: {str(e)}"
