"""Functions for fetching weather data from the OpenWeatherMap API."""
from collections import Counter
from typing import cast

from utils.logger import get_logger
from utils.network_utils import fetch_api_data


def get_weather(api_key: str, location: str) -> str:
    """
    Get the current weather and overall forecast for the day.

    :param api_key: The API key for the OpenWeatherMap API.
    :param location: The location to get the weather for.
    :return: A string containing the current weather and forecast for the day.
    """

    logger = get_logger()  # Initialize the logger
    logger.info(f"Starting to get weather data for {location}.")

    # URLs for current weather and forecast data
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"

    logger.info(f"Fetching weather data from {weather_url}.")
    weather_data = cast(dict, fetch_api_data(weather_url))
    if not weather_data:
        logger.error("Failed to fetch weather data.")
        return "..."

    main = weather_data["main"]
    weather_desc = weather_data["weather"][0]["description"]
    current_weather = f"Current weather in {location} is {weather_desc} with a temperature of {main['temp']}°C."
    logger.info(f"Current weather in {location} is {weather_desc}.")

    logger.info(f"Fetching forecast data from {forecast_url}.")
    forecast_data = cast(dict, fetch_api_data(forecast_url))
    if not forecast_data:
        logger.error("Failed to fetch forecast data.")
        return current_weather

    # Filtering forecasts for today
    today_forecast = [
        forecast
        for forecast in forecast_data["list"]
        if forecast["dt_txt"].split()[0]
        == forecast_data["list"][0]["dt_txt"].split()[0]
    ]

    # Calculate average temperature for the day
    average_temp = sum(forecast["main"]["temp"] for forecast in today_forecast) / len(
        today_forecast
    )

    # Determine the most frequent weather description for the day
    descriptions = [
        forecast["weather"][0]["description"] for forecast in today_forecast
    ]
    most_frequent_desc = Counter(descriptions).most_common(1)[0][0]

    logger.info("Completed fetching weather data.")
    forecast_str = f"Overall forecast for {location} today is {most_frequent_desc} with an average temperature of {average_temp:.1f}°C."

    return current_weather + " " + forecast_str
