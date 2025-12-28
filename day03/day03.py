def read_input(input=None):
    if not input:
        with open("day03/input.txt", "r") as f:
            input = f.read().strip()
        input = [list(map(int, l)) for l in input.split("\n")]
    return input


def argmax(array):
    return max(range(len(array)), key=lambda x: array[x])


def part1(banks):
    total_volts = 0
    for bank in banks:
        first_digit_index = argmax(bank[:-1])
        first_digit = bank[first_digit_index]
        second_digit = max(bank[first_digit_index + 1 :])
        total_volts += first_digit * 10 + second_digit
    return total_volts


def max_voltage_with_n_batteries(bank: list[int], n: int):
    if n == 1:
        return max(bank)
    first_digit_index = argmax(bank[: -n + 1])
    first_digit = bank[first_digit_index]
    rest = max_voltage_with_n_batteries(bank[first_digit_index + 1 :], n - 1)
    return first_digit * 10 ** (n - 1) + rest


def part2(banks):
    total_volts = 0
    for bank in banks:
        total_volts += max_voltage_with_n_batteries(bank, 12)
    return total_volts


def main():
    test_input = """
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
