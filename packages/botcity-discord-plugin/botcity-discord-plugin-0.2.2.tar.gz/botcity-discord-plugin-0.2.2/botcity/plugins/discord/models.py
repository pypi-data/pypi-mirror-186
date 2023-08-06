import enum
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Union


@dataclass
class Author:
    """
    Author info.

    Attributes:
        url: Profile url.
        name: Author name.
        icon_url: URL to author profile picture.
    """
    url: str
    name: str
    icon_url: str


@dataclass
class Footer:
    """
    Footer info.

    Attributes:
        text: Footer text.
        icon_url: URL to footer icon.
    """
    text: str
    icon_url: str


@dataclass
class Field:
    """
    Field info.

    Attributes:
        name: Name of field.
        value: Value of field.
        inline: True if the embed fields are placed side by side, False the field are placed in new line.
    """
    name: str
    value: str
    inline: bool = False


class Color(enum.Enum):
    """
    The color type.
    Attributes:
        RED (str): The red color in hexadecimal.
        GRAY (str): The gray color in hexadecimal.
        BLUE (str): The blue color in hexadecimal.
        GREEN (str): The green color in hexadecimal.
        WHITE (str): The white color in hexadecimal.
        BLACK (str): The black color in hexadecimal.
        BROWN (str): The brown color in hexadecimal.
        YELLOW (str): The yellow color in hexadecimal.
        PURPLE (str): The purple color in hexadecimal.
        ORANGE (str): The orange color in hexadecimal.
    """
    RED = 'FF0000'
    GRAY = '808080'
    BLUE = '0000FF'
    GREEN = '008000'
    WHITE = 'FFFFFF'
    BLACK = '000000'
    BROWN = '964B00'
    YELLOW = 'FFFF00'
    PURPLE = '800080'
    ORANGE = 'FFA500'


@dataclass
class EmbeddedMessage:
    """
    The embedded message.

    Attributes:
        title: Title of embed.
        description: Description body of embed.
        color: Color code of the embed as hexadecimal string or
            [Color][botcity.plugins.discord.models.Color] enum.
        image: Your image url here.
        author: [Author][botcity.plugins.discord.models.Author] information.
        footer: [Footer][botcity.plugins.discord.models.Footer] texts.
        thumbnail: Your thumbnail url here.
        fields: List of [Field][botcity.plugins.discord.models.Field] information.
        timestamp: Timestamp of embed content.
        files: Send files in embedded message.
    """
    title: str
    description: str
    color: Union[str, Color]
    image: str = None
    author: Author = None
    footer: Footer = None
    thumbnail: str = None
    fields: List[Field] = None
    timestamp: float = datetime.now().timestamp()
    files: Union[List[str], Dict[str, bytes]] = None
