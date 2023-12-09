from itertools import pairwise
from types import NoneType


def process_diffs(diff_levels: list[list[int]]):
    while len([x for x in diff_levels[-1] if x != 0]) != 0:  # Final "level" is not all 0
        new_level: list[int] = []
        for i, j in pairwise(diff_levels[-1]):
            new_level.append(j-i)
        diff_levels.append(new_level)
        process_diffs(diff_levels)


def generate_next(diff_levels: list[list[int]], level: int) -> int:
    if level == len(diff_levels) -1:
        return 0
    return diff_levels[level][-1] + generate_next(diff_levels, level + 1)


def part01():
    with open("day09/input.txt", "r") as file:
        f = file.read()
    result = 0
    for line in f.split("\n"):
        line = [int(x) for x in line.split()]
        difference_levels: list[list[int]] = [line]
        process_diffs(difference_levels)
        #print(difference_levels)
        result += generate_next(difference_levels, 0)
    print(result)


def generate_prev(diff_levels: list[list[int]], level: int) -> int:
    if level == len(diff_levels) -1:
        return 0
    return diff_levels[level][0] - generate_prev(diff_levels, level + 1)


def part02() -> NoneType:
    with open("day09/input.txt", "r") as file:
        f = file.read()
    result = 0
    for line in f.split("\n"):
        line = [int(x) for x in line.split()]
        difference_levels: list[list[int]] = [line]
        process_diffs(difference_levels)
        #print(difference_levels)
        result += generate_prev(difference_levels, 0)
    print(result)


if __name__ == "__main__":
    part01()
    part02()