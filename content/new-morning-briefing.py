"""A script to generate a morning briefing in a markdown document"""
import random
import os.path as path
from os import environ
from datetime import datetime
import requests
from collections import Counter
import feedparser
from itertools import islice, cycle
from openai import OpenAI
from icalendar import Calendar
import urllib3
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
from googleapiclient.discovery import build
from gtts import gTTS


# Disable SSL warnings (temporary workaround)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Global, local, and mathematical RSS feed URLs
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
    ]
}
CAL_URLS = [
    "https://calendar.google.com/calendar/ical/wills%40fayers.com/private-60149c6c42b754d0c98bbcfc72cc47ef/basic.ics",
    "https://calendar.google.com/calendar/ical/c_417sngltsr9kp47l52c9978du0%40group.calendar.google.com/private-735f2692630830375e8a3007ee272360/basic.ics",
    "https://blackboard.lincoln.ac.uk/webapps/calendar/calendarFeed/bf8217b5a6ef45099542d518470fdb29/learn.ics",
    "https://timetable.lincoln.ac.uk/ical/8OzbTTa18Dagy6spCOpfPixa2aOdIJeyrPczNPOva3X89vnBIBPYMEKkYa3pTYdZAT14LfwGmAQ"
]


def get_haiku(doc_loc: str) -> str:
    """
    A function to get a haiku from a markdown document.

    :param doc_loc: The location of the markdown document containing the haikus.
    :return: A random haiku from the document.
    """
    
    # create an array of haikus from the markdown document
    haikus = []
    with open(path.dirname(path.realpath(__file__)) + "\\" + doc_loc, "r") as f:
        haiku = ""
        for line in f:
            if line.startswith(">"):
                haiku += line
            else:
                haikus.append(haiku)
                haiku = ""

    # return a random haiku from the array
    return haikus[random.randint(0, len(haikus) - 1)]


def fetch_api_data(url: str, headers: dict = None, params: dict = None) -> dict:
    """
    Fetch data from the given API URL and return JSON data.
    
    :param url: The URL of the API to fetch data from.
    :param headers: A dictionary of headers to send with the request.
    :param params: A dictionary of parameters to send with the request.
    :return: The JSON data returned from the API.
    """

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None


def get_weather(api_key: str, location: str) -> str:
    """
    Get the current weather and overall forecast for the day.
    
    :param api_key: The API key for the OpenWeatherMap API.
    :param location: The location to get the weather for.
    :return: A string containing the current weather and forecast for the day.
    """
    
    # URLs for current weather and forecast data
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"

    # Fetching the current weather data
    weather_data = fetch_api_data(weather_url)
    if not weather_data:
        return "Couldn't get current weather data."

    main = weather_data['main']
    weather_desc = weather_data['weather'][0]['description']
    current_weather = f"Current weather in {location} is {weather_desc} with a temperature of {main['temp']}°C."

    # Fetching the forecast data
    forecast_data = fetch_api_data(forecast_url)
    if not forecast_data:
        return current_weather + " Couldn't get forecast data."

    # Filtering forecasts for today
    today_forecast = [forecast for forecast in forecast_data['list'] 
                      if forecast['dt_txt'].split()[0] == forecast_data['list'][0]['dt_txt'].split()[0]]

    # Calculate average temperature for the day
    average_temp = sum(forecast['main']['temp'] for forecast in today_forecast) / len(today_forecast)

    # Determine the most frequent weather description for the day
    descriptions = [forecast['weather'][0]['description'] for forecast in today_forecast]
    most_frequent_desc = Counter(descriptions).most_common(1)[0][0]

    forecast_str = f"Overall forecast for {location} today is {most_frequent_desc} with an average temperature of {average_temp:.1f}°C."
    
    return current_weather + " " + forecast_str


def fetch_news(rss_urls: dict, max_articles_per_category: int = 5) -> str:
    """
    Fetches a limited number of news articles from multiple RSS feed URLs, alternating between sources.
    
    :param rss_urls: A dictionary of RSS feed URLs, with the key being the category and the value being a list of URLs.
    :param max_articles_per_category: The maximum number of articles to fetch per category.
    :return: A string containing the news articles in Markdown
    """
    
    markdown_output = ""
    
    for category, urls in rss_urls.items():
        markdown_output += f"## {category}\n\n"
        seen_titles = set()  # Set to store titles for deduplication
        articles_count = 0

        # Create an iterator that cycles through the URLs
        url_cycle = cycle(urls)
        while articles_count < max_articles_per_category:
            url = next(url_cycle)  # Get the next URL in the cycle
            try:
                feed = feedparser.parse(url)
                if feed.bozo:
                    continue

                # Use islice to get an iterator for the first unseen entry
                entries = (entry for entry in feed.entries if entry.title not in seen_titles)
                entry = next(islice(entries, 1), None)
                
                # If we have an unseen entry, process it
                if entry:
                    title = entry.title
                    link = entry.link
                    markdown_output += f"- [{title}]({link})\n"
                    seen_titles.add(title)
                    articles_count += 1
            except Exception as e:
                print(f"An error occurred while fetching news from {url}: {e}")
                continue  # Continue with the next URL if an error occurred

        markdown_output += "\n"

    return markdown_output


