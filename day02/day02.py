import math
from typing import Iterator


def read_input(input=None):
    if not input:
        with open("day02/input.txt", "r") as f:
            input = f.read().strip()
    input = [tuple(map(int, r.strip().split("-"))) for r in input.split(",")]
    return input


def is_valid_id(id: int) -> bool:
    id_str = str(id)
    if len(id_str) % 2 != 0:
        return True
    mid = len(id_str) // 2
    if id_str[:mid] == id_str[mid:]:
        return False
    return True


def part1(input):
    invalid_ids = []
    for start, end in input:
        for id in range(start, end + 1):
            if not is_valid_id(id):
                invalid_ids.append(id)
    return sum(invalid_ids)


def divisors(num: int) -> Iterator[int]:
    for i in range(2, math.floor(num / 2) + 1):
        if num % i == 0:
            yield i
    yield num


def is_valid_id_2(id: int) -> bool:
    id_str = str(id)
    n = len(id_str)
    if n < 2:
        return True

    for divisor in divisors(n):
        block_len = n // divisor
        block = id_str[:block_len]
        fail = False
        for i in range(block_len, n, block_len):
            if block != id_str[i : i + block_len]:
                fail = True
                break
        if not fail:
            return False
    return True


def part2(input):
    invalid_ids = []
    for start, end in input:
        for id in range(start, end + 1):
            if not is_valid_id_2(id):
                invalid_ids.append(id)
    print(invalid_ids)
    return sum(invalid_ids)


def main():
    test_input = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
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
