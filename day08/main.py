from math import lcm
from tqdm import tqdm
def part01():
    with open("day08/input.txt", "r") as file:
        f = file.read()
    lines = f.split("\n")
    moves = [*lines[0]]
    network = {}
    for i in lines[2:]:
        point, dests = i.split(" = ")
        dests = dests[1:-1].split(", ")
        network[point] = (tuple(dests))
    
    current_place = network["AAA"]  # Starts in AAA
    num_of_steps = 0
    while current_place != network["ZZZ"]:
        for i in moves:
            num_of_steps += 1
            match i:
                case "L":
                    current_place = network[current_place[0]]
                case "R":
                    current_place = network[current_place[1]]
    print(num_of_steps)


def part02():
    with open("day08/input.txt", "r") as file:
        f = file.read()
    lines = f.split("\n")
    moves = [*lines[0]]
    network: dict[tuple[str, tuple[str, str]]] = {}
    for i in lines[2:]:
        point, dests = i.split(" = ")
        dests = dests[1:-1].split(", ")
        network[point] = (point, tuple(dests))
    
    network_simp = {}  # current -> next after round
    for v in network.values():
        current_place = network[v[0]]
        # print(current_place)
        for i in moves:
            match i:
                case "L":
                    current_place = network[current_place[1][0]]
                case "R":
                    current_place = network[current_place[1][1]]
        network_simp[v[0]] = current_place[0]

    current_places = [i for i in network_simp.items() if i[0][-1:] == "A"]
    start_places = [i for i in network_simp.items() if i[0][-1:] == "A"]
    # start_places = current_places
    print(current_places)
    num_of_moves = len(moves)
    rounds_loop_all = []
    for index, place in enumerate(current_places):
        bar = tqdm()
        rounds_to_loop = 0
        while place[0][-1:] != "Z":
            next = place[1]
            place = (next, network_simp[next])
            rounds_to_loop += 1
            bar.update()
        rounds_loop_all.append(rounds_to_loop)
        bar.close()
    print(rounds_loop_all)
    rounds_loop_all = [num_of_moves * i for i in rounds_loop_all]
    # Apparently it loops so I can use lcm :)
    print(lcm(*rounds_loop_all))
    # Naive solution that would've taken too much time
    # while not len([i for i in current_places if i[0][-1:] != "Z"]) == 0: # While at least one doesn't end in Z
    #     new_places = []
    #     for _, next in current_places:
    #         new_places.append((next, network_simp[next]))
    #     num_of_moves += 1
    #     bar.update()
    #     current_places = new_places
    # bar.close()
    # print(num_of_moves * len(moves))

if __name__ == "__main__":
    # part01()
    part02()