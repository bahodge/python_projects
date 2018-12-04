import random

global collector
collector = {}


def roll_dice():
    return random.randint(1, 6)


def compare_dice_rolls(dice_1, dice_2):
    if dice_1 == dice_2:
        matching_dice_rolled(dice_1)
        return True
    else:
        return False


def roll_and_compare():
    d1 = roll_dice()
    d2 = roll_dice()
    result = compare_dice_rolls(d1, d2)
    return result


def matching_dice_rolled(dice):
    if dice not in collector:
        collector[dice] = 1
    else:
        collector[dice] += 1


def roll_the_dice(times):
    counter = 0
    for _ in range(1, times):
        result = roll_and_compare()
        if result == True:
            counter += 1

    for key in sorted(collector):
        print(str(key) + " matched " + str(collector[key]) + " times")

    print("Number of Matches: " + str(counter))


res = input("How Many Times To Roll the Dice?: ")
roll_the_dice(int(res))
