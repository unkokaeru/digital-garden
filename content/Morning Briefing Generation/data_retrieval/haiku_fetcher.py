"""Haiku Fetcher"""
from random import randint
from utils.logger import get_logger


def get_haiku(doc_loc: str) -> str:
    """
    A function to get a haiku from a markdown document.

    :param doc_loc: The location of the markdown document containing the haikus.
    :return: A random haiku from the document.
    """

    logger = get_logger()  # Initialize the logger
    logger.info(f"Starting to get a haiku from {doc_loc}.")

    # create an array of haikus from the markdown document
    haikus = []
    with open(doc_loc, "r") as f:
        logger.info(f"Opened {doc_loc}.")
        haiku = ""
        for line in f:
            if line.startswith(">"):
                haiku += line
            else:
                haikus.append(haiku)
                haiku = ""
        logger.info("Completed reading haikus from the document.")

    # return a random haiku from the array
    random_index = randint(0, len(haikus) - 1)
    logger.info(f"Returning haiku at index {random_index}.")
    return haikus[random_index]
