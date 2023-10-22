from src.modules.trie.base import Trie, TrieQuery
from src.modules.wordlist.wordlist import WordList
from src.config import SWAP, TRIE

if TRIE == "MARISA":
    from src.modules.trie.marisa import MarisaTrie
    trie = MarisaTrie()
else:
    raise NotImplementedError()


class WordValidate:
    """Validate a word using a trie"""

    def __init__(self) -> None:
        self.wordlist: WordList = WordList()
        self.trie: Trie = trie
    
    def init_trie(self) -> None:
        self.trie.insert_trie(self.wordlist)

    def get_trie(self) -> TrieQuery:
        return self.trie.query_trie()


if __name__ == "__main__":
    
    def node_str(node: Trie) -> str:
        """Return a string representation of a TrieNode"""
        return "\n".join(
            [f"{swap}: {node.get_leaf(recursive=True, key=swap)}" for swap in SWAP]
        )

    while True:
        word = input("Insert a word: ")
        node = validate.trie.get_node(word)
        print(node_str(node) if node else f"There are no word started in {word}")
