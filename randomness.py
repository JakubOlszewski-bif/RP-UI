import random
"""Module with randomness used in the game"""

def throw_dice(d: int, n: int):
    """Throw a n-number of d-sided dice"""
    return [random.randint(1,d) for i in range(n)]


if __name__ == "__main__":
    while True:
        d = int(input("How many sides?: "))
        n = int(input("How many dice?: "))
        print(throw_dice(d,n))