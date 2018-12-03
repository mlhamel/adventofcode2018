from typing import List


def apply_freqs(current: int, changes: List[int]) -> int:
    return current + sum(changes)
