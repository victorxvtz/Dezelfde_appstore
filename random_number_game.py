import random
# import main
import tkinter as tk

def play() :
    root = tk.Toplevel()
    root.title("Random Number Game")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 20

    #sorry the messy code, tkinter is just not nice to keeping code clean

    text_label1 = tk.Label(root, text="Welcome to the number guessing game!")
    text_label2 = tk.Label(root, text="I'm thinking of a number between 1 and 100")
    text_label3 = tk.Label(root, text="Try to guess the number in as few attempts as possible")
    text_label4 = tk.Label(root, text=f"You get {max_attempts - attempts} attempts")
    text_label5 = tk.Label(root, text="")
    text_label1.pack()
    text_label2.pack()
    text_label3.pack()
    text_label4.pack()
    text_label5.pack()

    entry = tk.Entry(root)
    entry.pack()

    def on_submit_button_click():
        nonlocal text_label5
        # Checks if the input is a number and extracts it
        try:
            guess = int(entry.get())
        except ValueError:
            text_label5.config(text="Please enter a valid number.")
            return

        nonlocal attempts
        attempts += 1
        # Checks if the guess is too low, too high
        if guess < number:
            text_label5.config(text="Too low")
            entry.delete(0, tk.END)  # Clear the input field for the next guess

        elif guess > number:
            text_label5.config(text="Too high")
            entry.delete(0, tk.END)  # Clear the input field for the next guess

        # when the user goes over the max attempts
        elif attempts >= max_attempts:
            # The labels for the game are changed to show the user the game is over
            text_label5.config(text="You have reached the maximum number of attempts")
            text_label6 = tk.Label(root, text=f"The number was {number}")
            text_label6.pack()
            text_label7 = tk.Label(root, text="Do you want to play again?: ")
            text_label7.pack()
            yes_button = tk.Button(root, text="Yes", command= lambda: restart_game(root))
            yes_button.pack()
            no_button = tk.Button(root, text="No", command=root.destroy)
            no_button.pack()

            # The labels for the game are removed, to make space for the new labels and give a better view
            text_label1.pack_forget()
            text_label2.pack_forget()
            text_label3.pack_forget()
            text_label4.pack_forget()
            entry.pack_forget()
            button.pack_forget()
        # If the user doesn't get caught by the above if statements, the user guessed the number
        else:
            # The labels for the game are changed to show the user they guessed the number
            text_label5.config(text=f"Congratulations! You guessed the number in {attempts} attempts")
            text_label7 = tk.Label(root, text="Do you want to play again?: ")
            text_label7.pack()
            yes_button = tk.Button(root, text="Yes", command= lambda: restart_game(root))
            yes_button.pack()
            no_button = tk.Button(root, text="No", command=root.destroy)
            no_button.pack()
            # The labels for the game are removed, to make space for the new labels and give a better view (again)
            text_label1.pack_forget()
            text_label2.pack_forget()
            text_label3.pack_forget()
            text_label4.pack_forget()
            entry.pack_forget()
            button.pack_forget()


    button = tk.Button(root, text="Submit", command=on_submit_button_click)
    button.pack()

    root.mainloop()

def restart_game(root):
    root.destroy()
    play()




# def play():
#     print("Welcome to the number guessing game!")
#     print("I'm thinking of a number between 1 and 100")
#     print("Try to guess the number in as few attempts as possible")
#
#     number = random.randint(1, 100)
#     attempts = 0
#     max_attempts = 20
#
#     print(f"you get {max_attempts} attempts")
#
#
#     while True:
#         guess = int(input("Enter your guess: "))
#         attempts += 1
#         if guess < number:
#             print("Too low")
#         elif guess > number:
#             print("Too high")
#         elif attempts >= max_attempts:
#             print("You have reached the maximum number of attempts")
#             print("The number was", number)
#             break
#         else:
#             print("Congratulations! You guessed the number in", attempts, "attempts")
#             break
#
#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again == "yes" or play_again == "y":
#         play()
#     else:
#         print("Thanks for playing!")
#         main.menu()
