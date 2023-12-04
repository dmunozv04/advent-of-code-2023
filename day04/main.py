def part01():
    with open("day04/input.txt", "r") as f:
        file = f.read()
    sum = 0
    for line in file.split("\n"):
        data = line.split(": ")[1]
        cards, winners = data.split(" | ")
        cards = set([int(i.strip()) for i in cards.split()])
        winners = set([int(i.strip()) for i in winners.split()])
        num_of_wins = len(cards & winners)
        sum += (2 ** (num_of_wins -1)) if num_of_wins != 0 else 0
    print(sum)


def part02():
    with open("day04/input.txt", "r") as f:
        file = f.read()
    decks: list[(int, int)] = [] # number of reps of the card, number of wins of the card
    for line in file.split("\n"):
        num, data = line.split(": ")
        cards, winners = data.split(" | ")
        cards = set([int(i.strip()) for i in cards.split()])
        winners = set([int(i.strip()) for i in winners.split()])
        decks.append((1, len(cards & winners)))
    for index in range(len(decks)):
        num_of_reps, num_of_wins = decks[index]
        for deck_num in range(index+1, index+num_of_wins+1):
            decks[deck_num] = (decks[deck_num][0] + num_of_reps, decks[deck_num][1])
    result = sum(i[0] for i in decks)
    print(result)
if __name__ == "__main__":
    # part01()
    part02()