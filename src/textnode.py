from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
            text_type = text_node.text_type
            text = text_node.text
            url = text_node.url

            if text_type == TextType.TEXT:
                return LeafNode(None, text)
            elif text_type == TextType.BOLD:
                return LeafNode("b", text)
            elif text_type == TextType.ITALIC:
                return LeafNode("i", text)
            elif text_type == TextType.CODE:
                return LeafNode("code", text)
            elif text_type == TextType.LINK:
                if url is None:
                    raise ValueError("Link TextNode must have a URL.")
                return LeafNode("a", text, {"href": url})
            elif text_type == TextType.IMAGE:
                if url is None:
                    raise ValueError("Image TextNode must have a URL.")
                return LeafNode("img", "", {"src": url, "alt": text})
            else:
                raise ValueError(f"Unsupported TextType: {text_type}")
