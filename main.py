# this is the game hub. this is where you choose which game you want to play

import math_quiz
import random_number_game
import galgje
import tkinter as tk

startup = True


def on_random_number_button_click():
    print("You chose the Random Number Game!")
    random_number_game.play()


def on_hangman_button_click():
    print("You chose Hangman!")
    galgje.play(galgje.get_word())


def on_math_quiz_button_click():
    print("You chose the Math Quiz!")
    math_quiz.startup_game()


def on_quit_button_click():
    print("Goodbye!")
    quit()


def menu():
    root = tk.Tk()
    root.config(width=400, height=300)
    root.title("Game Hub")

    text_label1 = tk.Label(root, text="Welcome to the game hub!")
    text_label2 = tk.Label(root, text="Choose a game to play:")
    text_label1.pack()
    text_label2.pack()

    random_number_button = tk.Button(root, text="Random Number Game", command=on_random_number_button_click)
    random_number_button.pack()

    hangman_button = tk.Button(root, text="Hangman", command=on_hangman_button_click)
    hangman_button.pack()

    math_quiz_button = tk.Button(root, text="Math Quiz", command=on_math_quiz_button_click)
    math_quiz_button.pack()

    quit_button = tk.Button(root, text="Quit", command=on_quit_button_click)
    quit_button.pack()

    root.mainloop()


menu()

# def menu():
#     print("Welcome to the game hub!")
#     print("Choose a game to play:")
#     print("1. Random Number Game")
#     print("2. Hangman")
#     print("3. Math Quiz")
#     print("4. Quit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         print("You chose the Random Number Game!")
#         random_number_game.play()
#     elif choice == "2":
#         print("You chose Hangman!")
#         galgje.play(galgje.get_word())
#     elif choice == "3":
#         print("You chose the Math Quiz!")
#         math_quiz.play()
#     elif choice == "4":
#         print("Goodbye!")
#         quit()
#     else:
#         print("Invalid input. Please enter a number between 1 and 4.")
#         menu()

# if startup:
#     menu()
#     startup = False
