import re

def extract_markdown_images(text):
    """
    Estrae tutte le immagini markdown da un testo e restituisce una lista di tuple (alt_text, url).
    Esempio:
        text = "![alt text](https://example.com/image.png)"
        restituisce: [("alt text", "https://example.com/image.png")]
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Estrae tutti i link markdown da un testo e restituisce una lista di tuple (anchor_text, url).
    Esempio:
        text = "[anchor text](https://example.com)"
        restituisce: [("anchor text", "https://example.com")]
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
