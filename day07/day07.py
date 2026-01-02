from tkinter.messagebox import RETRY


def read_input(input=None):
    if not input:
        with open("day07/input.txt", "r") as f:
            input = f.read().strip()
    input = [l.strip() for l in input.split("\n")]
    return input


def part1(map: list[str]):
    w = len(map[0])
    start = map[0].index("S")
    beams = [False] * w
    beams[start] = True

    splits_count = 0

    for line in map[1:]:
        new_beams = [False] * w
        for x, beam in enumerate(beams):
            if not beam:
                continue
            if line[x] == "^":
                splits_count += 1
                if x - 1 >= 0:
                    new_beams[x - 1] = True
                if x + 1 <= w - 1:
                    new_beams[x + 1] = True
            else:
                new_beams[x] = True
        beams = new_beams

    return splits_count


def part2(map):
    w = len(map[0])
    start = map[0].index("S")
    beams = [0] * w
    beams[start] = 1

    for line in map[1:]:
        new_beams = [0] * w
        for x, beam in enumerate(beams):
            if beam == 0:
                continue
            if line[x] == "^":
                if x - 1 >= 0:
                    new_beams[x - 1] += beam
                if x + 1 <= w - 1:
                    new_beams[x + 1] += beam
            else:
                new_beams[x] += beam
        beams = new_beams
    return sum(beams)


def main():
    test_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
