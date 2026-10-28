"""To convert a phrase in its acronym."""

import re

def abbreviate(phrase):
    """In order to generate an acronym of a long name."""
    words = re.split(r"[\s_-]+", phrase)

    acronym = ""

    for word in words:
        match = re.search(r"[A-Za-z]", word)
        if match:
            acronym += match.group().upper()

    return acronym