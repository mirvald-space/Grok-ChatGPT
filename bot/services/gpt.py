import base64
from typing import Dict, List

from openai import AsyncOpenAI

from config import DALLE_MODEL, GPT_MODEL, MAX_TOKENS, OPENAI_API_KEY


class GPTService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def get_response(
        self, message: str, context: List[Dict[str, str]] = None
    ) -> str:
        try:
            if context is None:
                context = []
            messages = context + [{"role": "user", "content": message}]
            response = await self.client.chat.completions.create(
                model=GPT_MODEL,
                messages=messages,
                max_completion_tokens=MAX_TOKENS,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ошибка при получении ответа: {str(e)}"

    async def generate_image(self, prompt: str) -> str:
        try:
            response = await self.client.images.generate(
                model=DALLE_MODEL,
                prompt=prompt,
                size="1024x1024",
                quality="hd",
                n=1,
            )
            return response.data[0].url
        except Exception as e:
            raise Exception(f"Ошибка генерации изображения: {str(e)}")

    async def read_image(self, image_path: str) -> str:
        try:

            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

            response = await self.client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Опиши это изображение:"},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                },
                            },
                        ],
                    }
                ],
                max_completion_tokens=MAX_TOKENS,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ошибка при обработке изображения: {str(e)}"

    async def text_to_speech(
        self, text: str, voice: str = "alloy", output_path: str = "speech.mp3"
    ) -> str:
        try:
            response = await self.client.audio.speech.create(
                model="tts-1", voice=voice, input=text
            )

            # Получаем бинарные данные и записываем в файл напрямую
            binary_content = response.content

            with open(output_path, "wb") as file:
                file.write(binary_content)

            return output_path
        except Exception as e:
            import traceback

            error_traceback = traceback.format_exc()
            raise Exception(
                f"Ошибка при преобразовании текста в речь: {str(e)}\n{error_traceback}"
            )
