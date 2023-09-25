from .utils import Trie

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        Initializes an AutocompleteSystem object.

        :param sentences: A list of strings representing the sentences already typed. Each sentence has at most length 100 and consists of lowercase English letters and spaces.
        :type sentences: List[str]
        :param times: A list of integers representing the corresponding times that each sentence has been typed. The time is in the range [1, 1000].
        :type times: List[int]
        """
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.update_sentence(sentence, time)

        self.cur_trie_node = self.trie.root
        self.prefix = []

    def input(self, c):
        """
        Processes a new character from the user.

        :param c: A string representing the new character typed by the user.
        :type c: str
        :return: A list of up to 3 recommended sentences that have the prefix formed by the characters typed so far, sorted by decreasing order of frequency. If there are fewer than 3 recommended sentences, return all of them. If there are no recommended sentences, return an empty list.
        :rtype: List[str]
        """
        if c == '#':
            self.trie.update_sentence(self.prefix, 1)
            self.cur_trie_node = self.trie.root
            self.prefix = []
            return []
        else:
            self.prefix.append(c)
            if self.cur_trie_node is None or c not in self.cur_trie_node.children:
                self.cur_trie_node = None
                return []
            self.cur_trie_node = self.cur_trie_node.children[c]
            return self.trie.get_frequent_sentences(self.prefix, self.cur_trie_node)