from collections import defaultdict
from random import randint
from pprint import pprint as pp


def main():
    frequency = defaultdict(int)
    for i in range(100):
        d1, d2 = randint(1, 6), randint(1, 6)
        frequency[d1 + d2] += 1


    pp(frequency)


def checkBuiltInDict():
    frequencymap = {1: 3, 4: 5}
    pp("get value -->" + str(frequencymap[4]))


if __name__ == "__main__":
    main()
    checkBuiltInDict()
