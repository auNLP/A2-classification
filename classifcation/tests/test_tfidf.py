from ..tfidf import tfidf


def test_tfidf():

    tokenized_text = ["This", "is", "a", "text"]
    texts = [tokenized_text, tokenized_text]
    outcomes = tfidf(texts)

    # outcome should be a list of dictionaries
    isinstance(outcomes, list)
    outcome = outcomes[0]
    isinstance(outcome, dict)

    # where keys is strings (tokens) and values is the tf-idf score
    for keys, values in outcome.items():
        assert isinstance(keys, str)
        assert isinstance(values, float)