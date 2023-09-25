from aider.coders import AutocompleteSystem

def test_input_method():
    sentences = ["i love you", "island", "ironman", "i love leetcode"]
    times = [5, 3, 2, 2]
    acs = AutocompleteSystem(sentences, times)

    assert acs.input("i") == ["i love you", "island", "i love leetcode"]
    assert acs.input("a") == []
    assert acs.input("#") == []

def test_input_method_empty_string():
    sentences = ["i love you", "island", "ironman", "i love leetcode"]
    times = [5, 3, 2, 2]
    acs = AutocompleteSystem(sentences, times)

    assert acs.input("") == []
    
def test_input_method_multiple_characters():
    sentences = ["i love you", "island", "ironman", "i love leetcode", "i love modern software engineering", "i love macheight"]
    times = [5, 3, 20, 2, 4, 9]
    acs = AutocompleteSystem(sentences, times)

    assert acs.input("i") == ["ironman", "i love macheight", "i love you"]
    assert acs.input("i love") == ["i love macheight", "i love you", "i love modern software engineering"]
    assert acs.input("i love m") == ["i love macheight", "i love modern software engineering"]



def test_edge_cases():
    # Empty initial sentences
    acs = AutocompleteSystem([], [])
    assert acs.input("i") == []
    assert acs.input("#") == []

    # Single sentence in the initial list
    acs = AutocompleteSystem(["a"], [1])
    assert acs.input("a") == ["a"]
    assert acs.input("#") == []


