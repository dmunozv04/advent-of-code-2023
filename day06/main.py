def part01():
    with open("day06/input.txt", "r")as f:
        file = f.read()
    result = 1
    times, distances = file.split("\n")
    times = [int(x) for x in times.split(": ")[1].split()]
    distances = [int(x) for x in distances.split(": ")[1].split()]
    races = list(zip(times, distances))
    for race in races:
        ways_to_beat = 0
        total_time = race[0]
        distance_to_beat = race[1]
        #print(distance_to_beat)
        for hold_time in range(1,total_time):
            #print((total_time - hold_time) * hold_time )
            if (total_time - hold_time) * hold_time > distance_to_beat:
                ways_to_beat += 1
        #print(ways_to_beat)
        result *= ways_to_beat
    print(result)

def part02():
    with open("day06/input.txt", "r")as f:
        file = f.read()
    total_time, distance_to_beat = file.split("\n")
    total_time = int(total_time.split(": ")[1].replace(" ", ""))
    distance_to_beat = int(distance_to_beat.split(": ")[1].replace(" ", ""))
    ways_to_beat = 0
    first_hold = 0
    last_hold = 0
    #Find first and last time you win, then get the range
    for hold_time in range(1,total_time):
        if (total_time - hold_time) * hold_time > distance_to_beat:
            first_hold = hold_time
            break
    for hold_time in range(total_time ,0, -1):
        if (total_time - hold_time) * hold_time > distance_to_beat:
            last_hold = hold_time
            break
    print(last_hold - (first_hold -1))

if __name__ == '__main__':
    part01()
    part02()