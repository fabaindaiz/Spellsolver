import os
from collections.abc import Generator
from typing import TextIO

from src import SOURCES, WORDLIST
from src.utils import resource_path
from .generate import WordGenerate


class WordList:
    """
    Represents a class that can generate and load a wordlist file for Spellsolver.

    Attributes:
        source_path (str): The path to the folder containing source files.
        dest_path (str): The path to the destination wordlist file.
    """

    def __init__(self):
        """
        Initialize a WordList object with source and destination paths.
        """
        self.source = resource_path(SOURCES)
        self.destination = resource_path(WORDLIST)

    def open_file(self) -> TextIO:
        """
        Load a wordlist file, generate it if it doesn't exist.

        Returns:
            TextIO: A file object representing the opened wordlist file.
        """
        if not os.path.exists(self.destination):
            WordGenerate.generate_wordlist(
                source=self.source, destination=self.destination
            )
        return open(self.destination, "r")

    def get_words(self) -> Generator[str, None, None]:
        """
        Get the next word from the wordlist file.

        Returns:
            Generator[str, None, None]: A generator that yields the next word.
        """
        file = self.open_file()
        for line in file:
            yield line.strip().lower()
        file.close()
