import os
import time
from datetime import datetime
from typing import List

import requests
from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance

from .utils import MEDIA_TYPES


class BotTwilioWhatsappPlugin:

    def __init__(self, account_sid: str, auth_token: str, whatsapp_number: str) -> None:
        """
        BotTwilioWhatsapp.

        Args:
            account_sid (str): The unique Account Sid of your Twilio account.
            auth_token: The unique Auth Token of your Twilio account.
            whatsapp_number (str): A number that is active on your Twilio account to be used for sending messages.
                The number must be informed in this format: [+][country code][phone number including area code]
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.whatsapp_number = whatsapp_number

        self._client = Client(self.account_sid, self.auth_token)

    @property
    def whatsapp_number(self) -> str:
        """
        The Whatsapp number that will be used to send messages.
        """
        return self._whatsapp_number

    @whatsapp_number.setter
    def whatsapp_number(self, number):
        self._whatsapp_number = number

    def send_message(self, to_number: str, msg_content: str, media_url: str = None) -> None:
        """
        Sends an message via Whatsapp to the specified number.
        The to_number must be informed in this format: [+][country code][phone number including area code]

        Args:
            to_number (str): The Whatsapp number that will receive the message.
            msg_content (str): The message body content.
            media_url (str, optional): The URL of a media content that will be sent in the message.
        """
        if "whatsapp:" not in to_number:
            to_number = "whatsapp:" + to_number

        self._client.messages.create(
            to=to_number,
            from_="whatsapp:" + self.whatsapp_number,
            body=msg_content,
            media_url=media_url
        )

    def get_sent_messages(self, to_number: str = None, before_date: datetime = None, after_date: datetime = None,
                          on_date: datetime = None, limit: int = None) -> List[MessageInstance]:
        """
        Get all messages that were sent by the configured Whatsapp number.

        Args:
            to_number (str, optional): Filters messages that were sent only to this number.
            before_date (datetime, optional): Filters messages that were sent before this specific date.
            after_date (datetime, optional): Filters messages that were sent after this specific date.
            on_date (datetime, optional): Filters messages that were sent on this specific date.
            limit (int, optional): The maximum number of messages that will be returned.

        Returns:
            List[MessageInstance]: The list containing the messages found.
        """
        if to_number:
            to_number = "whatsapp:" + to_number

        messages = self._client.messages.list(
            to=to_number,
            from_="whatsapp:" + self.whatsapp_number,
            date_sent_before=before_date,
            date_sent_after=after_date,
            date_sent=on_date,
            limit=limit
        )
        return messages

    def get_received_messages(self, from_number: str = None, before_date: datetime = None,
                              after_date: datetime = None, on_date: datetime = None,
                              limit: int = None) -> List[MessageInstance]:
        """
        Get all messages that were received by the configured Whatsapp number.

        Args:
            from_number (str, optional): Filters messages that were received only from this number.
            before_date (datetime, optional): Filters messages that were received before this specific date.
            after_date (datetime, optional): Filters messages that were received after this specific date.
            on_date (datetime, optional): Filters messages that were received on this specific date.
            limit (int, optional): The maximum number of messages that will be returned.

        Returns:
            List[MessageInstance]: The list containing the messages found.
        """
        if from_number:
            from_number = "whatsapp:" + from_number

        messages = self._client.messages.list(
            to="whatsapp:" + self.whatsapp_number,
            from_=from_number,
            date_sent_before=before_date,
            date_sent_after=after_date,
            date_sent=on_date,
            limit=limit
        )
        return messages

    def reply_message(self, msg: MessageInstance, text_content: str, media_url: str = None) -> None:
        """
        Reply to a previously received message.

        Args:
            msg (MessageInstance): The message to reply.
            text_content (str): The body of the reply message.
            media_url (str, optional): The URL of a media content that will be sent in the message.
        """
        self.send_message(to_number=msg.from_, msg_content=text_content, media_url=media_url)

    def wait_for_new_message(self, from_number: str = None, timeout: int = 60) -> MessageInstance:
        """
        Wait for a new message until a timeout.

        Args:
            from_number (str, optional): Wait for a new message from this specific number.
                Defaults to any new message.
            timeout (int): The maximum waiting time (in seconds). Defaults to 60s.

        Returns:
            MessageInstance: The new message received. None otherwise.
        """
        msg_count = len(self.get_received_messages(from_number))
        start_time = time.time()

        while True:
            elapsed_time = (time.time() - start_time)
            if elapsed_time > timeout:
                return None
            messages = self.get_received_messages(from_number)
            if len(messages) > msg_count:
                return messages[0]
            time.sleep(1)

    def download_media_file(self, msg: MessageInstance, download_folder_path: str = None) -> None:
        """
        Download the media content from a message and save on disk.

        Args:
            msg (MessageInstance): The message that contains a media content.
            download_folder_path (str, optional): The folder where the file will be saved.
                Defaults to the current working directory.
        """
        if not download_folder_path:
            download_folder_path = os.getcwd()

        if int(msg.num_media) > 0:
            for media in msg.media.list():
                media_url = "https://api.twilio.com" + media.uri[:-5]
                media_type = MEDIA_TYPES.get(media.content_type)

                if media_type:
                    file_name = media.sid + media_type
                    file_path = os.path.join(download_folder_path, file_name)
                    try:
                        response = requests.get(media_url)
                        response.raise_for_status()
                    except requests.HTTPError as ex:
                        raise Exception('''Failed to download media content.
                        Please verify that the message has valid media content.''') from ex
                    with open(file_path, "wb") as file:
                        file.write(response.content)
