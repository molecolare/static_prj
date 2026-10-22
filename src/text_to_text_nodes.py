from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    """
    Converte un testo in formato Markdown in una lista di TextNode.

    Args:
        text (str): Il testo in formato Markdown.

    Returns:
        list[TextNode]: Una lista di TextNode rappresentanti il testo.
    """
    nodes = [TextNode(text, TextType.TEXT)]

    # Split bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # Split italic (_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Split code (`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Split images (![alt](url))
    nodes = split_nodes_image(nodes)

    # Split links ([anchor](url))
    nodes = split_nodes_link(nodes)

    return nodes
