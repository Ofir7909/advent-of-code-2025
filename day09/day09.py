from collections import deque
from dataclasses import dataclass
from enum import StrEnum
from itertools import chain, combinations, pairwise
import itertools
from pprint import pprint
from typing import Any, Self


def pprint_matrix(matrix: list[list[Any]]):
    print("\n".join([" ".join([str(cell) for cell in row]) for row in matrix]))


@dataclass
class Pos2i:
    x: int
    y: int

    @classmethod
    def from_str(cls, str: str) -> Self:
        chunks = str.split(",")
        assert len(chunks) == 2
        chunks = list(map(int, chunks))
        return cls(chunks[0], chunks[1])


def read_input(input=None):
    if not input:
        with open("day09/input.txt", "r") as f:
            input = f.read().strip()
    input = [Pos2i.from_str(l) for l in input.split("\n")]
    return input


def part1(red_tiles: list[Pos2i]):
    max_area = 0
    for t1, t2 in combinations(red_tiles, 2):
        w = abs(t1.x - t2.x) + 1
        h = abs(t1.y - t2.y) + 1
        area = w * h
        max_area = max(max_area, area)
    return max_area


class TileState(StrEnum):
    UNKNOWN = "?"
    EMPTY = "."
    RED = "#"
    GREEN = "x"


def flood_fill(
    matrix: list[list[TileState]], start_x: int, start_y: int, value: TileState
):
    queue = deque([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()
        if x not in range(0, len(matrix[0])) or y not in range(0, len(matrix)):
            continue
        if matrix[y][x] != TileState.UNKNOWN:
            continue
        matrix[y][x] = value
        queue.append((x - 1, y))
        queue.append((x + 1, y))
        queue.append((x, y - 1))
        queue.append((x, y + 1))


def part2(red_tiles: list[Pos2i]):
    valid_x = sorted(set([tile.x for tile in red_tiles] + [0, 100000]))
    valid_y = sorted(set([tile.y for tile in red_tiles] + [0, 100000]))

    m = len(valid_y)
    n = len(valid_x)

    matrix = [[TileState.UNKNOWN] * n for _ in range(m)]
    # fill red
    for tile in red_tiles:
        compacted_x = valid_x.index(tile.x)
        compacted_y = valid_y.index(tile.y)
        matrix[compacted_y][compacted_x] = TileState.RED

    # fill edges
    for t1, t2 in itertools.pairwise(red_tiles + [red_tiles[0]]):
        compacted_x1 = valid_x.index(t1.x)
        compacted_y1 = valid_y.index(t1.y)
        compacted_x2 = valid_x.index(t2.x)
        compacted_y2 = valid_y.index(t2.y)
        if compacted_x1 == compacted_x2:
            for y in itertools.chain(
                range(compacted_y1, compacted_y2 + 1),
                range(compacted_y2, compacted_y1 + 1),
            ):
                if matrix[y][compacted_x1] == TileState.UNKNOWN:
                    matrix[y][compacted_x1] = TileState.GREEN
        elif compacted_y1 == compacted_y2:
            for x in itertools.chain(
                range(compacted_x1, compacted_x2 + 1),
                range(compacted_x2, compacted_x1 + 1),
            ):
                if matrix[compacted_y1][x] == TileState.UNKNOWN:
                    matrix[compacted_y1][x] = TileState.GREEN
        else:
            print("Error! same tile")

    # flood fill empty
    flood_fill(matrix, 0, 0, TileState.EMPTY)

    candidate_rectangles = []
    for t1, t2 in combinations(red_tiles, 2):
        w = abs(t1.x - t2.x) + 1
        h = abs(t1.y - t2.y) + 1
        area = w * h
        candidate_rectangles.append((t1, t2, area))
    candidate_rectangles = reversed(
        sorted(candidate_rectangles, key=lambda rect: rect[2])
    )

    def is_rect_valid(t1: Pos2i, t2: Pos2i):
        compacted_x1 = valid_x.index(t1.x)
        compacted_y1 = valid_y.index(t1.y)
        compacted_x2 = valid_x.index(t2.x)
        compacted_y2 = valid_y.index(t2.y)
        if compacted_x1 > compacted_x2:
            compacted_x1, compacted_x2 = compacted_x2, compacted_x1
        if compacted_y1 > compacted_y2:
            compacted_y1, compacted_y2 = compacted_y2, compacted_y1
        for y in range(compacted_y1, compacted_y2 + 1):
            for x in range(compacted_x1, compacted_x2 + 1):
                if matrix[y][x] == TileState.EMPTY:
                    return False
        return True

    pprint_matrix(matrix)

    # find biggest valid one
    for t1, t2, area in candidate_rectangles:
        if is_rect_valid(t1, t2):
            return area


def main():
    test_input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
