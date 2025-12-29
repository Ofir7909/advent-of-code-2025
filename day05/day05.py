def read_input(input=None):
    if not input:
        with open("day05/input.txt", "r") as f:
            input = f.read().strip()
    fresh_ing, avail_ing = input.split("\n\n")
    fresh_ing = [tuple(map(int, l.split("-"))) for l in fresh_ing.split("\n")]
    avail_ing = [int(l) for l in avail_ing.split("\n")]
    return fresh_ing, avail_ing


def is_fresh(fresh_ing_ranges, ing):
    for r in fresh_ing_ranges:
        if ing in r:
            return True
    return False


def part1(fresh_ing, avail_ing):
    fresh_ing_ranges = [range(s, e + 1) for s, e in fresh_ing]
    count = 0
    for ing in avail_ing:
        if is_fresh(fresh_ing_ranges, ing):
            count += 1
    return count


def part2(fresh_ing):
    fresh_ing = sorted(fresh_ing, key=lambda r: r[0])
    n = len(fresh_ing)
    total = 0

    i = 0
    while i < n:
        start = fresh_ing[i][0]
        end = fresh_ing[i][1]
        i += 1
        while i < n and fresh_ing[i][0] <= end:
            end = max(end, fresh_ing[i][1])
            i += 1
        total += end - start + 1
    return total


def main():
    test_input = """
""".strip()

    # fresh_ing, avail_ing = read_input(test_input)
    fresh_ing, avail_ing = read_input()

    ans1 = part1(fresh_ing, avail_ing)
    print(f"{ans1= }")

    ans2 = part2(fresh_ing)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
