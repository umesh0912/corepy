from pprint import pprint as pp
from math import sqrt
import os
import glob


def readfile():
    with open('test.txt', 'r+') as f:
        read_data = f.read()
    # f.write('Piyush is very cute')

    print(read_data)


def printSysPaths():
    file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
    pp(file_sizes)


def isPrime(number):
    if number < 2:
        return False

    # for i in range(2, int(sqrt(number))+1):
    #    if number % i == 0:
    #         return False

    # return True
    t = 2
    while (number % t != 0):
        t += 1

    if number == t:
        return True
    elif number != t:
        return False
    return False


def listComprehensionDemo(ipString):
    words = ipString.split()
    wordsLength = [len(word) for word in words]
    return wordsLength


def dictComprehensionDemo(ipDict):
    return {capital: state for state, capital in ipDict.items()}


def main():
    wordsLen = listComprehensionDemo('I love my son piyush and my sweet wife puja!')
    print(f'words len {wordsLen}')

    state_to_capital = {'Maharashtra': 'mumbai',
                        'WestBangal': 'kolkata',
                        'Karnatak': 'banglore'}

    capital_to_state = dictComprehensionDemo(state_to_capital)
    x = [x for x in range(10) if isPrime(x)]
    print(x)
    pp(capital_to_state)

    printSysPaths()
    readfile()


if __name__ == "__main__":
    main()
else:
    print("core module impoerted succesfully")
