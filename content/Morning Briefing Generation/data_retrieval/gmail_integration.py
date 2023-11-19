"""Contains functions for fetching data from Gmail."""
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config.cfg import CREDS_PATH
from utils.logger import get_logger


def fetch_email_subjects() -> str:
    """
    Fetch the subjects of the user's emails and return them in a markdown formatted string.

    :return: A markdown formatted string containing the subjects of the emails.
    """

    logger = get_logger()  # Initialize the logger
    logger.info("Starting to fetch email subjects.")

    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    if os.path.exists("token.pickle"):
        logger.info("Loading credentials from token.pickle.")
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no valid credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logger.info("Refreshing credentials.")
            creds.refresh(Request())
        else:
            logger.info("Fetching new credentials.")
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDS_PATH,
                ["https://www.googleapis.com/auth/gmail.readonly"],
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
            logger.info("Credentials saved to token.pickle.")

    logger.info("Credentials authenticated. Building Gmail service.")
    service = build("gmail", "v1", credentials=creds)

    logger.info("Fetching email subjects.")
    results = service.users().messages().list(userId="me", labelIds=["INBOX"]).execute()
    messages = results.get("messages", [])

    email_subjects_md = ""

    if not messages:
        logger.info("No messages found.")
        return email_subjects_md + "No messages found.\n"
    else:
        for message in messages:
            msg = (
                service.users()
                .messages()
                .get(userId="me", id=message["id"], format="metadata")
                .execute()
            )
            headers = msg.get("payload", {}).get("headers", [])
            subject = next(
                (
                    header["value"]
                    for header in headers
                    if header["name"].lower() == "subject"
                ),
                "No Subject",
            )
            email_subjects_md += f"- {subject}\n"
            logger.info(f"Added email subject: {subject}")
        logger.info("Finished fetching email subjects.")

    return email_subjects_md
