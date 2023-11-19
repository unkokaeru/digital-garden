<a id="main"></a>

# main

A script to generate a morning briefing in a markdown document.

<a id="main.logger"></a>

#### logger

Initialize the logger

<a id="main.main"></a>

#### main

```python
def main() -> None
```

A function to generate a morning briefing in a markdown document, and save it to the "Day by day" folder.

**Returns**:

None

<a id="config"></a>

# config

<a id="config.cfg"></a>

# config.cfg

Configuration file for the morning briefing application.

<a id="data_retrieval"></a>

# data\_retrieval

<a id="data_retrieval.calendar_integration"></a>

# data\_retrieval.calendar\_integration

Calendar integration module.

<a id="data_retrieval.calendar_integration.fetch_calendar_events"></a>

#### fetch\_calendar\_events

```python
def fetch_calendar_events(urls: list[str]) -> str
```

Fetch calendar events from multiple .ics URLs and return a markdown formatted string.

Only events for the current day are returned.

**Arguments**:

- `urls`: A list of .ics URLs.

**Returns**:

A markdown formatted string with today's events from all the calendars.

<a id="data_retrieval.chess_fetcher"></a>

# data\_retrieval.chess\_fetcher

Contains functions for fetching data from lichess.org.

<a id="data_retrieval.chess_fetcher.fetch_chess_puzzle"></a>

#### fetch\_chess\_puzzle

```python
def fetch_chess_puzzle(query: dict[str, str]) -> str
```

Fetch a chess puzzle from lichess.org and return its details in a formatted string.

**Arguments**:

- `query`: A dictionary containing the query parameters for the API.

**Returns**:

A string with the puzzle's FEN, rating, and solution.

<a id="data_retrieval.gmail_integration"></a>

# data\_retrieval.gmail\_integration

Contains functions for fetching data from Gmail.

<a id="data_retrieval.gmail_integration.fetch_email_subjects"></a>

#### fetch\_email\_subjects

```python
def fetch_email_subjects() -> str
```

Fetch the subjects of the user's emails and return them in a markdown formatted string.

**Returns**:

A markdown formatted string containing the subjects of the emails.

<a id="data_retrieval.haiku_fetcher"></a>

# data\_retrieval.haiku\_fetcher

Haiku Fetcher

<a id="data_retrieval.haiku_fetcher.get_haiku"></a>

#### get\_haiku

```python
def get_haiku(doc_loc: str) -> str
```

A function to get a haiku from a markdown document.

**Arguments**:

- `doc_loc`: The location of the markdown document containing the haikus.

**Returns**:

A random haiku from the document.

<a id="data_retrieval.openai_integration"></a>

# data\_retrieval.openai\_integration

OpenAI API integration functions.

<a id="data_retrieval.openai_integration.prompt_gpt4_turbo"></a>

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

<a id="data_retrieval.questions_fetcher"></a>

# data\_retrieval.questions\_fetcher

Contains functions for retrieving questions from the database.

<a id="data_retrieval.questions_fetcher.get_driving_questions"></a>

#### get\_driving\_questions

```python
def get_driving_questions(num: int = 3) -> str
```

Get a list of questions to ask myself each day.

**Arguments**:

- `num`: The number of questions to return.

**Returns**:

A string containing the questions.

<a id="data_retrieval.rss_fetcher"></a>

# data\_retrieval.rss\_fetcher

Fetches news articles from RSS feeds.

<a id="data_retrieval.rss_fetcher.fetch_news"></a>

#### fetch\_news

```python
def fetch_news(rss_urls: dict[str, list[str]],
               max_articles_per_category: int = 5) -> str
```

Fetches a limited number of news articles from multiple RSS feed URLs, alternating between sources.

**Arguments**:

- `rss_urls`: A dictionary of RSS feed URLs, with the key being the category and the value being a list of URLs.
- `max_articles_per_category`: The maximum number of articles to fetch per category.

**Returns**:

A string containing the news articles in Markdown

<a id="data_retrieval.weather_fetcher"></a>

# data\_retrieval.weather\_fetcher

Functions for fetching weather data from the OpenWeatherMap API.

<a id="data_retrieval.weather_fetcher.get_weather"></a>

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

<a id="template_rendering"></a>

# template\_rendering

<a id="template_rendering.markdown_generator"></a>

# template\_rendering.markdown\_generator

Generates a markdown document with a morning briefing for the user.

<a id="template_rendering.markdown_generator.doc_gen"></a>

#### doc\_gen

```python
def doc_gen() -> None
```

A function to generate a morning briefing in a markdown document, and save it to the "Day by day" folder.

**Returns**:

None

<a id="utils"></a>

# utils

<a id="utils.logger"></a>

# utils.logger

Contains the logger for the application.

<a id="utils.logger.get_logger"></a>

#### get\_logger

```python
def get_logger() -> logging.Logger
```

Get the logger for the application.

**Returns**:

The logger for the application.

<a id="utils.network_utils"></a>

# utils.network\_utils

Contains utility functions for network requests.

<a id="utils.network_utils.fetch_api_data"></a>

#### fetch\_api\_data

```python
def fetch_api_data(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None) -> Optional[Dict[str, str]]
```

Fetch data from the given API URL and return JSON data.

**Arguments**:

- `url`: The URL of the API to fetch data from.
- `headers`: A dictionary of headers to send with the request.
- `params`: A dictionary of parameters to send with the request.

**Returns**:

The JSON data returned from the API.

