import random
import main
import tkinter as tk

def get_word():
    words = ["luffy", "zoro", "brook", "goingmerry", "nami", "thousandsunny", "chopper", "franky", "robin", "usopp", "sanji",
             "ace", "sabo", "shanks", "mihawk", "kaido", "bigmom", "blackbeard", "whitebeard", "garp", "sengoku", "akainu",
             "kizaru", "fujitora", "ryokugyu", "smoker", "tashigi", "law", "kid", "killer", "hawkins", "apoo", "drake",
             "bonney", "bege", "jimbei", "carrot", "kinemon", "momonosuke", "oden", "shinobu", "kawamatsu", "raizo",
             "inuarashi", "nekomamushi", "ashura", "denjiro", "kinemon", "kanjuro", "kiku", "yamato", "shimotsuki",
             "zorojuro", "kurozumi", "orochi", "kyoshiro", "hyogoro", "raizo", "kawamatsu", "ashura", "oden", "shinobu",
             "kaido", "bigmom", "blackbeard", "whitebeard", "garp", "sengoku", "akainu", "kizaru", "fujitora", "ryokugyu",
             "smoker", "tashigi", "law", "kid", "killer", "hawkins", "apoo", "drake", "bonney", "bege", "jimbei", "carrot",
             "kinemon", "momonosuke", "oden", "shinobu", "kawamatsu", "raizo", "inuarashi", "nekomamushi", "ashura", "denjiro",
             "kinemon", "kanjuro", "kiku", "yamato", "shimotsuki", "zorojuro", "kurozumi", "orochi", "kyoshiro", "hyogoro",
             "raizo", "kawamatsu", "ashura", "oden", "shinobu", "kaido", "bigmom", "blackbeard", "whitebeard", "garp", "sengoku",
             "akainu", "kizaru", "fujitor"]
    return random.choice(words)

def play(word):
    word_completion = "_" * len(word)
    # the following list has been taken from the internet (because I'm not an artist)
    # source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
    display_hangman = [
        r'''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
      =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
      =========''', r'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
      =========''', r'''
      +---+
      |   |
      O   |
      |   |
          |
          |
      =========''', r'''
      +---+
      |   |
      O   |
          |
          |
          |
      =========''', r'''
      +---+
      |   |
          |
          |
          |
          |
      ========='''
    ]

    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman[tries])
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        #First I check if the guessed letter is in the word (and if its a single letter)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter ", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                completion_as_list = list(word_completion)
                word_as_list = list(word)
                for i in range(len(word_as_list)):
                    if word_as_list[i] == guess:
                        completion_as_list[i] = guess
                word_completion = "".join(completion_as_list)
                if word_completion == word:
                    guessed = True

        #if the guess is longer than 1 letter, I check if the guess is the word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        #if the guess is not a single letter or the word, I print an error message without taking away a try
        else:
            print("Not a valid guess.")
        print(display_hangman[tries])
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

    play_again = input("Do you want to play again? (yes or no) ").lower()
    if play_again == "yes" or play_again == "y":
        play(get_word())
    else:
        print("Thanks for playing!")
        main.menu()




