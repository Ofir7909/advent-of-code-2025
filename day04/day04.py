def read_input(input=None):
    if not input:
        with open("day04/input.txt", "r") as f:
            input = f.read().strip()
    input = [l.strip() for l in input.split("\n")]
    return input


adj8 = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def part1(map):
    m, n = len(map), len(map[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if map[i][j] != "@":
                continue

            paper_count = 0
            for dj, di in adj8:
                if i + di in range(m) and j + dj in range(n):
                    if map[i + di][j + dj] == "@":
                        paper_count += 1

            if paper_count < 4:
                ans += 1
    return ans


def part2(map):
    m, n = len(map), len(map[0])
    ans = 0

    neighbors = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if map[i][j] != "@":
                neighbors[i][j] = -1
                continue

            paper_count = 0
            for dj, di in adj8:
                if i + di in range(m) and j + dj in range(n):
                    if map[i + di][j + dj] == "@":
                        paper_count += 1
            neighbors[i][j] = paper_count

    changed = True
    while changed:
        changed = False
        for i in range(m):
            for j in range(n):
                if neighbors[i][j] == -1:
                    continue
                if neighbors[i][j] < 4:
                    changed = True
                    ans += 1
                    neighbors[i][j] = -1
                    for dj, di in adj8:
                        if (
                            i + di in range(m)
                            and j + dj in range(n)
                            and neighbors[i + di][j + dj] != -1
                        ):
                            neighbors[i + di][j + dj] -= 1
    return ans


def main():
    test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
