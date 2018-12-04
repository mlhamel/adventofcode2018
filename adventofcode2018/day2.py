from itertools import combinations

from typing import List


def make_checksum(values: List[str]) -> int:
    def has_pairs(value: str) -> bool:
        pairs = {x for x in combinations(value, 2)}

        number_full_pairs = len([pair for pair in pairs
                                 if all(p == pair[0] for p in pair)])
        return number_full_pairs != 0

    def has_thirds(value: str) -> bool:
        thirds = {x for x in combinations(value, 3)}

        number_full_thirds = len([third for third in thirds
                                  if all(p == third[0] for p in third)])
        return number_full_thirds != 0

    number_of_pairs = len([value for value in values if has_pairs(value)])
    number_of_thirds = len([value for value in values if has_thirds(value)])

    return number_of_pairs * number_of_thirds
