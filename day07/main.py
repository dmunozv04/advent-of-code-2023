from collections import Counter
from curses import has_extended_color_support
from heapq import heapify
from pprint import pprint as print
global debug
debug = False
def dprint(*arg):
    if debug:
        print(*arg)


class Hand:
    bid: int
    hand: str
    hand_str: str # Just for debuggin purposes
    type: int  # Smaller is worse ie: high card -> 1
    def __init__(self, line):
        hand, bid = line.split()
        self.hand_str = hand
        self.hand = self.hand_to_ints(hand)
        self.bid = int(bid)
        self.type = self.process_type(hand)
    
    def __repr__(self):
        return str(self.__dict__)
    
    @staticmethod
    def hand_to_ints(hand_str):
        hand = []
        for i in hand_str:
            if i.isdigit():
                hand.append(int(i))
            else:
                match i:
                    case "T":
                        hand.append(10)
                    case "J":
                        hand.append(11)
                    case "Q":
                        hand.append(12)
                    case "K":
                        hand.append(13)
                    case "A":
                        hand.append(14)
        return hand

    def process_type(self, hand):
        counter = Counter(hand).most_common()  # Get char counts ordered
        # dprint(counter)
        match len(counter):
            case 5: # All are different (high card)
                return 1
            case 4: # One pair
                return 2
            case 3: # 3 types
                if counter[0][1] == 2: # Two pairs
                    return 3
                if counter[0][1] == 3: # Three of a kind
                    return 4
            case 2: # 2 types
                if counter[0][1] == 3: # Full house
                    return 5
                if counter[0][1] == 4: # Four of a kind
                    return 6
            case 1: # Five of a kind
                return 7

    def __lt__(self, other):
        dprint(self)
        dprint(other)
        dprint(self.type < other.type)
        if self.type != other.type:
            return self.type < other.type
        else:
            for c_self, c_other in zip(self.hand, other.hand):
                if c_self != c_other:
                    return c_self < c_other


def part01():
    with open("day07/input.txt") as file:
        f = file.read()
    hands: list[Hand] = []
    for line in f.split("\n"):
        hands.append(Hand(line))
    hands.sort()
    dprint(hands)
    result = 0
    for index, hand in enumerate(hands, start = 1):
        result += index * hand.bid
    print(result)


class HandP2(Hand):
    @staticmethod
    def hand_to_ints(hand_str):
        hand = []
        for i in hand_str:
            if i.isdigit():
                hand.append(int(i))
            else:
                match i:
                    case "T":
                        hand.append(10)
                    case "J":
                        hand.append(1) # Joker is the weakest card
                    case "Q":
                        hand.append(12)
                    case "K":
                        hand.append(13)
                    case "A":
                        hand.append(14)
        return hand
    
    def process_type(self, hand):
        counter = Counter(hand)  # Get char counts ordered
        try:
            most_common = Counter(hand.replace("J", "")).most_common(1)[0][0] # Most common that isn't J
            if "J" in counter:
                counter[most_common] += counter["J"]
                del counter["J"]
        except: # ALL J
            return 7
        counter = counter.most_common()
        dprint(counter)
        match len(counter):
            case 5: # All are different (high card)
                return 1
            case 4: # One pair
                return 2
            case 3: # 3 types
                if counter[0][1] == 2: # Two pairs
                    return 3
                if counter[0][1] == 3: # Three of a kind
                    return 4
            case 2: # 2 types
                if counter[0][1] == 3: # Full house
                    return 5
                if counter[0][1] == 4: # Four of a kind
                    return 6
            case 1: # Five of a kind
                return 7
        print("something broke here")
        print(hand)
        print(most_common)


def part02():
    with open("day07/input.txt") as file:
        f = file.read()
    hands: list[HandP2] = []
    for line in f.split("\n"):
        hands.append(HandP2(line))
    hands.sort()
    dprint(hands)
    result = 0
    for index, hand in enumerate(hands, start = 1):
        result += index * hand.bid
    print(result)


if __name__ == "__main__":
    part01()
    part02()