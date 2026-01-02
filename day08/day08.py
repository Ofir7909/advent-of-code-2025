from dataclasses import dataclass
from typing import Counter, Self


@dataclass
class Pos3i:
    x: int
    y: int
    z: int

    def distance_to_squared(self, other: Self) -> float:
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    @classmethod
    def from_str(cls, str: str) -> Self:
        chunks = str.split(",")
        assert len(chunks) == 3
        chunks = list(map(int, chunks))
        return cls(chunks[0], chunks[1], chunks[2])


def read_input(input=None):
    if not input:
        with open("day08/input.txt", "r") as f:
            input = f.read().strip()
    input = [Pos3i.from_str(l) for l in input.split("\n")]
    return input


def part1(boxes: list[Pos3i]):
    CONNECTIONS_NUM = 1000
    potential_connections = []
    for i, b1 in enumerate(boxes):
        for j, b2 in enumerate(boxes[i + 1 :], start=i + 1):
            dist = b1.distance_to_squared(b2)
            potential_connections.append((dist, i, j))
    potential_connections.sort()

    groups = [i for i in range(len(boxes))]

    connections_made = 0
    for dist, i, j in potential_connections:
        if connections_made == CONNECTIONS_NUM:
            break

        connections_made += 1

        g1 = groups[i]
        g2 = groups[j]
        if g1 == g2:
            continue

        min_group = min(g1, g2)
        max_group = max(g1, g2)
        groups = [min_group if g == max_group else g for g in groups]

    group_counter = Counter(groups)
    prod = 1
    for group, count in group_counter.most_common(3):
        prod *= count
    return prod


def part2(boxes: list[Pos3i]):
    potential_connections = []
    for i, b1 in enumerate(boxes):
        for j, b2 in enumerate(boxes[i + 1 :], start=i + 1):
            dist = b1.distance_to_squared(b2)
            potential_connections.append((dist, i, j))
    potential_connections.sort()

    groups = [i for i in range(len(boxes))]

    for dist, i, j in potential_connections:
        g1 = groups[i]
        g2 = groups[j]
        if g1 == g2:
            continue

        min_group = min(g1, g2)
        max_group = max(g1, g2)
        groups = [min_group if g == max_group else g for g in groups]

        if all(g == 0 for g in groups):
            return boxes[i].x * boxes[j].x


def main():
    test_input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
