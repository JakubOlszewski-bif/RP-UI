import random
"""Module with randomness used in the game"""

def throw_dice(d: int):
    return random.randint(1,d)


if __name__ == "__main__":
    while True:
        d = int(input("How many sides?: "))
        print(throw_dice(d))