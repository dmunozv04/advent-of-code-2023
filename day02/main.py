def part01():
    result = 0
    with open("day02/input.txt", "r") as f:
        file = f.read()
    for line in file.split("\n"):
        parts = line.split(": ")
        game_num = int(parts[0].split(" ")[-1])
        rounds = parts[1].split("; ")
        is_possible = True
        for round in rounds:
            round_colors_str = round.split(", ")
            round_colors = {"red": 0, "green": 0, "blue": 0}
            for color in round_colors_str:
                color_parts = color.split()
                round_colors[color_parts[1]] = int(color_parts[0])
            if round_colors["red"] > 12 or round_colors["green"] > 13 or round_colors["blue"] > 14:
                is_possible = False
                break
        if is_possible:
            result += game_num
    print(result)


def part02():
    result = 0
    with open("day02/input.txt", "r") as f:
        file = f.read()
    for line in file.split("\n"):
        min_colors = {"red": 0, "green": 0, "blue": 0}
        parts = line.split(": ")
        # game_num = int(parts[0].split(" ")[-1])
        rounds = parts[1].split("; ")
        for round in rounds:
            round_colors_str = round.split(", ")
            for color in round_colors_str:
                color_parts = color.split()
                if min_colors[color_parts[1]] < int(color_parts[0]):
                    min_colors[color_parts[1]] = int(color_parts[0])
        result += min_colors["red"] * min_colors["green"] * min_colors["blue"]
    print(result)


if __name__ == "__main__":
    part01()
    part02()
