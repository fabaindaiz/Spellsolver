from src.entities import Coordinates

CHARS = set("abcdefghijklmnopqrstuvwxyz")

POINTS = {
    "a": 1,
    "b": 4,
    "c": 5,
    "d": 3,
    "e": 1,
    "f": 5,
    "g": 3,
    "h": 4,
    "i": 1,
    "j": 7,
    "k": 6,
    "l": 3,
    "m": 4,
    "n": 2,
    "o": 1,
    "p": 4,
    "q": 8,
    "r": 2,
    "s": 2,
    "t": 2,
    "u": 4,
    "v": 5,
    "w": 5,
    "x": 7,
    "y": 4,
    "z": 8,
}


def aux_to_indices(coordinate: int) -> Coordinates:
    """
    Converts an auxiliary coordinate to a tuple of row and column indices.

    Args:
        coordinate (int): The auxiliary coordinate to convert.

    Returns:
        Coordinates: A coordinate object containing the row and column indices.
    """
    coordinate = coordinate % 25

    return Coordinates(coordinate % 5, coordinate // 5)


def is_valid_word(word: str) -> bool:
    """
    Checks if a given word consists of valid characters.

    Args:
        word (str): The word to validate.

    Returns:
        bool: True if the word only contains valid characters, False otherwise.
    """
    return all(letter in CHARS for letter in word)


def get_letter_point_value(letter: str) -> int:
    """
    Retrieves the point value of a letter.

    Args:
        letter (str): The letter for which to determine the point value.

    Returns:
        int: The point value of the letter. Returns 0 if the letter is not in the POINTS dictionary.
    """
    return POINTS.get(letter, 0)
