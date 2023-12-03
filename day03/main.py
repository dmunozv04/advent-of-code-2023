import copy


def check_if_part(schem, current_num_positions):
    vectors = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1),  # 0,0 not needed
                       (1, -1), (1, 0), (1, 1)]
    for pos in current_num_positions:
        y, x = pos
        for v in vectors:
            char_to_check = schem[y + v[0]][x + v[1]]
            if (not char_to_check.isnumeric()) and (char_to_check != "."):
                return True
    return False


def part01():
    with open("day03/input.txt", "r") as f:
        schem = f.readlines()
    # pad input
    schem.insert(0, "."*(len(schem[0])-1))
    schem.append("."*(len(schem[0])-1))
    for i, line in enumerate(schem):
        line = line.strip("\n")
        schem[i] = "." + line + "."
    sum = 0

    for y, line in enumerate(schem):
        current_num_values = ""
        current_num_positions = []

        for x, char in enumerate(line):
            if char.isnumeric():
                current_num_positions.append((y, x))
                current_num_values += char
            elif len(current_num_positions) != 0:
                if check_if_part(schem, current_num_positions):
                    sum += int(current_num_values)
                current_num_values = ""
                current_num_positions = []
    print(sum)


def check_if_gear(schem, pos):
    nums = []
    schem = copy.deepcopy(schem)
    pos_y, pos_x = pos
    vectors = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),  # 0,0 not needed
                    (1, -1), (1, 0), (1, 1)]
    for v in vectors:
        num_actual = ""
        char_to_check = schem[pos_y + v[0]][pos_x + v[1]]
        char_to_check_start = schem[pos_y + v[0]][pos_x + v[1]]
        pos_start_y = pos_y + v[0]
        pos_start_x = pos_x + v[1]
        # Go left
        x_increment = 0
        had_left = False
        while(char_to_check.isnumeric()):
            had_left = True
            num_actual = char_to_check + num_actual
            schem[pos_y + v[0]] = schem[pos_y + v[0]][:pos_x + v[1] + x_increment] + "." + schem[pos_y + v[0]][pos_x + v[1] + x_increment + 1:] #Only count once
            x_increment -= 1
            char_to_check = schem[pos_y + v[0]][pos_x + v[1] + x_increment]
        char_to_check = char_to_check_start # Has been overridden with a .
        x_increment = 0
        # Go right
        while(char_to_check.isnumeric()):
            if had_left:
                had_left = False
            else:
                num_actual = num_actual + char_to_check
            schem[pos_y + v[0]] = schem[pos_y + v[0]][:pos_x + v[1] + x_increment] + "." + schem[pos_y + v[0]][pos_x + v[1] + x_increment + 1:] #Only count once
            x_increment += 1
            char_to_check = schem[pos_y + v[0]][pos_x + v[1] + x_increment]
        if num_actual:
            nums.append(int(num_actual))
    #print(nums)
    if len(nums) == 2:
        return nums[0] * nums[1]
    return 0

# Part02 wants me to do stuff the other way around 
def part02():
    with open("day03/input.txt", "r") as f:
        schem = f.readlines()
    # pad input
    schem.insert(0, "."*(len(schem[0])-1))
    schem.append("."*(len(schem[0])-1))
    for i, line in enumerate(schem):
        line = line.strip("\n")
        schem[i] = "." + line + "."
    sum = 0

    for y, line in enumerate(schem):
        for x, char in enumerate(line):
            if char == "*":
                sum += check_if_gear(schem, (y,x))
    print(sum)


if __name__ == "__main__":
    part02()