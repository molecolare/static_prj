def markdown_to_blocks(markdown):
    """
    Converte un testo Markdown in una lista di blocchi (block strings).

    Args:
        markdown (str): Il testo Markdown da suddividere in blocchi.

    Returns:
        list[str]: Una lista di blocchi Markdown.
    """
    # Divide il testo in blocchi usando \n\n come delimitatore
    blocks = markdown.split("\n\n")

    # Rimuove gli spazi vuoti iniziali e finali da ogni blocco
    blocks = [block.strip() for block in blocks]

    # Filtra i blocchi vuoti (dovuti a newline multipli)
    blocks = [block for block in blocks if block]

    return blocks
