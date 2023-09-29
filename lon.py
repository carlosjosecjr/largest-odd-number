from typing import Callable

def fn(z: list[int]) -> int:
    gt:   Callable[[int, int], bool] = lambda x, y: x >= y
    odd:  Callable[[int], bool]      = lambda x: not x % 2 == 0
    high: Callable[[int, int], bool] = lambda x, y: odd(x) and gt(x, y)

    max_odd: int = -1

    for number in z:
        if high(number, max_odd): max_odd = number

    return max_odd
