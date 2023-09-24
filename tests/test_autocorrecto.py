from aider.autocorrector import get_k_similar_words

def test_get_k_similar_words():
    dictionary = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    assert get_k_similar_words(dictionary, 'aple', 3) == ['apple', 'date', 'grape']
    assert get_k_similar_words(dictionary, 'bananna', 2) == ['banana']
    assert get_k_similar_words(dictionary, 'elderbery', 1) == ['elderberry']

def test_get_k_similar_words_empty():
    dictionary = []
    assert get_k_similar_words(dictionary, 'aple', 3) == []
    assert get_k_similar_words(dictionary, 'bananna', 2) == []
    assert get_k_similar_words(dictionary, 'elderbery', 1) == []

def test_get_most_similar_words_short():
    dictionary = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    threshold = 2
    assert get_k_similar_words(dictionary, 'a', 1, threshold) == []
    assert get_k_similar_words(dictionary, 'b', 1, threshold) == []
    assert get_k_similar_words(dictionary, 'e', 1, threshold) == []

def test_long_words():
    dictionary = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'floccinaucinihilipilification']
    assert get_k_similar_words(dictionary, 'pneumonoultramicroscopicsilicovolcanoconiosis', 1) == ['pneumonoultramicroscopicsilicovolcanoconiosis']
    assert get_k_similar_words(dictionary, 'floccinaucinihilipilification', 1) == ['floccinaucinihilipilification']