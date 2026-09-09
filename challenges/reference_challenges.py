# Challenge 01

def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples

    print("#1:", apples, oranges, papaya)

    apples = apples + oranges

    print("#2:", apples, oranges, papaya)


# Challenge 02

def challenge_02():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]

    print("#3:", apples, oranges, bananas)


# Challenge 03

def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)

    print("#4:", kiwis, mangos)


def challenge_03():
    bananas = [1729, 42]
    challenge_03_helper(bananas)

    print("Back in challenge_03:", bananas)