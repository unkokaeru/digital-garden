# new-morning-briefing

A script to generate a morning briefing in a markdown document

<a id="new-morning-briefing.get_haiku"></a>

#### get\_haiku

```python
def get_haiku(doc_loc: str) -> str
```

A function to get a haiku from a markdown document.

**Arguments**:

- `doc_loc`: The location of the markdown document containing the haikus.

**Returns**:

A random haiku from the document.

<a id="new-morning-briefing.fetch_api_data"></a>

#### fetch\_api\_data

```python
def fetch_api_data(url: str,
                   headers: dict = None,
                   params: dict = None) -> dict
```

Fetch data from the given API URL and return JSON data.

**Arguments**:

- `url`: The URL of the API to fetch data from.
- `headers`: A dictionary of headers to send with the request.
- `params`: A dictionary of parameters to send with the request.

**Returns**:

The JSON data returned from the API.

<a id="new-morning-briefing.get_weather"></a>

#### get\_weather

```python
def get_weather(api_key: str, location: str) -> str
```

Get the current weather and overall forecast for the day.

**Arguments**:

- `api_key`: The API key for the OpenWeatherMap API.
- `location`: The location to get the weather for.

**Returns**:

A string containing the current weather and forecast for the day.

<a id="new-morning-briefing.fetch_news"></a>

#### fetch\_news

```python
def fetch_news(rss_urls: dict, max_articles_per_category: int = 5) -> str
```

Fetches a limited number of news articles from multiple RSS feed URLs, alternating between sources.

**Arguments**:

- `rss_urls`: A dictionary of RSS feed URLs, with the key being the category and the value being a list of URLs.
- `max_articles_per_category`: The maximum number of articles to fetch per category.

**Returns**:

A string containing the news articles in Markdown

<a id="new-morning-briefing.prompt_gpt4_turbo"></a>

#### prompt\_gpt4\_turbo

```python
def prompt_gpt4_turbo(
        api_key: str,
        user_message: str,
        system_message: str = "You are a helpful assistant.") -> str
```

A function to prompt the ChatGPT API to generate a response to a user message.

**Arguments**:

- `api_key`: The API key for the OpenAI API.
- `user_message`: The user's message to respond to.
- `system_message`: The system's message to respond to.

**Returns**:

The response from the ChatGPT API.

<a id="new-morning-briefing.fetch_chess_puzzle"></a>

#### fetch\_chess\_puzzle

```python
def fetch_chess_puzzle(query: dict) -> str
```

Fetch a chess puzzle from lichess.org and return its details in a formatted string.

**Arguments**:

- `query`: A dictionary containing the query parameters for the API.

**Returns**:

A string with the puzzle's FEN, rating, and solution.

<a id="new-morning-briefing.fetch_calendar_events"></a>

#### fetch\_calendar\_events

```python
def fetch_calendar_events(urls: list) -> str
```

Fetch calendar events from multiple .ics URLs and return a markdown formatted string.

Only events for the current day are returned.

**Arguments**:

- `urls`: A list of .ics URLs.

**Returns**:

A markdown formatted string with today's events from all the calendars.

<a id="new-morning-briefing.fetch_email_subjects"></a>

#### fetch\_email\_subjects

```python
def fetch_email_subjects() -> str
```

Fetch the subjects of the user's emails and return them in a markdown formatted string.

**Returns**:

A markdown formatted string containing the subjects of the emails.

<a id="new-morning-briefing.main"></a>

#### main

```python
def main() -> None
```

A function to generate a morning briefing in a markdown document, and save it to the "Day by day" folder. Then generate a summary of the document for text-to-speech.

**Returns**:

None

