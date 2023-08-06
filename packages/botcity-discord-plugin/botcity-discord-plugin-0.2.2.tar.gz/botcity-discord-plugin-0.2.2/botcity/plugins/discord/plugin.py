import os
from typing import Dict, List, Union

from discord_webhook import DiscordEmbed, DiscordWebhook
from requests import Response

from .models import Color, EmbeddedMessage


class BotDiscordPlugin:
    def __init__(self, urls: Union[str, List[str]], username: str = None, **kwargs):
        """
        BotDiscordPlugin

        Args:
            urls (list or str): Webhook urls.
            username (str): The bot username
        """
        self._urls = urls
        self._username = username

    @property
    def webhook(self, **kwargs) -> DiscordWebhook:
        """
        Returns the discord-webhook instance.

        Returns:
            discord-webhook: The discord-webhook instance.
        """
        return DiscordWebhook(url=self._urls, username=self._username, **kwargs)

    def send_message(self, content: str, rate_limit_retry: bool = False,
                     allowed_mentions: List[str] = None, files: Union[List[str], Dict[str, bytes]] = None,
                     **kwargs) -> Response:
        """
        Sends a simple message.

        Args:
            content (str): The message content.
            rate_limit_retry (bool, optional): if rate_limit_retry is True then in the event that you are
                being rate limited by Discord your webhook will automatically be sent once
                the rate limit has been lifted
            allowed_mentions (list, optional): The list of users to ping.
            files (str): Add files.

        Returns:
            response: Webhook response.
        """
        files_dict = {}
        if isinstance(files, dict):
            files_dict = files
        else:
            for filepath in files or []:
                with open(file=filepath, mode='rb') as f:
                    files_dict[os.path.basename(filepath)] = f.read()

        webhook = DiscordWebhook(url=self._urls, username=self._username, files=files_dict, **kwargs)
        webhook.content = content
        webhook.rate_limit_retry = rate_limit_retry
        if allowed_mentions is not None:
            webhook.allowed_mentions = {"users": allowed_mentions}
        return webhook.execute()

    def send_embedded_message(self, message: EmbeddedMessage, **kwargs) -> Union[Response, List[Response]]:
        """
        Discord Embed Message.

        Args:
            message (EmbeddedMessage): The message content.
                See [EmbeddedMessage][botcity.plugins.discord.models.EmbeddedMessage]

        Returns:
            response: Webhook response.
        """
        if isinstance(message.color, Color):
            color = message.color.value
        else:
            color = message.color
        embed = DiscordEmbed(title=message.title, description=message.description, color=color)

        if message.author is not None:
            embed.set_author(name=message.author.name, url=message.author.url, icon_url=message.author.icon_url)

        if message.image is not None:
            embed.set_image(url=message.image)

        if message.thumbnail is not None:
            embed.set_thumbnail(url=message.thumbnail)

        if message.footer is not None:
            embed.set_footer(text=message.footer.text, icon_url=message.footer.icon_url)

        if message.timestamp is not None:
            embed.set_timestamp(timestamp=message.timestamp)
        else:
            embed.set_timestamp()

        if message.fields is not None:
            for field in message.fields:
                embed.add_embed_field(name=field.name, value=field.value)

        files_dict = {}
        if isinstance(message.files, dict):
            files_dict = message.files
        else:
            for filepath in message.files or []:
                with open(file=filepath, mode='rb') as f:
                    files_dict[os.path.basename(filepath)] = f.read()

        webhook = DiscordWebhook(url=self._urls, username=self._username, files=files_dict, **kwargs)
        webhook.add_embed(embed)
        return webhook.execute()

    def edit_message(self, message_response: Union[Response, List[Response]],
                     new_content_message: str, **kwargs) -> Union[Response, List[Response]]:
        """
        Edits the message based on the response passed as argument.

        Args:
            message_response (requests.Response or list): webhook.execute() response
            new_content_message: The new message content.

        Returns:
            response: Webhook response.
        """
        webhook = DiscordWebhook(url=self._urls, username=self._username, **kwargs)
        webhook.content = new_content_message
        return webhook.edit(message_response, **kwargs)

    def delete_message(self, message_response: Union[Response, List[Response]],
                       **kwargs) -> Union[Response, List[Response]]:
        """
        Deletes the message based on the response passed as argument.

        Args:
            message_response (requests.Response or list): webhook.execute() response

        Returns:
            response: Webhook response.
        """
        webhook = DiscordWebhook(url=self._urls, username=self._username, **kwargs)
        return webhook.delete(message_response)

    def send_file(self, files: List[str], **kwargs):
        """
        Upload file to the webhook.

        Args:
            files (list): The file paths.

        Returns:
            response: Webhook response.
        """
        webhook = DiscordWebhook(url=self._urls, username=self._username, **kwargs)
        for file in files:
            with open(file, "rb") as f:
                webhook.add_file(file=f.read(), filename=os.path.basename(file))
        return webhook.execute()
