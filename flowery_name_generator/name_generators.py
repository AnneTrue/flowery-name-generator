"""
Name generators
"""

import random

from . import training_data as td


def _r(word_set: set, capitalise: bool = True) -> str:
    chosen: str = random.choice(list(word_set))
    if capitalise:
        return chosen.capitalize()
    return chosen


def _join(first: str, second: str, space_ratio: int = 5) -> str:
    # Don't join empty strings
    if not first:
        return second
    if not second:
        return first
    joiners = [" "] * space_ratio + ["-"]  # Prefer spaces by default, tuned with the ratio
    return f"{first}{random.choice(joiners)}{second}"


def _simple_hyphen() -> str:
    return f"{_r(td.BIG_SET)}-{_r(td.BIG_SET)}"


def _hyphen_number() -> str:
    return f"{_r(td.BIG_SET)}-{_r(td.NUMBERS)}"

def _long_connected_name(min_len: int = 2, max_len: int = 6) -> str:
    remaining_length = random.randint(min_len, max_len)
    partial_name = ""
    while remaining_length > 0:
        num_to_pick = random.randint(1, min(3, remaining_length))
        for _ in range(num_to_pick):
            partial_name = _join(partial_name, _r(td.BIG_SET))
        remaining_length -= num_to_pick
        if remaining_length:
            partial_name = _join(partial_name, _r(td.JOINING_WORDS))
    return partial_name

def _long_name_with_descriptive(min_len: int = 2, max_len: int = 5) -> str:
    remaining_length = random.randint(min_len, max_len)
    hyphens_only: bool = random.randint(0, 3) == 0
    partial_name = _r(td.NAME_LIKES)
    while remaining_length > 0:
        num_to_pick = random.randint(1, min(3, remaining_length))
        for _ in range(num_to_pick):
            partial_name = _join(
                partial_name, _r(td.DESCRIPTORS | td.CURATED_WORDS), space_ratio=0 if hyphens_only else 9
            )
        remaining_length -= num_to_pick
        if remaining_length:
            partial_name = _join(
                partial_name, _r(td.JOINING_WORDS), space_ratio=0 if hyphens_only else 9
            )
    return partial_name
