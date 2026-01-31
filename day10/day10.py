from dataclasses import dataclass
from pprint import pprint
import pulp


@dataclass
class Machine:
    target_lights: list[bool]
    buttons: list[list[int]]
    voltages: list[int]


def read_input(input=None):
    if not input:
        with open("day10/input.txt", "r") as f:
            input = f.read().strip()

    lines = [l.strip() for l in input.split("\n")]

    machines = []
    for l in lines:
        l_split = l.split()
        target_lights = [c == "#" for c in l_split[0][1:-1]]
        buttons = [list(map(int, b[1:-1].split(","))) for b in l_split[1:-1]]
        voltages = [int(v) for v in l_split[-1][1:-1].split(",")]
        machines.append(Machine(target_lights, buttons, voltages))

    return machines


def part1(machines: list[Machine]):
    total = 0
    for machine in machines:
        prob = pulp.LpProblem(sense=pulp.LpMinimize)

        button_vars = [
            pulp.LpVariable(f"button{i}", cat=pulp.LpBinary)
            for i in range(len(machine.buttons))
        ]

        prob += pulp.lpSum(button_vars), "Objective Function"

        for light_index, light in enumerate(machine.target_lights):
            k = pulp.LpVariable(f"k{light_index}", cat=pulp.LpInteger)
            prob += (
                pulp.lpSum(
                    [
                        button_vars[i]
                        for i, button in enumerate(machine.buttons)
                        if light_index in button
                    ]
                )
                + light
                == 2 * k
            )

        prob.solve(pulp.PULP_CBC_CMD(msg=0))
        total += int(pulp.value(prob.objective))
    return total


def part2(machines: list[Machine]):
    total = 0
    for machine in machines:
        prob = pulp.LpProblem(sense=pulp.LpMinimize)

        button_vars = [
            pulp.LpVariable(f"button{i}", cat=pulp.LpInteger, lowBound=0)
            for i in range(len(machine.buttons))
        ]

        prob += pulp.lpSum(button_vars), "Objective Function"

        for voltage_index, voltage in enumerate(machine.voltages):
            prob += (
                pulp.lpSum(
                    [
                        button_vars[i]
                        for i, button in enumerate(machine.buttons)
                        if voltage_index in button
                    ]
                )
                == voltage,
                f"Voltage Index {voltage_index}",
            )

        prob.solve(pulp.PULP_CBC_CMD(msg=0))
        total += int(pulp.value(prob.objective))
    return total


def main():
    test_input = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1= }")

    ans2 = part2(input)
    print(f"{ans2= }")


if __name__ == "__main__":
    main()
