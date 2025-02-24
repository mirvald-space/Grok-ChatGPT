from typing import Dict, List

from together import Together

from config import MAX_TOKENS, TOGETHER_API_KEY, TOGETHER_MODEL


class TogetherService:
    def __init__(self):
        self.client = Together(api_key=TOGETHER_API_KEY)

    async def get_response(
        self, message: str, context: List[Dict[str, str]] = None
    ) -> str:
        try:
            if context is None:
                context = []
            messages = context + [{"role": "user", "content": message}]
            response = self.client.chat.completions.create(
                model=TOGETHER_MODEL,
                max_tokens=MAX_TOKENS,
                messages=messages,
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"Ошибка при получении ответа от together: {str(e)}"
