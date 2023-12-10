from types import NoneType


def find_start(maze: list[tuple[str]]) -> tuple[int, int]:
    for s_y, line in enumerate(maze):
        try:
            s_x = line.index("S")
            break
        except ValueError:
            pass  # Not in this line
    return (s_y, s_x)


def get_vectors(pipe):
    vectors = []
    match pipe:
        case "|":
            vectors = [(1,0), (-1,0)]
        case "-":
            vectors = [(0,1), (0,-1)]
        case "L":
            vectors = [(-1,0), (0,1)]
        case "J":
            vectors = [(-1,0), (0,-1)]
        case "7":
            vectors = [(0,-1), (1,0)]
        case "F":
            vectors = [(0,1), (1,0)]
        case ".":
            vectors = []
        case "S":
            vectors = [(1,0), (-1,0), (0,1), (0,-1)]
    # if len(vectors) == 0:
    #     print(pipe)
    #     print("________")
    return vectors


def find_next_move(maze: list[tuple[str]], visited: set[tuple[int, int]], pos: tuple[int, int]):
    current_pos: str = maze[pos[0]][pos[1]]
    #print(current_pos)
    vectors = get_vectors(current_pos)
    for vec in vectors:
        possible_next_pos = (pos[0] + vec[0], pos[1] + vec[1])
        #print(possible_next_pos)
        if possible_next_pos not in visited and possible_next_pos[0] >= 0 and possible_next_pos[1] >= 0 and possible_next_pos[0] < len(maze) and possible_next_pos[1] < len(maze[0]):
            visited.add(possible_next_pos)
            #print(possible_next_pos)
            return possible_next_pos


