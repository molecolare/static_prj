from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        remaining_text = text
        for alt_text, url in images:
            # Trova la posizione dell'immagine nel testo
            start_index = remaining_text.find(f"![{alt_text}]({url})")
            if start_index == -1:
                raise ValueError("Impossibile trovare l'immagine nel testo.")

            # Aggiungi il testo prima dell'immagine
            before_image = remaining_text[:start_index]
            if before_image:
                new_nodes.append(TextNode(before_image, TextType.TEXT))

            # Aggiungi il nodo immagine
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            # Aggiorna il testo rimanente
            remaining_text = remaining_text[start_index + len(f"![{alt_text}]({url})"):]

        # Aggiungi il testo rimanente dopo l'ultima immagine
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        remaining_text = text
        for anchor_text, url in links:
            # Trova la posizione del link nel testo
            start_index = remaining_text.find(f"[{anchor_text}]({url})")
            if start_index == -1:
                raise ValueError("Impossibile trovare il link nel testo.")

            # Aggiungi il testo prima del link
            before_link = remaining_text[:start_index]
            if before_link:
                new_nodes.append(TextNode(before_link, TextType.TEXT))

            # Aggiungi il nodo link
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))

            # Aggiorna il testo rimanente
            remaining_text = remaining_text[start_index + len(f"[{anchor_text}]({url})"):]

        # Aggiungi il testo rimanente dopo l'ultimo link
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text

        parts = text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: no matching closing delimiter for '{delimiter}'.")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
