from processor import Text
from collections import OrderedDict


def test_content():
    """
    GIVEN a Text object

    WHEN the initialization text is a valid URL; accessible via urllib
    THEN the content should be the text content on that website

    WHEN the initialization text is an invalid URL OR plain text; inaccessible via urllib
    THEN the content should be the same as the initialization text
    """
    valid_url = Text("http://example.com")
    invalid_url = Text("http://example.c")
    plain_text = Text("Tell the audience what you're going to say. Say it. Then tell them what you've said.")
    assert "example domain" in valid_url.content.casefold()
    assert invalid_url.content == "http://example.c"
    assert plain_text.content == "Tell the audience what you're going to say. Say it. Then tell them what you've said."


def test_word_count():
    """
    GIVEN a Text object

    WHEN the initialization text is a valid URL; accessible via urllib
    THEN the word_count should return a dictionary with a word:count mapping, with an accurate count value, from the text content in the web page at the given URL

    WHEN the initialization text is an invalid URL OR plain text; inaccessible via urllib
    THEN the word_count should return a dictionary with a word:count mapping of the initialization text, with an accurate count value
    """
    valid_url = Text("http://example.com")
    invalid_url = Text("http://example.c")
    plain_text = Text("Tell the audience what you're going to say. Say it. Then tell them what you've said.")
    assert type(valid_url.words_by_count) == dict
    assert type(invalid_url.words_by_count) == dict
    assert type(plain_text.words_by_count) == dict

    assert valid_url.words_by_count['example'] == 2
    assert invalid_url.words_by_count['http://example.c'] == 1
    assert plain_text.words_by_count['tell'] == 2


def test_sorted_wbc_by_count():
    plain_text = Text("Tell the audience what you're going to say. Say it. Then tell them what you've said.")
    assert plain_text.sorted_wbc_by_count() == OrderedDict([('the', 1), ('audience', 1), ("you're", 1), ('going', 1), ('to', 1), ('it', 1), ('then', 1), ('them', 1), ("you've", 1), ('said', 1), ('tell', 2), ('what', 2), ('say', 2)])


def test_sorted_wbc_alphabetically():
    plain_text = Text("Tell the audience what you're going to say. Say it. Then tell them what you've said.")
    assert plain_text.sorted_wbc_by_count() == OrderedDict([('the', 1), ('audience', 1), ("you're", 1), ('going', 1), ('to', 1), ('it', 1), ('then', 1), ('them', 1), ("you've", 1), ('said', 1), ('tell', 2), ('what', 2), ('say', 2)])


