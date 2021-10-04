"""
contains function for computing the tfidf scores.
"""

from typing import Optional, List

def tfidf(texts: list, df: Optional[dict]=None) -> List[dict]:
    """
    takes in a list of tokenized texts and returns a list of dictionaries

    args:
        df (dict): Document frequencies, defaults to None, in which case it is estimated from the texts.
    """
    pass