def prompt_gpt4_turbo(api_key: str, user_message: str, system_message: str = "You are a helpful assistant.") -> str:
    """
    A function to prompt the ChatGPT API to generate a response to a user message.

    :param api_key: The API key for the OpenAI API.
    :param user_message: The user's message to respond to.
    :param system_message: The system's message to respond to.
    :return: The response from the ChatGPT API.
    """
    
    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


def fetch_chess_puzzle(query: dict) -> str:
    """
    Fetch a chess puzzle from lichess.org and return its details in a formatted string.

    :param query: A dictionary containing the query parameters for the API.
    :return: A string with the puzzle's FEN, rating, and solution.
    """

    url = "https://chess-puzzles.p.rapidapi.com/"
    headers = {
        "X-RapidAPI-Key": "90d069b03emsh494903ef45a4734p10d481jsn832ac943fdeb",
        "X-RapidAPI-Host": "chess-puzzles.p.rapidapi.com"
    }

    puzzle_data = fetch_api_data(url, headers, query)

    if puzzle_data is None:
        return "Error fetching puzzle data."

    try:
        puzzle = puzzle_data['puzzles'][0]
        puzzle_details = (
            f"Rating: {puzzle['rating']}\n"
            f"Puzzle ID: [{puzzle['puzzleid']}](lichess.org/training/{puzzle['puzzleid']})\n"
            "```chessboard\n"
            f"fen: {puzzle['fen']}\n"
            "```\n"
            "#### Solution\n"
            "```spoiler-block\n"
            f"{puzzle['moves']}\n"
            "```"
        )
        return puzzle_details
    except (KeyError, IndexError):
        return "Error processing puzzle data."


def fetch_calendar_events(urls: list) -> str:
    """
    Fetch calendar events from multiple .ics URLs and return a markdown formatted string.
    Only events for the current day are returned.

    :param urls: A list of .ics URLs.
    :return: A markdown formatted string with today's events from all the calendars.
    """
    markdown_output = ""
    today = datetime.now().date()  # Get the current date

    for url in urls:
        try:
            response = requests.get(url, verify=False) # Verify is set to False to ignore SSL certificate errors (temporary workaround)
            response.raise_for_status()

            calendar = Calendar.from_ical(response.content)

            for component in calendar.walk():
                if component.name == "VEVENT":
                    summary = component.get('summary')
                    start = component.get('dtstart')
                    end = component.get('dtend')

                    if start and start.dt:
                        # If start.dt is a datetime object, convert to date for comparison
                        start_date = start.dt.date() if isinstance(start.dt, datetime) else start.dt
                        if start_date == today:
                            start_fmt = start.dt.strftime('%Y-%m-%d %H:%M:%S') if isinstance(start.dt, datetime) else 'All Day/Not Specified'
                            end_fmt = end.dt.strftime('%Y-%m-%d %H:%M:%S') if end and isinstance(end.dt, datetime) else 'All Day/Not Specified'

                            markdown_output += f"- **{summary}**\n  - Start: {start_fmt}\n  - End: {end_fmt}\n\n"
        except requests.RequestException as e:
            markdown_output += f"Failed to fetch calendar from {url}: {e}\n\n"
        except Exception as e:
            markdown_output += f"Error processing calendar from {url}: {e}\n\n"


    return markdown_output


