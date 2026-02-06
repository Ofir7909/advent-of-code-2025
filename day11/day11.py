from collections import defaultdict, deque


def read_input(input=None):
    if not input:
        with open("day11/input.txt", "r") as f:
            input = f.read().strip()
    input = [l.strip() for l in input.split("\n")]

    connections = {}
    for line in input:
        device = line[: line.index(":")]
        to = line[line.index(":") + 1 :].split()
        connections[device] = to
    return connections


def topological_sort(graph: dict[str, list[str]]):
    topo_order = []
    visited = set()

    def topo_dfs(v: str):
        visited.add(v)
        for u in graph.get(v, []):
            if u not in visited:
                topo_dfs(u)
        topo_order.append(v)

    for v in graph:
        if v not in visited:
            topo_dfs(v)
    return topo_order


def count_paths_from_to(graph: dict[str, list[str]], src: str, dst: str):
    possible_paths_from_src = defaultdict(int)
    possible_paths_from_src[src] = 1

    topological_order = topological_sort(graph)

    for v in reversed(topological_order):
        for u in graph.get(v, []):
            possible_paths_from_src[u] += possible_paths_from_src[v]

    return possible_paths_from_src[dst]


def part1(connections: dict[str, list[str]]):
    return count_paths_from_to(connections, "you", "out")


def part2(connections: dict[str, list[str]]):
    total = 0
    total += (
        count_paths_from_to(connections, "svr", "dac")
        * count_paths_from_to(connections, "dac", "fft")
        * count_paths_from_to(connections, "fft", "out")
    )
    total += (
        count_paths_from_to(connections, "svr", "fft")
        * count_paths_from_to(connections, "fft", "dac")
        * count_paths_from_to(connections, "dac", "out")
    )
    return total


def main():
    test_input = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip()

    test_input_2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()

    # input = read_input(test_input_2)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
