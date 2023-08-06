import datetime
import enum
from dataclasses import asdict, dataclass, field
from typing import List, Optional, Union


class Color(enum.Enum):
    """
    The color type.
    Attributes:
        RED (str): The red color.
        GRAY (str): The gray color.
        BLUE (str): The blue color.
        GREEN (str): The green color.
        WHITE (str): The white color.
        BLACK (str): The black color.
        BROWN (str): The brown color.
        YELLOW (str): The yellow color.
        PURPLE (str): The purple color.
        ORANGE (str): The orange color.
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

    def __str__(self):
        """
        Returns a string as a representation of the object.
        """
        return str(self.value)

    def __repr__(self):
        """
        Returns a string as a representation of the object.
        """
        return str(self.value)


@dataclass
class Author:
    """
    Author info.

    Attributes:
        author_name: The author name.
        author_icon: A valid URL that displays a small 16px by 16px image to the left of the author_name.
        author_link: A valid URL that will hyperlink the author_name text.
    """
    author_name: str = None
    author_icon: str = None
    author_link: str = None


@dataclass
class Footer:
    """
    Footer in message.

    Attributes:
        footer: A brief text that will be displayed footer.
        footer_icon: A valid URL to an image file that will be displayed beside the footer text.
    """
    footer: str = None
    footer_icon: str = None


@dataclass
class Field:
    """
    Fields are an array of field objects that get displayed in a table-like way

    Attributes:
        title: Title as bold heading displayed in the field object.
        value: The text value displayed in the field object.
        short: Indicates whether the field object is short enough to be displayed side-by-side
               with other field objects. Defaults to false.
    """
    title: str
    value: str
    short: bool = False


@dataclass
class Message:
    """
    The message with attachment.

    Attributes:
        text: The main text of the message content.
        title: Title text near the top of the message.
        pretext: Text that appears above the message block.
        thumb_url: A valid URL to an image file that will be displayed as a thumbnail on the right side
                   of a message attachment.
        author: [Author][botcity.plugins.slack.models.Author] information.
        footer: [Footer][botcity.plugins.slack.models.Footer] texts.
        ts: The timestamp value as part of the message footer.
        fields: List of [Field][botcity.plugins.slack.models.Field] information.
        fallback: A plain text summary of the attachment used in clients that don't show formatted text.
        color: Changes the color of the border on the left side of this message, the default color is gray.
        image_url: A valid URL to an image file that will be displayed at the bottom of the message.
                   We support GIF, JPEG, PNG, and BMP formats.
        title_link: A valid URL that turns the title text into a hyperlink.
        markdown_in: An array of field names that should be formatted by mrkdwn syntax.
    """
    text: str = ""
    title: str = None
    pretext: str = None
    thumb_url: str = None
    author: Author = field(default_factory=Author)
    footer: Footer = field(default_factory=Footer)
    ts: Optional[int] = datetime.datetime.now().timestamp()
    fields: List[Field] = None
    fallback: Optional[str] = None
    color: Union[Color, str] = None
    image_url: Optional[str] = None
    title_link: Optional[str] = None
    markdown_in: Optional[List[str]] = None

    def asdict(self):
        if self.fields:
            fields = [asdict(field) for field in self.fields]
        else:
            fields = None
        if isinstance(self.color, Color):
            color = self.color.value
        else:
            color = self.color
        return {
            'text': self.text,
            'fallback': self.fallback,
            'fields': fields,
            'color': color,
            'markdown_in': self.markdown_in,
            'title': self.title,
            'title_link': self.title_link,
            'pretext': self.pretext,
            'author_name': self.author.author_name,
            'author_link': self.author.author_link,
            'author_icon': self.author.author_icon,
            'image_url': self.image_url,
            'thumb_url': self.thumb_url,
            'footer': self.footer.footer,
            'footer_icon': self.footer.footer_icon,
            'ts': self.ts
        }