def fetch_email_subjects() -> str:
    """
    Fetch the subjects of the user's emails and return them in a markdown formatted string.

    :return: A markdown formatted string containing the subjects of the emails.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    if os.path.exists(path.dirname(path.realpath(__file__)) + "\\" + 'token.pickle'):
        with open(path.dirname(path.realpath(__file__)) + "\\" + 'token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no valid credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                path.dirname(path.realpath(__file__)) + "\\" + 'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(path.dirname(path.realpath(__file__)) + "\\" + 'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    email_subjects_md = "### Email Subjects:\n"

    if not messages:
        return email_subjects_md + "No messages found.\n"
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='metadata').execute()
            headers = msg.get("payload", {}).get("headers", [])
            subject = next((header['value'] for header in headers if header['name'].lower() == 'subject'), "No Subject")
            email_subjects_md += f"- {subject}\n"
    
    return email_subjects_md



def main() -> None:
    """
    A function to generate a morning briefing in a markdown document, and save it to the "Day by day" folder. Then generate a summary of the document for text-to-speech.

    :return: None
    """

    # environment variables (API keys)
    try:
        OPENAI_API_KEY = environ["OPENAI_API_KEY"] # OpenAI API key
        OPEN_WEATHER_API_KEY = environ["OPEN_WEATHER_API_KEY"] # OpenWeatherMap API key
    except KeyError as e:
        print(f"Error: {e}")
        OPENAI_API_KEY = input("Please enter your OpenAI API key manually: ")
        OPEN_WEATHER_API_KEY = input("Please enter your OpenWeatherMap API key manually: ")

    # variables
    haiku = get_haiku("My Haikus.md") # one of the ten haikus
    print("Fetched haiku.")
    date = datetime.now().strftime("%Y-%m-%d") # today's date
    print("Fetched date.")
    weather = get_weather(OPEN_WEATHER_API_KEY,"Lincoln, UK") # fetch from weather API
    print("Fetched weather.")
    news = fetch_news(RSS_URLS) # fetch from news APIs - TODO: Allow user to choose how many articles to fetch - maybe based on energy level? Honeyman?
    print("Fetched news.")
    career_information = prompt_gpt4_turbo(OPENAI_API_KEY,"Given that I live in Lincoln, UK: Provide a daily update on job market trends for maths graduates, available scholarships or grants for further mathematics studies, upcoming maths conferences or workshops, and career advice for a maths student. Keep it fairly short, and well formatted for a markdown document.") # fetch from ChatGPT API
    print("Fetched career information.")
    maths_problem = prompt_gpt4_turbo(OPENAI_API_KEY,"Generate an interesting maths problem for a maths undergraduate student to solve in about five minutes. Use Markdown and Latex if needed. Do not provide a solution, just a final answer.") # fetch from ChatGPT API
    print("Fetched maths problem.")
    calendar_events = fetch_calendar_events(CAL_URLS) # fetch from calendar API
    print("Fetched calendar events.")
    emails = fetch_email_subjects() # fetch from email API
    print("Fetched emails.")
    day_prediction = prompt_gpt4_turbo(OPENAI_API_KEY,"How do you think my day will go today? Answer in a short paragraph.", "You are an older version of me: a maths student from Lincoln University and a personal tutor, although I'm currently quite stressed about exams etc.") # fetch from ChatGPT API
    print("Fetched day prediction.")
    chess_puzzle = fetch_chess_puzzle({"rating": "1500", "themesType": "ALL"}) # fetch from chess API
    print("Fetched chess puzzle.")
    good_luck_message = prompt_gpt4_turbo(OPENAI_API_KEY,"Give me a short good luck message! :D", "You are a fun motivator!") # fetch from ChatGPT API
    print("Fetched good luck message.")
    random_emojis = prompt_gpt4_turbo(OPENAI_API_KEY,"Give me five random, fun emojis, that's it.") # fetch from ChatGPT API
    print("Fetched random emojis.")
    biggest_takeaway = input("What was your biggest takeaway from yesterday? ") # user input
    print("Fetched biggest takeaway.")
    print("Finished fetching data.")
    print("Generating markdown document...")

    # markdown document
    md_doc = f"""
Start your day with one of these [[possible routines]]!

{haiku}
**Biggest takeaway from yesterday:** {biggest_takeaway}
[[Daily Note Generation]]
# Morning Briefing ({date})
*{weather}*
{news}

{career_information}

## Today's Maths Problem
{maths_problem}

## Today's Schedule
{calendar_events}

{emails}

*{day_prediction}*

## Chess Puzzle & Games
### Chess Puzzle
{chess_puzzle}
### Chess Games
*A space to log what chess games I've done today, as well as an analysis of them.*

...

## Good Luck! ✨
{good_luck_message}

### Now...
Have a look at the to-do list in [[The Scholar's Ledger]], or try some yoga/home calisthenics.

{random_emojis}
    """

    # save the markdown document
    with open(path.dirname(path.realpath(__file__)) + "\\Day by day\\" + f"{date}.md", "w", encoding="utf-8") as f:
        f.write(md_doc)

    print("Finished generating markdown document.")

    # Generate a summary of the document for text-to-speech
    doc_summary = prompt_gpt4_turbo("Please provide a short summary  of the following document so that it can be read by text-to-speech in a natural way: " + md_doc, "You are a text-to-speech program.")
    tts = gTTS(doc_summary, lang='en-gb')
    tts.save("speech.mp3") # save the summary as an mp3 file

    # TODO: Call my phone and play the mp3 file with a phone API


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except FileNotFoundError as e:
        print(f"File Error: {e}")
        exit()
    except KeyError as e:
        print(f"Key Error: {e}")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()