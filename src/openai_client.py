from openai import OpenAI
from logger import logger
from typing import List, Dict, Any
import time
from config import (
    OPENAI_API_KEY,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    MAX_RETRIES,
    RETRY_DELAY
)

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        logger.info("OpenAI client initialized")

    def generate_response(
        self,
        prompt: str,
        model: str = DEFAULT_MODEL,
        temperature: float = DEFAULT_TEMPERATURE
    ) -> str:
        for attempt in range(MAX_RETRIES):
            try:
                logger.debug(
                    "Sending request to OpenAI API",
                    prompt=prompt,
                    response=f"Model: {model}, Temperature: {temperature}"
                )
                
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature
                )
                
                response_text = response.choices[0].message.content
                logger.info(
                    "Successfully received response from OpenAI API",
                    prompt=prompt,
                    response=response_text
                )
                return response_text
                
            except Exception as e:
                logger.warning(
                    f"Attempt {attempt + 1} failed",
                    prompt=prompt,
                    response=str(e)
                )
                if attempt == MAX_RETRIES - 1:
                    logger.error(
                        f"Failed after {MAX_RETRIES} attempts",
                        prompt=prompt,
                        response=str(e)
                    )
                    raise Exception(f"Failed after {MAX_RETRIES} attempts: {str(e)}")
                logger.info(f"Waiting {RETRY_DELAY} seconds before retrying...")
                time.sleep(RETRY_DELAY) 