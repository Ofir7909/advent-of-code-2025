from functools import reduce
import operator


def read_input(input=None):
    if not input:
        with open("day06/input.txt", "r") as f:
            input = f.read().strip()
    try_int = lambda s: int(s) if s not in "+*" else s
    input = [list(map(try_int, l.split())) for l in input.split("\n")]
    return input


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def part1(input):
    input = transpose(input)
    total_sum = 0
    for equation in input:
        operand = equation[-1]
        nums = equation[:-1]
        if operand == "*":
            total_sum += reduce(operator.mul, nums, 1)
        else:
            total_sum += sum(nums)
    return total_sum


def part2():
    with open("day06/input.txt", "r") as f:
        input = f.read().strip()
    lines = input.split("\n")

    num_lines = lines[:-1]
    i = 0
    chunks = []
    while i < len(num_lines[0]):
        start = i
        while i < len(num_lines[0]) and not all(line[i] == " " for line in num_lines):
            i += 1
        chunks.append(list(line[start:i] for line in lines))
        i += 1

    total_sum = 0
    for c in chunks:
        operand = c[-1].strip()
        nums_str = ["".join(num) for num in transpose(c[:-1])]
        nums = list(map(int, nums_str))
        if operand == "*":
            total_sum += reduce(operator.mul, nums, 1)
        else:
            total_sum += sum(nums)

    return total_sum


def main():
    test_input = """
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2()
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
