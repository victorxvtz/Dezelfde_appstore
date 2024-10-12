import random
import tkinter as tk
from PIL import Image, ImageTk


def restart_game(root):
    root.destroy()
    play(get_word())


def get_word():
    with open(r"C:\Users\victo\PycharmProjects\Dezelfde_appstore\Wordlist.txt", "r") as file:
        word_list = file.readlines()
    word = random.choice(word_list)
    return word


def play(word):
    root = tk.Toplevel()
    root.title("Hangman")

    word_completion = "_" * len(word)
    display_hangman = [rf"C:\Users\victo\PycharmProjects\Dezelfde_appstore\Hangman_images\{i}.jpg" for i in range(4, 11)]

    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = [6]  # Wrapping tries in a list to pass by reference

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)


    text_label1 = tk.Label(root, text="Welcome to Hangman!")
    text_label2 = tk.Label(root, text=f"current word: {word_completion}")
    entry = tk.Entry(root)
    text_label3 = tk.Label(root, text=f"you have {tries[0]} tries left")
    text_label4 = tk.Label(root, text="")
    text_label1.grid(row=0, column=1, padx=10, pady=10)
    text_label2.grid(row=1, column=1, padx=10, pady=10)
    entry.grid(row=2, column=1, padx=10, pady=10)
    text_label3.grid(row=3, column=1, padx=10, pady=5)
    text_label4.grid(row=4, column=1, padx=10, pady=0)

    # Initial image setup
    image = Image.open(display_hangman[6 - tries[0]])
    image = image.resize((250, 250), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    img_label = tk.Label(root, image=image)
    img_label.image = image
    img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

    def hangman_image(tries_count):
        img = Image.open(display_hangman[6 - tries_count])
        img = img.resize((250, 250), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)  # Update the label image
        img_label.image = img

    def on_submit_button_click():
        nonlocal word_completion, guessed
        guess = entry.get().lower()
        entry.delete(0, tk.END)

        if tries[0] > 0 and not guessed:
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    text_label4.config(text="You already guessed the letter")
                elif guess not in word:
                    text_label4.config(text="The letter is not in the word")
                    guessed_letters.append(guess)
                    tries[0] -= 1
                    hangman_image(tries[0])
                    text_label3.config(text=f"you have {tries[0]} tries left")
                else:
                    text_label4.config(text="The letter is in the word")
                    guessed_letters.append(guess)
                    completion_as_list = list(word_completion)
                    for i, letter in enumerate(word):
                        if letter == guess:
                            completion_as_list[i] = guess
                    word_completion = "".join(completion_as_list)
                    text_label2.config(text=f"current word: {word_completion}")
                    if "_" not in word_completion:
                        text_label4.config(text="Congratulations, you guessed the word!")
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    text_label4.config(text="You already guessed the word")
                elif guess != word:
                    text_label4.config(text="The word is not correct")
                    guessed_words.append(guess)
                    tries[0] -= 1
                    hangman_image(tries[0])
                    text_label3.config(text=f"you have {tries[0]} tries left")
                else:
                    text_label4.config(text="Congratulations, you guessed the word!")
                    guessed = True
                    word_completion = word
                    text_label2.config(text=f"current word: {word_completion}")
            else:
                text_label4.config(text="Invalid guess")
        else:
            text_label4.config(text=f"Sorry, you ran out of tries. The word was '{word}'")
            guessed = True

        if guessed or tries[0] == 0:
            submit_button.config(state=tk.DISABLED)

            if guessed:
                text_label3.config(text=f"you guessed the word, the word was: {word}")
            else:
                text_label3.config(text=f"you ran out of tries, the word was: {word}")

            text_label4.config(text=f"Do you want to play again?: ")
            yes_button = tk.Button(root, text="Yes", command=lambda: restart_game(root))
            yes_button.grid(row=5, column=0, padx=10, pady=10)
            no_button = tk.Button(root, text="No", command=root.destroy)
            no_button.grid(row=5, column=2, padx=10, pady=10)
            text_label1.grid_forget()
            text_label2.grid_forget()
            entry.grid_forget()
            submit_button.grid_forget()
            img_label.grid_forget()

    submit_button = tk.Button(root, text="Submit", command=on_submit_button_click)
    submit_button.grid(row=2, column=2, padx=10, pady=10)

    root.mainloop()


# import random
# import main
# import tkinter as tk
#
# def get_word():
#     words = ["luffy", "zoro", "brook", "goingmerry", "nami", "thousandsunny", "chopper", "franky", "robin", "usopp", "sanji",
#              "ace", "sabo", "shanks", "mihawk", "kaido", "bigmom", "blackbeard", "whitebeard", "garp", "sengoku", "akainu",
#              "kizaru", "fujitora", "ryokugyu", "smoker", "tashigi", "law", "kid", "killer", "hawkins", "apoo", "drake",
#              "bonney", "bege", "jimbei", "carrot", "kinemon", "momonosuke", "oden", "shinobu", "kawamatsu", "raizo",
#              "inuarashi", "nekomamushi", "ashura", "denjiro", "kinemon", "kanjuro", "kiku", "yamato", "shimotsuki",
#              "zorojuro", "kurozumi", "orochi", "kyoshiro", "hyogoro", "raizo", "kawamatsu", "ashura", "oden", "shinobu",
#              "kaido", "bigmom", "blackbeard", "whitebeard", "garp", "sengoku", "akainu", "kizaru", "fujitora", "ryokugyu",
#              "smoker", "tashigi", "law", "kid", "killer", "hawkins", "apoo", "drake", "bonney", "bege", "jimbei", "carrot",
#              "kinemon", "momonosuke", "oden", "shinobu", "kawamatsu", "raizo", "inuarashi", "nekomamushi", "ashura", "denjiro",
#              "kinemon", "kanjuro", "kiku", "yamato", "shimotsuki", "zorojuro", "kurozumi", "orochi", "kyoshiro", "hyogoro",
#              "raizo", "kawamatsu", "ashura", "oden", "shinobu", "kaido", "bigmom", "blackbeard", "whitebeard", "garp", "sengoku",
#              "akainu", "kizaru", "fujitor"]
#     return random.choice(words)
#
# def play(word):
#     word_completion = "_" * len(word)
#     # the following list has been taken from the internet (because I'm not an artist)
#     # source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
#     display_hangman = [
#         r'''
#         +---+
#         |   |
#         O   |
#        /|\  |
#        / \  |
#             |
#         =========''', r'''
#       +---+
#       |   |
#       O   |
#      /|\  |
#      /    |
#           |
#       =========''', r'''
#       +---+
#       |   |
#       O   |
#      /|\  |
#           |
#           |
#       =========''', r'''
#       +---+
#       |   |
#       O   |
#      /|   |
#           |
#           |
#       =========''', r'''
#       +---+
#       |   |
#       O   |
#       |   |
#           |
#           |
#       =========''', r'''
#       +---+
#       |   |
#       O   |
#           |
#           |
#           |
#       =========''', r'''
#       +---+
#       |   |
#           |
#           |
#           |
#           |
#       ========='''
#     ]
#
#     guessed = False
#     guessed_letters = []
#     guessed_words = []
#     tries = 6
#
#     print("Let's play Hangman!")
#     print(display_hangman[tries])
#     print(word_completion)
#     print("\n")
#
#     while not guessed and tries > 0:
#         guess = input("Please guess a letter or word: ").lower()
#
#         #First I check if the guessed letter is in the word (and if its a single letter)
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("You already guessed the letter ", guess)
#             elif guess not in word:
#                 print(guess, "is not in the word.")
#                 tries -= 1
#                 guessed_letters.append(guess)
#             else:
#                 print("Good job,", guess, "is in the word!")
#                 guessed_letters.append(guess)
#                 completion_as_list = list(word_completion)
#                 word_as_list = list(word)
#                 for i in range(len(word_as_list)):
#                     if word_as_list[i] == guess:
#                         completion_as_list[i] = guess
#                 word_completion = "".join(completion_as_list)
#                 if word_completion == word:
#                     guessed = True
#
#         #if the guess is longer than 1 letter, I check if the guess is the word
#         elif len(guess) == len(word) and guess.isalpha():
#             if guess in guessed_words:
#                 print("You already guessed the word", guess)
#             elif guess != word:
#                 print(guess, "is not the word.")
#                 tries -= 1
#                 guessed_words.append(guess)
#             else:
#                 guessed = True
#                 word_completion = word
#         #if the guess is not a single letter or the word, I print an error message without taking away a try
#         else:
#             print("Not a valid guess.")
#         print(display_hangman[tries])
#         print(word_completion)
#         print("\n")
#
#     if guessed:
#         print("Congratulations, you guessed the word! You win!")
#     else:
#         print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
#
#     play_again = input("Do you want to play again? (yes or no) ").lower()
#     if play_again == "yes" or play_again == "y":
#         play(get_word())
#     else:
#         print("Thanks for playing!")
#         main.menu()




