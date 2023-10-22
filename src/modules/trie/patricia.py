from typing import Any, Dict, Generator, List, Tuple
from src.modules.trie.base import Trie, TrieQuery
from src.modules.wordlist.wordlist import WordList
from src.modules.trie.loader import word_iter


class PatriciaNode:
    """Represents a node of a Patricia trie"""

    def __init__(self) -> None:
        self.childs: Dict[str, PatriciaNode] = {}
        self.words: List[str] = []

    def insert(self, iter_word: str, word: str) -> None:
        """Insert a word recursively in the trie"""
        if not iter_word:
            return self.words.append(word)

        common_prefix = next((prefix for prefix in self.childs.keys() if iter_word.startswith(prefix)), None)
        if common_prefix:
            next_word = iter_word[len(common_prefix):]
            child = self.childs[common_prefix]
        else:
            common_prefix = iter_word[0]
            next_word = iter_word[1:]
            child = self.childs.setdefault(common_prefix, PatriciaNode())

        child.insert(next_word, word)

    def get_key(self, letter: str) -> "PatriciaNode":
        return next((key for key in self.childs if key.startswith(letter)), None)

    def get_node(self, word: str) -> "PatriciaNode":
        """Get node representing a word in the trie"""
        node = self
        while word:
            prefix = next((p for p in node.childs.keys() if word.startswith(p)), None)
            if not prefix:
                return None
            node = node.childs[prefix]
            word = word[len(prefix):]
        return node

    def get_leaf(self, recursive=False) -> Any:
        """Get content from trie leaf using kwargs"""
        words = self.words
        if recursive:
            for node in self.childs.values():
                words += node.get_leaf(recursive=True)
        return words
    
    def merge_tries(self, trie: "PatriciaNode") -> None:
        """Merge other_trie into main_trie"""
        self.words += trie.words

        for prefix, child in trie.childs.items():
            if prefix in self.childs:
                self.childs[prefix].merge_tries(child)
            else:
                self.childs[prefix] = child


class PatriciaTrie(Trie):

    def __init__(self) -> None:
        self.node: PatriciaNode = PatriciaNode()

    def insert_trie(self, loader: WordList) -> None:
        for word in loader.get_words():
            for iword in word_iter(word):
                self.node.insert(iword, word)
    
    def query_trie(self) -> "TrieQuery":
        return PatriciaTrieQuery(self)
    

class PatriciaTrieQuery(TrieQuery):

    def __init__(self, trie: Trie) -> None:
        self.trie: PatriciaTrie = trie
    
    def get_root(self) -> PatriciaNode:
        return self.trie.node

    def get_key(self, node: PatriciaNode, letter: str) -> Tuple[Any, str]:
        child_key = node.get_key(letter)
        return node.childs[child_key] if child_key else None, child_key

    def get_leaf(self, node: PatriciaNode) -> Generator[str, None, None]:
        yield from node.get_leaf()
