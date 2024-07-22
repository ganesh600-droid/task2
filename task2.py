import random
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    low = 1
    high = 100
    tries = 0
    while True:
        guess = random.randint(low, high)
        print(f"My guess is {guess}.")
        tries += 1
        feedback = input("Is my guess too high (h), too low (l), or correct (c)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} correctly in {tries} tries.")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    print("Thank you for playing!")
# Start the game
guessing_game()
