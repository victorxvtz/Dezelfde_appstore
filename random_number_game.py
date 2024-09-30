import random
import main
import tkinter as tk

def play():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print("Try to guess the number in as few attempts as possible")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 20

    print(f"you get {max_attempts} attempts")


    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        elif attempts >= max_attempts:
            print("You have reached the maximum number of attempts")
            print("The number was", number)
            break
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        play()
    else:
        print("Thanks for playing!")
        main.menu()
