class TrieNode:
    """
    A node in a Trie data structure.

    Attributes:
    -----------
    children : dict
        A dictionary containing the children of the node.
    frequency : int
        The frequency of the node.
    end : bool
        A boolean indicating whether the node is the end of a word.
    """
    def __init__(self):
        self.children = {}
        self.frequency = 0
        self.end = False


class Trie:
    """
    A class representing a Trie data structure.

    Attributes:
    -----------
    root : TrieNode
        The root node of the Trie.

    Methods:
    --------
    update_sentence(sentence: str, frequency: int) -> None:
        Updates the Trie with the given sentence and its frequency.

    get_frequent_sentences(prefix: str, cur_node: TrieNode) -> List[str]:
        Returns a list of the three most frequent sentences that start with the given prefix.
    """
    def __init__(self):
        self.root = TrieNode()

    def update_sentence(self, sentence, frequency):
        """
        Updates the Trie with the given sentence and its frequency.

        Parameters:
        -----------
        sentence : str
            The sentence to be added to the Trie.
        frequency : int
            The frequency of the sentence.

        Returns:
        --------
        None
        """
        root = self.root
        for c in sentence:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]

        root.frequency += frequency
        root.end = True

    def get_frequent_sentences(self, prefix, cur_node):
        """
        Returns a list of the three most frequent sentences that start with the given prefix.

        Parameters:
        -----------
        prefix : str
            The prefix of the sentences to be searched.
        cur_node : TrieNode
            The current node of the Trie.

        Returns:
        --------
        List[str]
            A list of the three most frequent sentences that start with the given prefix.
        """
        def find_sentences(prefix, node):
            if node.end:
                sentences.append((-node.frequency, ''.join(prefix)))

            for c in node.children:
                prefix.append(c)
                find_sentences(prefix, node.children[c])
                prefix.pop()

        sentences = []
        find_sentences(prefix, cur_node)
        sentences.sort()

        return [s[1] for s in sentences[:3]]