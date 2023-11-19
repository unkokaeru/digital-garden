"""Configuration file for the morning briefing application."""
import os

from rich.logging import RichHandler

# AI Prompting Configuration
# CAREER_PROMPT = "Given that I live in Lincoln, UK: Provide a daily update on job market trends for maths graduates, available scholarships or grants for further mathematics studies, upcoming maths conferences or workshops, and career advice for a maths student. Keep it fairly short, and well formatted for a markdown document."
CAREER_PROMPT = "Could I have some career advice for a maths student? What should I be doing right now to prepare for my future, what skills should I learn, habits to build, mindsets to nurture, etc."
MATHS_PROMPT = "Generate an interesting maths problem for a maths undergraduate student to solve in about five minutes. Use Markdown and Latex if needed. Do not provide a solution, just a final answer."
PREDICTION_PROMPT = (
    "How do you think my day will go today? Answer in a short paragraph."
)
PREDICTION_CONTEXT = "You are an older version of me: a maths student from Lincoln University and a personal tutor, although I'm currently quite stressed about exams etc."
LUCK_PROMPT = "Give me a short good luck message! :D"
LUCK_CONTEXT = "You are a fun motivator!"
EMOJI_PROMPT = "Give me some random emojis! :D"

# RSS Feed URLs
RSS_URLS = {
    "Global News": [
        "http://feeds.bbci.co.uk/news/world/rss.xml",  # BBC World News
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",  # NY Times World News
        "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera English
        "https://www3.nhk.or.jp/rj/podcast/rss/english.xml",  # NHK World English
    ],
    "Lincoln News": [
        "https://www.lincolnshirelive.co.uk/news/?service=rss",  # Lincolnshire Live
        "https://thelincolnite.co.uk/feed/",  # The Lincolnite
    ],
    "Mathematical News": [
        "https://www.sciencedaily.com/rss/strange_offbeat.xml",  # ScienceDaily - Strange & Offbeat
        "https://www.sciencedaily.com/rss/top/science.xml",  # ScienceDaily - Top Science News
        "https://www.ams.org/rss/mathmoments.xml",  # AMS - Math Moments
        "https://www.ams.org/rss/conm.rss",  # AMS - Contemporary Mathematics
    ],
}

# ICS Calendar URLs
CAL_URLS = [
    "https://calendar.google.com/calendar/ical/wills%40fayers.com/private-60149c6c42b754d0c98bbcfc72cc47ef/basic.ics",
    "https://calendar.google.com/calendar/ical/c_417sngltsr9kp47l52c9978du0%40group.calendar.google.com/private-735f2692630830375e8a3007ee272360/basic.ics",
    "https://blackboard.lincoln.ac.uk/webapps/calendar/calendarFeed/bf8217b5a6ef45099542d518470fdb29/learn.ics",
    "https://timetable.lincoln.ac.uk/ical/8OzbTTa18Dagy6spCOpfPixa2aOdIJeyrPczNPOva3X89vnBIBPYMEKkYa3pTYdZAT14LfwGmAQ",
]

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(message)s",
    "datefmt": "[%X]",
    "handlers": [RichHandler(rich_tracebacks=True)],
}

# File Paths
HAIKU_PATH = (
    "C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\My Haikus.md"
)

# fetch API keys from .env file or prompt user to enter them manually
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", input("Enter your OpenAI API key: "))
OPEN_WEATHER_API_KEY = os.getenv(
    "OPEN_WEATHER_API_KEY", input("Enter your OpenWeather API key: ")
)

# Gmail API Credentials
CREDS_PATH = "C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\Morning Briefing Generation\\config\\credentials.json"

# Where to save the generated markdown document
SAVE_LOCATION = (
    "C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\Day by day\\"
)
