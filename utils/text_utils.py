def clean_text(text: str) -> str:
    """ Removes non-ASCII characters (e.g., icon fonts) from text """
    return ''.join(c for c in text if c.isascii()).strip()