def find_start_moves(maze: list[tuple[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    positions = []
    vectors = [(1,0), (-1,0), (0,1), (0,-1)]
    for vec in vectors:
        possible_next_pos = (pos[0] + vec[0], pos[1] + vec[1])
        if possible_next_pos[0] >= 0 and possible_next_pos[1] >= 0 and possible_next_pos[0] < len(maze) and possible_next_pos[1] < len(maze[0]):
            possible_next_pos_value: str = maze[possible_next_pos[0]][possible_next_pos[1]]
            if possible_next_pos_value != ".":  # There's a pipe there
                positions.append(possible_next_pos)
    return positions


def check_if_loop(maze: list[tuple[str]], pos: tuple[int, int], start):
    visited = set()
    visited.add(pos)
    
    is_connected = False
    for vec in get_vectors(maze[pos[0]][pos[1]]):
        pos_before = (pos[0] + vec[0], pos[1] + vec[1])
        if start == pos_before:
            is_connected = True
            break
    if not is_connected:
        return False
    return True

    # while maze[pos[0]][pos[1]] != "S":  # Not at start
    #     new_pos = find_next_move(maze, visited, pos)
    #     if new_pos is None:
    #         return False
    #     # Check if new piece connects to old one
    #     is_connected = False
    #     for vec in get_vectors(maze[new_pos[0]][new_pos[1]]):
    #         pos_before = (new_pos[0] + vec[0], new_pos[1] + vec[1])
    #         if pos_before == pos:
    #             is_connected = True
    #             pos = new_pos
    #             break
    #     if not is_connected:
    #         return False
    # print("DONE")
    # return True


def part01():
    with open("day10/input.txt", "r") as file:
        f = file.read()
    maze = [(*i, ) for i in f.split("\n")]
    start = find_start(maze)
    #print(start)
    positions_start = find_start_moves(maze, start)
    #print(positions_start)
    positions_start = [i for i in positions_start if check_if_loop(maze, i, start)]
    #print(positions_start)
    
    pos_1 = positions_start[0]
    pos_2 = positions_start[1]
    visited_1 = set()
    visited_2 = set()
    
    visited_1.add(start)
    visited_2.add(start)
    
    visited_1.add(positions_start[0])
    visited_2.add(positions_start[1])
    count = 0
    while pos_1 != pos_2:
        pos_1 = find_next_move(maze, visited_1, pos_1)
        pos_2 = find_next_move(maze, visited_2, pos_2)
        #print(f"{maze[pos_1[0]][pos_1[1]]}...")
        #print(f"...{maze[pos_2[0]][pos_2[1]]}")
        #print(visited_1)
        #print(visited_2)
        #print()
        count += 1
    print(count+1)


def are_connected(maze, pos, start):
    #print(f"Check connected on {pos[0]}, {pos[1]}")
    is_connected = False
    for vec in get_vectors(maze[pos[0]][pos[1]]):
        pos_before = (pos[0] + vec[0], pos[1] + vec[1])
        if start == pos_before:
            is_connected = True
            break
    if not is_connected:
        return False
    #print(f"Connected on {pos[0]}, {pos[1]}")
    return True


def check_if_inside(maze, loop, pos_start):
    vectors = [(1,0), (-1,0), (0,1), (0,-1)]
    crosses = []
    for vec in vectors:
        pos = (pos_start[0], pos_start[1])
        num_of_crosses = 0
        while pos[0] > 0 and pos[1] > 0 and pos[0] < len(maze)  and pos[1] < len(maze[0]) :
            pos = (pos[0] + vec[0], pos[1] + vec[1])
            # pos_value = map[pos[0]][pos[1]]
            if pos in loop:
                num_of_crosses += 1
        crosses.append(num_of_crosses)
    return not any([i % 2 == 0 for i in crosses])


def get_start_piece(start, positions_start):
    # Start piece can be one of 4 possible
    vectors_start = []
    for i in positions_start:
        vec = (i[0] - start[0], i[1] - start[1])
        vectors_start.append(vec)
    vectors_start = sorted(vectors_start)
    match vectors_start:
        case [(-1,0), (0,1)]:
            return "L"
        case [(-1,0), (0,-1)]:
            return "J"
        case [(0,-1), (1,0)]:
            return "7"
        case [(0,1), (1,0)]:
            return "F"


def part02():
    with open("day10/input.txt", "r") as file:
        f = file.read()
    maze = [(*i, ) for i in f.split("\n")]
    start = find_start(maze)
    #print(start)
    positions_start = find_start_moves(maze, start)
    #print(positions_start)
    positions_start = [i for i in positions_start if check_if_loop(maze, i, start)]
    #print(positions_start)
    
    pos_1 = positions_start[0]
    pos_2 = positions_start[1]
    visited_1 = set()
    visited_2 = set()
    
    visited_1.add(start)
    visited_2.add(start)
    
    visited_1.add(positions_start[0])
    visited_2.add(positions_start[1])
    while pos_1 != pos_2:
        pos_1 = find_next_move(maze, visited_1, pos_1)
        pos_2 = find_next_move(maze, visited_2, pos_2)
    loop = visited_1.union(visited_2)
    #print(list(sorted(loop)))
    #print(maze)
    count = 0
    
    # Change S for appropriate piece
    maze[start[0]] = list(maze[start[0]])
    maze[start[0]][start[1]] = get_start_piece(start, positions_start)
    maze[start[0]] = tuple(maze[start[0]])
    #print(maze[start[0]][start[1]])
    for y, line in enumerate(maze):
        is_inside_loop = False
        last_char = ""
        for x, char in enumerate(line):
            if (y,x) not in loop:  # Every piece not in the loop can be counted
                if is_inside_loop:
                    #print(f"char {char} {y}, {x} in loop")
                    count += 1
            else:
                if char == "-": # Doesn't change a thing, it'll always have parts at both sides
                    pass
                elif char == "|":
                    is_inside_loop = not is_inside_loop # Always switches 
                elif char == "F" or char == "L":
                    last_char = char # Save to evaluate what happens with the "turn"
                elif char == "7":
                    if last_char == "F": # F7 doesn't change if it's in loop
                        pass
                    if last_char == "L": # Crosses loop boundary
                        is_inside_loop = not is_inside_loop
                elif char == "J":
                    if last_char == "L": # LJ doesn't change if it's in loop
                        pass
                    if last_char == "F": # Crosses loop boundary
                        is_inside_loop = not is_inside_loop
    print(count)


if __name__ == "__main__":
    part01()
    part02()