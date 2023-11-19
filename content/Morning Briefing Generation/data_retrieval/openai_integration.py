"""OpenAI API integration functions."""
from typing import cast

from openai import OpenAI
from utils.logger import get_logger


def prompt_gpt4_turbo(
    api_key: str,
    user_message: str,
    system_message: str = "You are a helpful assistant.",
) -> str:
    """
    A function to prompt the ChatGPT API to generate a response to a user message.

    :param api_key: The API key for the OpenAI API.
    :param user_message: The user's message to respond to.
    :param system_message: The system's message to respond to.
    :return: The response from the ChatGPT API.
    """

    logger = get_logger()  # Initialize the logger
    logger.info("Starting to prompt the ChatGPT API.")

    try:
        client = OpenAI(api_key=api_key)
        logger.info("Client initialized.")

        logger.info(f"Prompting the ChatGPT API with: '{user_message}'.")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
        logger.info("Response received.")
        return cast(str, response.choices[0].message.content)
    except Exception as e:
        logger.error(f"Error: {e}")
        return "..."
