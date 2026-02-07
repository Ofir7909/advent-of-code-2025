from dataclasses import dataclass
import itertools
from turtle import shape


type Shape = list[list[bool]]


def count_cells_in_shape(shape: Shape) -> int:
    return sum(1 for cell in itertools.chain.from_iterable(shape) if cell)


def flip_h(shape: Shape) -> Shape:
    return list(reversed(shape))


def rotate(shape: Shape, n: int) -> Shape:
    if n == 0:
        return shape

    new_shape = [
        [shape[2][0], shape[1][0], shape[0][0]],
        [shape[2][1], shape[1][1], shape[0][1]],
        [shape[2][2], shape[1][2], shape[0][2]],
    ]

    return rotate(new_shape, n - 1)


def shape_to_str(shape: Shape) -> str:
    mapping = {True: "#", False: "."}
    return "\n".join("".join(map(mapping.get, row)) for row in shape)


@dataclass
class Tree:
    width: int
    height: int
    presents: list[int]


def line_to_bools(line: str):
    return [c == "#" for c in line]


def read_input(input=None):
    if not input:
        with open("day12/input.txt", "r") as f:
            input = f.read().strip()

    shapes: list[Shape] = []
    trees: list[Tree] = []
    input_iter = iter(input.splitlines())
    for line in input_iter:
        if not line:
            continue
        if ":" in line:
            if line.endswith(":"):
                shape = [line_to_bools(next(input_iter)) for _ in range(3)]
                shapes.append(shape)
            else:
                shape, _, presents = line.partition(":")
                presents = list(map(int, presents.split()))
                left, _, right = shape.partition("x")
                w, h = int(left), int(right)
                tree = Tree(w, h, presents)
                trees.append(tree)

        else:
            raise Exception("Invalid line: ", line)

    return shapes, trees


def part1(shapes: list[Shape], trees: list[Tree]):
    count = 0
    cellls_per_shape = {
        i: count_cells_in_shape(shape) for i, shape in enumerate(shapes)
    }

    for tree in trees:
        available_cells = tree.height * tree.width
        needed_cells = sum(p * cellls_per_shape[i] for i, p in enumerate(tree.presents))
        if needed_cells <= available_cells:
            count += 1
    return count


def part2(shapes: list[Shape], trees: list[Tree]):
    pass


def main():
    test_input = """
""".strip()

    # shapes, trees = read_input(test_input)
    shapes, trees = read_input()

    ans1 = part1(shapes, trees)
    print(f"{ans1= }")

    ans2 = part2(shapes, trees)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
