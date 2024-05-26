import inspect
import os
import re
import traceback

import inflect


class AsyncHelperBase:
    """
    Base class to support async constructor `__init__()`.
    Used by all helpers to call async methods in their constructors.
    """

    async def __new__(cls, *args, **kwargs):
        coroutine_obj = super().__new__(cls)
        await coroutine_obj.__init__(*args, **kwargs)  # type: ignore
        return coroutine_obj

    async def __init__(self, *args, **kwargs):
        pass


class Singleton(type):
    """The Metaclass used to apply Singleton Pattern to a class.

    Usage:
    ------
    >>> class Server(metaclass=Singleton):
        ...
    """

    _instances: dict = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwargs)
        return self._instances[self]


def find_word_indices(string: str, words: list[str], case_sensitive: bool = False) -> list[int]:
    """Find the indices of the words in the string.

    Args:
    -----
    string : str
        The string to search.
    words : list[str]
        The words to search for.
    case_sensitive : bool, optional
        Whether the search is case sensitive, by default False.

    Returns
    -------
    list[int]
        The indices of the words in the string.

    Examples
    --------
    >>> find_word_indices("This is a test", ["test"])
    [4]
    >>> find_word_indices("This is a test", ["test"], case_sensitive=True)
    []
    >>> find_word_indices("This is a test", ["test", "this"])
    [4, 0]
    >>> find_word_indices("This is a test", ["test", "this"], case_sensitive=True)
    [4, 0]
    >>> find_word_indices("This is a test", ["test", "this", "is"])
    [4, 0, 2]"""
    string = string.lower()

    indices: list[int] = []
    string_words = string.split()
    for word in words:
        if not case_sensitive:
            word = word.lower()
        indices.extend(index for index, string_word in enumerate(string_words) if word in string_word and len(word) > len(string_word) - 2)
    return indices


def check_environment_variables(variable_names: list[str]) -> tuple[bool, list[bool]]:
    """Check if all variables is in the environment.

    Args:
    -----
        `variable_names (list[str])`: list of variables to check

    Returns:
    --------
        `tuple[bool, list[bool]]`:
        - `bool`: all variables are in the environment
        - `list[bool]`: indicates whether each variable is in the environment or not
    """
    results = [variable in os.environ for variable in variable_names]
    return all(results), results


def add_environment_variables(variables: dict[str, str]) -> None:
    """Add a list of environment variables from a dictionary

    Args:
    -----
        `env_parameters (dict[str, str])`: the dictionary of environment variables
    """
    for key, value in variables.items():
        os.environ[key] = str(value)


def is_float(text: str) -> bool:
    """Return where a `string` can be converted to a float"""
    try:
        float(text)
        return True
    except ValueError:
        return False


def remove_punctuations(sentence: str) -> str:
    """Remove punctuations in a sentence: !"#$%&()*+,-./:;<=>?@[]^_{|}~\n
    Doesn't not remove the single quote because it can be the contraction symbol."""
    translator = str.maketrans('', '', r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~""")
    return sentence.translate(translator)


def is_capitalized(input_string: str) -> bool:
    """Return whether the `input_string` is capitilized (ex: "John", "Melbourne",...) or not"""
    if not input_string:
        return False
    if len(input_string) == 1:
        return input_string.isupper()
    return all((word[0].isupper() and (word[1:].islower() if len(word) > 1 else True)) for word in input_string)


def replace_numbers_with_words(input_string: str) -> str:
    """Convert any numbers in the `input_string` into the words equivalent.

    Examples:
    ---------
    >>> print(replace_numbers_with_words('I have 10 apples and 20 oranges.'))
    # Output: 'I have ten apples and twenty oranges.'
    """
    p = inflect.engine()
    numbers = re.findall(r'\b\d+\b', input_string)
    for number in numbers:
        word = str(p.number_to_words(number))
        input_string = re.sub(r'\b' + number + r'\b', word, input_string)
    return input_string


def remove_words(sentence: str, words_to_remove: list[str]) -> str:
    """Remove all specific words in the given sentence

    Args:
        sentence (str): The sentence to be removed
        words_to_remove (list[str]): The list of words to be removed (each element can be a single word or a multiply words)
    """
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    cleaned_sentence = re.sub(pattern, '', sentence, flags=re.IGNORECASE)
    cleaned_sentence = re.sub(r'\s+', ' ', cleaned_sentence).strip()
    return cleaned_sentence


def count_words_in_sentence(sentence: str, words: list[str]):
    """Count the total appearing of a list of words in a sentence.

    Args:
        sentence (str): The sentence to be counted in.
        words (list[str]): The list of words to be counted.
    """
    word_set = set(words)
    sentence_words = sentence.split()
    return sum(1 for word in sentence_words if word in word_set)


def _unhyphenate(match: re.Match):
    return match.group(1) + match.group(2)


def replace_hyphenated_words(sentence: str):
    """Replace hyphenated words in a sentence with their unhyphenated version."""
    hyphenated_word_pattern = r'\b(\w+)-(\w+)\b'
    return re.sub(hyphenated_word_pattern, _unhyphenate, sentence)


def get_traceback_str() -> str:
    """Get the traceback when an exception is given into the logger"""
    return traceback.format_exc()


def get_current_function_name():
    stack = inspect.stack()
    return stack[2].function
