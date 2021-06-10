import random
NUM_SIDES = 6
def main():
    #random.seed(1)
    die1 = random.randint(1,NUM_SIDES)
    die2 = random.randint(1,NUM_SIDES)
    total = die1+die2
    print("Dice have",NUM_SIDES,"side each.")
    print("First Dice:",die1)
    print("Second Dice:",die2)
    print("Total of two Dice:",total)
main()
