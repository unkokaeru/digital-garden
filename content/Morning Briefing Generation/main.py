"""A script to generate a morning briefing in a markdown document."""
from template_rendering.markdown_generator import doc_gen
from utils.logger import get_logger

# TODO: Add tests with pytest and pytest-cov (see tests/morning_briefing_tests.py)
# TODO: Add Bing API integration for current data for the career information section
# TODO: Add asynchronicity to the script (asyncio, httpx, asyncio TaskGroup)
# TODO: Call my phone and play the mp3 file (generated with GPT-4 and TTS) with a phone API (Twilio?)
# TODO: Add a GUI (PySimpleGUI? Streamlit? Tkinter? PyQt?): customise what is included in the briefing, and when it is generated

logger = get_logger()  # Initialize the logger


def main() -> None:
    """
    A function to generate a morning briefing in a markdown document, and save it to the "Day by day" folder.

    :return: None
    """
    logger.info(
        "Starting the script for generating a morning briefing."
    )  # Log the start of the script

    logger.info(
        "Beginning the generation of the markdown document."
    )  # Log before document generation
    doc_gen()  # Generate the markdown document
    logger.info(
        "Markdown document generation completed."
    )  # Log after document generation


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.error("\nExiting due to KeyboardInterrupt.")
        exit()
    except FileNotFoundError as e:
        logger.error(f"File Error: {e}")
        exit()
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        exit()
