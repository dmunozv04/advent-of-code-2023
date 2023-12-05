import itertools
from math import inf
from tqdm import tqdm
from bisect import bisect_left
def chunks(xs, n):
    n = max(1, n)
    return (xs[i:i+n] for i in range(0, len(xs), n))

def parse_rules(segment):
    segment = segment.split("\n")[1:]
    rules: list[(int, int, int)] = []
    for line in segment:
        rule_parts = [int(x) for x in line.split()]
        rules.append(
            (*rule_parts, rule_parts[1] + rule_parts[2] - 1)
        )  # (dest-range-start, source-range-start, range-length)
    return sorted(rules, key= lambda x: x[1] + x[2] - 1)

def parse_rules_num(segment):
    segment = segment.split("\n")[1:]
    rules: list[(int, int, int)] = []
    for line in segment:
        rule_parts = [int(x) for x in line.split()]
        rules.append(rule_parts[1] + rule_parts[2] - 1) 
    return sorted(rules)

# class KeyWrapper:
#     def __init__(self, iterable, key):
#         self.it = iterable
#         self.key = key

#     def __getitem__(self, i):
#         return self.key(self.it[i])

#     def __len__(self):
#         return len(self.it)

def transform(element, rules, rules_wrapped):
    # rule_to_choose = [rule for rule in rules if rule[1] <= element and (rule[1] + rule[2]) > element]
    # if rule_to_choose:
    #     rule = rule_to_choose[0]
    #     return rule[0] + (element - rule[1])
    # return element
    #Replace with binary search maintaining the range of the rule
    rule_to_choose = bisect_left(rules_wrapped, element)
    if rule_to_choose == len(rules):
        return element
    rule = rules[rule_to_choose]
    if(rule[1] <= element):
        return rule[0] + (element - rule[1])
    return element




def do_transforms(element, rules_all):
    for rules, rules_wrapped in rules_all:
        # print("hi")
        # print(rules, rules_wrapped)
        element = transform(element, rules, rules_wrapped)
        # print(element)
    return element


def part01():
    with open("day05/input.txt", "r") as f:
        file = f.read()
    locations = []
    segments = file.split("\n\n")
    seeds = [int(x) for x in segments[0].split(": ")[1].split()]
    # print(seeds)
    packs_of_rules = [parse_rules(i) for i in segments[1:]]
    # print(packs_of_rules)
    locations = [do_transforms(seed, packs_of_rules) for seed in seeds]
    # print(locations)
    print(min(locations))

def get_seeds(seed_ranges):
    for i in seed_ranges:
        for j in range(i[0], i[0] + i[1]):
            yield j
# Ugly and slow solution, but it works.
# Takes 5 minutes to run on a decent machine with pypy
def part02():
    with open("day05/input.txt", "r") as f:
        file = f.read()
    segments = file.split("\n\n")
    seed_ranges = [int(x) for x in segments[0].split(": ")[1].split()]
    seed_ranges = list(chunks(seed_ranges, 2))
    total_seeds = sum([i[1] for i in seed_ranges])
    # print(seed_ranges)
    #seeds = get_seeds(seed_ranges)
    packs_of_rules = [parse_rules(i) for i in segments[1:]]
    packs_of_rules_wrapped = [parse_rules_num(i) for i in segments[1:]]
    #print(packs_of_rules_wrapped)
    rules_all = tuple(zip(packs_of_rules, packs_of_rules_wrapped))
    min_location = inf

    for i in tqdm(get_seeds(seed_ranges), total = total_seeds):
            min_location = min(min_location, do_transforms(i, rules_all))
    print(min_location)



if __name__ == "__main__":
    #part01()
    part02()