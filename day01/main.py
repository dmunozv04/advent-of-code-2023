
def part01():
    acumulator = 0
    with open("day01/input.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        numbers_this_line = ""
        for j in line:
            if j.isdigit():
                numbers_this_line += j
                break
        for j in reversed(line):
            if j.isdigit():
                numbers_this_line += j
                break
        acumulator += int(numbers_this_line)
    print(acumulator)


REPLACEMENTS = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9")
]


def part02():
    acumulator = 0
    with open("day01/input.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        numbers_this_line = []
        for x in range(0, len(line)):
            subline = line[x:]
            # print(subline[:1])
            for i in REPLACEMENTS:
                if subline.startswith(i[0]):
                    numbers_this_line.append(i[1])
            if subline[:1].isdigit():
                numbers_this_line.append(subline[:1])
        acumulator += int(numbers_this_line[0] + numbers_this_line[-1])
    print(acumulator)


if __name__ == "__main__":
    # part01()
    part02()
