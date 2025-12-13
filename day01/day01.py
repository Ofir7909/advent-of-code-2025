def read_input(input=None):
    if not input:
        with open("day01/input.txt", "r") as f:
            input = f.read().strip()
    input = [l.strip() for l in input.split("\n")]
    input = [(l[0], int(l[1:])) for l in input]
    return input


def part1(input):
    curr = 50
    zero_counter = 0
    for dir, steps in input:
        if dir == "L":
            curr -= steps
        else:
            curr += steps

        curr %= 100
        if curr == 0:
            zero_counter += 1
    return zero_counter


def part2(input):
    curr = 50
    zero_counter = 0
    for dir, steps in input:
        prev = curr
        if dir == "L":
            curr -= steps
        else:
            curr += steps

        if curr >= 100:
            zero_counter += curr // 100
            curr %= 100
        elif curr <= 0:
            zero_counter += abs(curr // 100) - 1
            if curr % 100 == 0:
                zero_counter += 1
            if prev != 0:
                zero_counter += 1
            curr %= 100

        # print(dir, steps, "===", curr, curr % 100, "===", curr // 100, zero_counter)

    return zero_counter


def main():
    test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()

    # input = read_input(test_input)
    input = read_input()

    # print(input)

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
