import json
import time
from typing import List, Optional

from requests import Response
from slack import WebClient

from .models import Message


class BotSlackPlugin:
    def __init__(self, slack_token: str, channel: str, **kwargs):
        """
        BotSlackPlugin

        Args:
            slack_token (str): Authentication token.
            channel (str): Channel or private group to send message to. Can be an ID, or a name.
        """
        self._channel = channel
        self._client = WebClient(token=slack_token, **kwargs)
        self._member_list = self.client.users_list().get("members")

    @property
    def client(self):
        """
        Slack client instance.

        Returns:
            client: The slack client instance.

        """
        return self._client

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel

    def _id_for_username(self, username):
        member_list = self.client.users_list().get("members")

        for member in member_list:
            if member["real_name"] == username:
                return member["id"]
        return None

    def _get_users_mention(self, users: List[str]):
        if not users:
            return ""

        ids = []
        for user in users:
            ids.append(self._id_for_username(user))
        return " ".join([f"<@{id}>" for id in ids if id is not None])

    def send_simple_message(self, text: str, channel: Optional[str] = None, users: Optional[List[str]] = None,
                            attachment: Optional[bool] = False, **kwargs):
        """
        Sends a simple message.

        Args:
            text (str): The text of message.
            channel (str, optional): Channel or private group to send message to. Can be an ID, or a name.
            users (str): The usernames for mentions
            attachment (dict): For a simple message keep Default false.

        Returns:
            response: send message response.
        """
        return self.send_message(message=Message(text=text), channel=channel or self.channel, users=users,
                                 attachment=attachment, **kwargs)

    def send_message(self, message: Message, attachment: Optional[bool] = True, channel: Optional[str] = None,
                     users: Optional[List[str]] = None, **kwargs) -> Response:
        """
        Sends a more elaborate message via attachment.

        Args:
            message (Message): The full content of the message.See [Message][botcity.plugins.slack.models.Message].
            attachment (dict): For a message with attachment keep Default True.
            channel (str, optional): Channel or private group to send message to. Can be an ID, or a name.
            users (str): The usernames for mentions.
        Returns:
            response: send message response.
        """
        message.text = f"{self._get_users_mention(users)} {message.text}"
        return self.client.chat_postMessage(
            channel=channel or self.channel,
            attachments="" if not attachment else json.dumps([message.asdict()]),
            text=message.text, **kwargs)

    def update_message(self, response: Response, text: str, users: Optional[List[str]] = None) -> Response:
        """
        Update the message based on the response passed as argument.

        Args:
            message (Response): The response of sended message.
            text (str): The new text for message update.
            users (str): The usernames for mentions.
        Returns:
            response: update message response.
        """

        channel = response["channel"]

        ts = response["ts"]

        response.text = f"{self._get_users_mention(users)} {text}"
        return self.client.chat_update(channel=channel or self.channel,
                                       ts=ts, text=response.text)

    def delete_message(self, response: Response) -> Response:
        """
        Deletes the message based on the response passed as argument.

        Args:
            message (Response): The response of sended message.
        Returns:
            response: delete message response.
        """
        channel = response["channel"]
        ts = response["ts"]
        return self.client.chat_delete(channel=channel, ts=ts)

    def upload_file(self, file: str, channel: Optional[str] = None, text_for_file: Optional[str] = None,
                    title_for_file: Optional[str] = None) -> Response:
        """
        Upload file to slack.

        Args:
            file (str): The file path.
            channel (str, optional): Channel or private channel to send message to. Can be an ID, or a name.
            text_for_file (str, optional): The text that comes before the file upload.
            text_for_file (str, optional): The File title.

        Returns:
            response: upload file response.
        """
        return self.client.files_upload(channels=channel or self.channel, file=file,
                                        initial_comment=text_for_file, title=title_for_file)

    def delete_file(self, response: Response) -> Response:
        """
        Deletes file based on the response of upload file passed as argument.

        Args:
            upload file (Response): Response of upload file.
        Returns:
            response: delete file response.
        """
        file_id = response["file"]["shares"]["public"]
        for key, value in file_id.items():
            value = value
            channel = key
        ts = [v["ts"] for v in value]
        return self.client.chat_delete(channel=channel, ts=ts)

    def get_replies(self, response: Response, **kwargs) -> List[Message]:
        """
        Update the message based on the response passed as argument.

        Args:
            message (Response): The response of sent message.

        Returns:
            List[Message]: List of replies.
        """
        channel = response["channel"]
        ts = response["ts"]
        replies = self.client.conversations_replies(channel=channel, ts=ts, **kwargs)
        return replies

    def get_text_replies(self, response: Response) -> List[str]:
        """
        Get the text of the message replied to in the thread based on the response passed as argument.

        Args:
            replies (Response): The response of get replies.

        Returns:
            List[str]: List of messages replies as string.
        """
        message_thread = []
        [message_thread.append(message['text']) for message in response['messages']]
        if len(message_thread) <= 1:
            return []
        return message_thread[1:]

    def get_member_by_id(self, id: str):
        for member in self._member_list:
            if member["id"] == id:
                return member

    def wait_for_reply(self, response: Response, timeout: int = 300) -> List[dict]:
        """
        Wait for a new message until a timeout.

        Args:
            message (Response): The response of sent message.
            timeout (int): The maximum waiting time (in seconds). Defaults to 300s.

        Returns:
            List[dict]: The dict to text and member.
        """
        reply_count = len(self.get_text_replies(self.get_replies(response=response)))
        start_time = time.time()
        messages_to_return = []
        while True:
            elapsed_time = (time.time() - start_time)
            if elapsed_time > timeout:
                return []
            replies = self.get_replies(response=response)
            messages_sent = self.get_text_replies(self.get_replies(response=response))
            if len(messages_sent) > reply_count:
                reply = replies.get("messages", [])[-1]
                text = reply.get("text")
                member = self.get_member_by_id(id=reply["user"])
                messages_to_return.append({"text": text, "member": member})
                return messages_to_return
            time.sleep(1)

    def reply(self, response: Response, msg: str, **kwargs) -> Response:
        """
        Reply to a previously received message.

        Args:
            message (Response): The response of sent message.
            msg: The message to reply.

        Returns:
            response: send message response.
        """
        for threads in response['messages']:
            if 'thread_ts' in threads:
                return self.send_simple_message(text=msg, thread_ts=threads['thread_ts'])
            else:
                return self.send_simple_message(text=msg, thread_ts=threads['ts'])
