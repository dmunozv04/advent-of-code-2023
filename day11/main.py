from itertools import combinations


def part01():
    with open("day11/input.txt", "r") as file:
        f = file.read()
    im = [[*line] for line in f.split("\n")]
    
    # Add extra empty lines
    empty_lines = []
    for y, line in enumerate(im):
        if all(i == "." for i in line):  # Empty line
            empty_lines.append(y + len(empty_lines))
    for i in empty_lines:
        im.insert(i, ["." for i in range(len(im[0]))])
    
    # Add extra empty columns
    empty_cols = []
    im_flipped = zip(*im)
    for x, line in enumerate(im_flipped):
        if all(i == "." for i in line):  # Empty line
            empty_cols.append(x + len(empty_cols))
    for i in empty_cols:
        for line in im:
            line.insert(i, ".")
    
    # print(im)
    # Calculate distances
    stars = [(y,x) for y, line in enumerate(im) for x, char in enumerate(line) if im[y][x] == "#"]
    # print(stars)
    sum = 0
    for i, j in combinations(stars, 2):
        sum += abs(j[0]-i[0]) + abs(j[1]-i[1])
    print(sum)


def part02():
    increase = 1000000 -1 # Already counting original once
    with open("day11/input.txt", "r") as file:
        f = file.read()
    im = [[*line] for line in f.split("\n")]
    
    # Count extra empty lines
    empty_lines = []
    for y, line in enumerate(im):
        if all(i == "." for i in line):  # Empty line
            empty_lines.append(y)

    # Count extra empty columns
    empty_cols = []
    im_flipped = zip(*im)
    for x, line in enumerate(im_flipped):
        if all(i == "." for i in line):  # Empty line
            empty_cols.append(x)

    # print(im)
    # Calculate distances
    stars = [(y,x) for y, line in enumerate(im) for x, char in enumerate(line) if im[y][x] == "#"]

    sum = 0
    for i, j in combinations(stars, 2):
        sum += abs(j[0]-i[0]) + abs(j[1]-i[1])
        for k in range(min(i[0], j[0]), max(i[0], j[0])+1):
            #print(k)
            if k in empty_lines:
                sum += increase
        #print()
        for k in range(min(i[1], j[1]), max(i[1], j[1])+1):
            #print(k)
            if k in empty_cols:
                sum += increase

    print(sum)


if __name__ == "__main__":
    part01()
    part02()