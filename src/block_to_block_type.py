from blocktype import BlockType

def block_to_block_type(block):
    """
    Determina il tipo di blocco Markdown.

    Args:
        block (str): Un blocco di testo Markdown.

    Returns:
        BlockType: Il tipo di blocco.
    """
    lines = block.split("\n")

    # Controlla se è un heading
    if block.startswith("#"):
        heading_level = 0
        for char in block:
            if char == "#":
                heading_level += 1
            else:
                break
        if heading_level <= 6 and (len(block) > heading_level and block[heading_level] == " "):
            return BlockType.HEADING

    # Controlla se è un blocco di codice
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    # Controlla se è un blocco di citazione
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Controlla se è un elenco non ordinato
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Controlla se è un elenco ordinato
    if all(line.split(". ", 1)[0].isdigit() and int(line.split(". ", 1)[0]) == lines.index(line) + 1 for line in lines):
        return BlockType.ORDERED_LIST

    # Se non è nessuno dei precedenti, è un paragrafo
    return BlockType.PARAGRAPH
