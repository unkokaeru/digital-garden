"""Generates a markdown document with a morning briefing for the user."""
import os
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from config.cfg import (
    CAL_URLS,
    CAREER_PROMPT,
    EMOJI_PROMPT,
    HAIKU_PATH,
    LUCK_CONTEXT,
    LUCK_PROMPT,
    MATHS_PROMPT,
    OPEN_WEATHER_API_KEY,
    OPENAI_API_KEY,
    PREDICTION_CONTEXT,
    PREDICTION_PROMPT,
    RSS_URLS,
    SAVE_LOCATION,
)
from data_retrieval.calendar_integration import fetch_calendar_events
from data_retrieval.chess_fetcher import fetch_chess_puzzle
from data_retrieval.gmail_integration import fetch_email_subjects
from data_retrieval.haiku_fetcher import get_haiku
from data_retrieval.openai_integration import prompt_gpt4_turbo
from data_retrieval.questions_fetcher import get_driving_questions
from data_retrieval.rss_fetcher import fetch_news
from data_retrieval.weather_fetcher import get_weather
from utils.logger import get_logger


def doc_gen() -> None:
    """
    A function to generate a morning briefing in a markdown document, and save it to the "Day by day" folder.

    :return: None
    """

    logger = get_logger()  # Initialize the logger
    logger.info("Starting the generation of the morning briefing document.")

    os.chdir(Path(__file__).parent.parent)  # Set the working directory
    logger.info(
        f"Changed working directory to {os.getcwd()}"
    )  # Log the directory change

    # Initialize Jinja2 environment and load template
    env = Environment(loader=FileSystemLoader("./template_rendering"))
    template = env.get_template("morning-briefing-template.md")
    logger.info("Template loaded successfully.")

    # Prepare data for the template
    data = {
        "haiku": get_haiku(HAIKU_PATH),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "weather": get_weather(OPEN_WEATHER_API_KEY, "Lincoln, UK"),
        "news": fetch_news(
            RSS_URLS, int(input("How many news articles would you like to fetch? "))
        ),
        "career_information": prompt_gpt4_turbo(
            OPENAI_API_KEY,
            CAREER_PROMPT,
        ),
        "maths_problem": prompt_gpt4_turbo(
            OPENAI_API_KEY,
            MATHS_PROMPT,
        ),
        "calendar_events": fetch_calendar_events(CAL_URLS),
        "emails": fetch_email_subjects(),
        "day_prediction": prompt_gpt4_turbo(
            OPENAI_API_KEY,
            PREDICTION_PROMPT,
            PREDICTION_CONTEXT,
        ),
        "chess_puzzle": fetch_chess_puzzle({"rating": "1500", "themesType": "ALL"}),
        "driving_questions": get_driving_questions(),
        "good_luck_message": prompt_gpt4_turbo(
            OPENAI_API_KEY,
            LUCK_PROMPT,
            LUCK_CONTEXT,
        ),
        "random_emojis": prompt_gpt4_turbo(
            OPENAI_API_KEY,
            EMOJI_PROMPT,
        ),
        "biggest_takeaway": input("What was your biggest takeaway from yesterday? "),
        # ... other data ...
    }

    logger.info("Data preparation for the document is complete.")

    rendered_content = template.render(data)
    logger.info("Document rendered successfully.")

    file_path = SAVE_LOCATION + f"{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(rendered_content)
    logger.info(f"Morning briefing document saved successfully at {file_path}.")
