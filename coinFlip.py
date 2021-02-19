import random

coinDict = {0: "heads", 1: "tails", }


def main():
    print("Welcome to coinFlip!")

    while True:

        print("Please choose Heads, Tails or Quit")

        bet = input()
        bet = bet.lower()

        if bet == "quit":
            print("Thanks for playing!")
            break

        if bet != "heads" and bet != "tails":
            print("Please only use Heads or Tails, try again.")
            continue

        # Generate a random number either 0 (Heads) or 1 (Tails)
        flip = random.randint(0, 1)

        print("It's", coinDict[flip])

        if coinDict[flip] == bet:
            print("You win!")
        else:
            print("You loose")


main()
