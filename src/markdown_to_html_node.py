from blocktype import BlockType
from textnode import text_node_to_html_node
from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_text_nodes import text_to_textnodes
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    """
    Converte un documento Markdown in un singolo nodo HTML genitore (div) con nodi figli.

    Args:
        markdown (str): Il testo Markdown da convertire.

    Returns:
        ParentNode: Un nodo HTML genitore (div) con nodi figli.
    """
    # Divide il markdown in blocchi
    blocks = markdown_to_blocks(markdown)

    # Crea il nodo genitore div
    root_node = ParentNode("div", [])

    # Itera su ogni blocco e crea il corrispondente nodo HTML
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block_type, block)
        root_node.children.append(block_node)

    return root_node

def block_to_html_node(block_type, block):
    """
    Converte un blocco Markdown nel corrispondente nodo HTML.

    Args:
        block_type (BlockType): Il tipo di blocco Markdown.
        block (str): Il contenuto del blocco Markdown.

    Returns:
        HTMLNode: Il nodo HTML corrispondente.
    """
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    else:
        return paragraph_to_html_node(block)

def paragraph_to_html_node(block):
    """
    Converte un paragrafo Markdown in un nodo HTML <p>.

    Args:
        block (str): Il contenuto del paragrafo Markdown.

    Returns:
        ParentNode: Un nodo HTML <p> con nodi figli.
    """
    newblock = block.replace("\n", " ")
    children = text_to_children(newblock)
    return ParentNode("p", children)

def heading_to_html_node(block):
    """
    Converte un heading Markdown in un nodo HTML <h1>-<h6>.

    Args:
        block (str): Il contenuto dell'heading Markdown.

    Returns:
        ParentNode: Un nodo HTML <h1>-<h6> con nodi figli.
    """
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    text = block[level + 1:]  # Rimuove il # e lo spazio dopo
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    """
    Converte un blocco di codice Markdown in un nodo HTML <pre><code>.

    Args:
        block (str): Il contenuto del blocco di codice Markdown.

    Returns:
        ParentNode: Un nodo HTML <pre><code> con un nodo figlio LeafNode.
    """
    # Rimuove i backtick e il newline iniziale/finale
    code_text = block.strip("```").strip()
    code_node = LeafNode("code", code_text)
    return ParentNode("pre", [code_node])

def quote_to_html_node(block):
    """
    Converte un blocco di citazione Markdown in un nodo HTML <blockquote>.

    Args:
        block (str): Il contenuto del blocco di citazione Markdown.

    Returns:
        ParentNode: Un nodo HTML <blockquote> con nodi figli.
    """
    lines = block.split("\n")
    # Rimuove il > e lo spazio dopo
    quote_lines = [line[1:].strip() if line.startswith("> ") else line[1:].strip() for line in lines]
    quote_text = "\n".join(quote_lines)
    children = text_to_children(quote_text)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    """
    Converte un elenco non ordinato Markdown in un nodo HTML <ul>.

    Args:
        block (str): Il contenuto dell'elenco non ordinato Markdown.

    Returns:
        ParentNode: Un nodo HTML <ul> con nodi figli <li>.
    """
    items = block.split("\n")
    list_items = []
    for item in items:
        # Rimuove il - e lo spazio dopo
        text = item[2:].strip()
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)

def ordered_list_to_html_node(block):
    """
    Converte un elenco ordinato Markdown in un nodo HTML <ol>.

    Args:
        block (str): Il contenuto dell'elenco ordinato Markdown.

    Returns:
        ParentNode: Un nodo HTML <ol> con nodi figli <li>.
    """
    items = block.split("\n")
    list_items = []
    for item in items:
        # Rimuove il numero, il . e lo spazio dopo
        text = item.split(". ", 1)[1].strip()
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)

def text_to_children(text):
    """
    Converte un testo Markdown in una lista di nodi HTML figli.

    Args:
        text (str): Il testo Markdown da convertire.

    Returns:
        list[HTMLNode]: Una lista di nodi HTML figli.
    """
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
