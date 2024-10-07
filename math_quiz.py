import random
import tkinter as tk

def startup_game():
    math_quiz_window = tk.Toplevel()
    math_quiz_window.title("Math Quiz")

    # Labels and entry for number of questions
    text_label1 = tk.Label(math_quiz_window, text="Welcome to the math quiz!")
    text_label2 = tk.Label(math_quiz_window, text="How many questions would you like to answer?")
    text_label1.pack()
    text_label2.pack()

    entry = tk.Entry(math_quiz_window)
    entry.pack()

    # Start the quiz with the specified number of questions
    def on_submit_button_click():
        game_length = int(entry.get())
        math_quiz_window.destroy()
        play(game_length)

    button = tk.Button(math_quiz_window, text="Submit", command=on_submit_button_click)
    button.pack()

    math_quiz_window.mainloop()

def restart_game(root):
    root.destroy()
    startup_game()

def play(game_length):
    # Store the math problems and answers
    math_problems = []
    answers = []
    iteration = 0
    score = 0

    # Generate math problems and corresponding answers
    for i in range(game_length):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])
        if operator == "+":
            answer = a + b
        elif operator == "-":
            answer = a - b
        elif operator == "*":
            answer = a * b
        elif operator == "/":
            answer = round(a / b, 2)  # rounding division results to 2 decimal places

        problem = f"{a} {operator} {b} = "
        math_problems.append(problem)
        answers.append(answer)

    # Create the quiz window
    root = tk.Toplevel()
    root.title("Math Quiz")

    # Display initial problem
    text_label1 = tk.Label(root, text="Let's play the math quiz!")
    text_label1.pack()

    question_label = tk.Label(root, text=math_problems[iteration])
    question_label.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    entry = tk.Entry(root)
    entry.pack()

    # Function to handle submission of each answer
    def on_submit_button_click():
        nonlocal iteration
        nonlocal score
        nonlocal result_label
        nonlocal question_label

        try:
            user_answer = float(entry.get())
        except ValueError:
            result_label.config(text="Please enter a valid number.")
            return

        # Check if the user's answer is correct
        if user_answer == answers[iteration]:
            score += 1
            result_label.config(text="Correct!")
        else:
            result_label.config(text=f"Incorrect! Correct answer: {answers[iteration]}")

        iteration += 1

        # Move to the next question or show the final score
        if iteration < game_length:
            question_label.config(text=math_problems[iteration])
            entry.delete(0, tk.END)  # Clear the input field for the next question
        else:
            question_label.config(text=f"You got {score} out of {game_length} correct!")
            entry.pack_forget()  # Remove entry field once quiz is over
            submit_button.pack_forget()  # Remove submit button once quiz is over
            # Ask user if they want to play again
            play_again_label = tk.Label(root, text="Would you like to play again?")
            play_again_label.pack()
            play_again_button = tk.Button(root, text="Play Again", command=lambda: restart_game(root))
            play_again_button.pack()
            quit_button = tk.Button(root, text="Quit", command=root.destroy)
            quit_button.pack()


    # Button to submit the answer
    submit_button = tk.Button(root, text="Submit", command=on_submit_button_click)
    submit_button.pack()

    root.mainloop()


# import random
# import math
# import tkinter as tk
#
# def startup_game():
#     math_quiz_window = tk.Toplevel()
#     math_quiz_window.title("Math Quiz")
#
#     text_label1 = tk.Label(math_quiz_window, text="Welcome to the math quiz!")
#     text_label2 = tk.Label(math_quiz_window, text="How many questions would you like to answer?")
#     text_label1.pack()
#     text_label2.pack()
#
#     entry = tk.Entry(math_quiz_window)
#     entry.pack()
#
#     def on_submit_button_click():
#         game_length = int(entry.get())
#         play(game_length)
#         math_quiz_window.destroy()
#
#     button = tk.Button(math_quiz_window, text="Submit", command=on_submit_button_click)
#     button.pack()
#
#     math_quiz_window.mainloop()
#
# def play(game_length):
#     math_problem = []
#     answers = []
#     iteration = 0
#
#     root = tk.Toplevel()
#     root.title("Math Quiz")
#     print("Welcome to the math quiz!")
#
#     text_label1 = tk.Label(root, text="Let's play the math quiz!")
#     text_label2 = tk.Label(root, text=f"Answer {game_length} questions")
#     text_label1.pack()
#     text_label2.pack()
#
#     score = 0
#     for i in range(game_length):
#         a = random.randint(1, 10)
#         b = random.randint(1, 10)
#         operator = random.choice(["+", "-", "*", "/"])
#         if operator == "+":
#             answer = a + b
#         elif operator == "-":
#             answer = a - b
#         elif operator == "*":
#             answer = a * b
#         elif operator == "/":
#             answer = a / b
#
#         math_problem = [f"{a} {operator} {b} = "]
#         answers = [answer]
#     text_label3 = tk.Label(root, text=math_problem[iteration])
#     text_label3.pack()
#
#     text_label4 = tk.Label(root, text="")
#     text_label4.pack()
#
#     entry = tk.Entry(root)
#     entry.pack()
#
#     def on_submit_button_click(answers):
#         user_answer = entry.get()
#         float(user_answer)
#         nonlocal score
#         nonlocal iteration
#         nonlocal text_label4
#         if user_answer == answers[iteration]:
#             score += 1
#             text_label4 = tk.Label(root, text="Correct!")
#         else:
#             text_label4 = tk.Label(root, text="Incorrect!")
#         iteration += 1
#
#     button = tk.Button(root, text="Submit", command= lambda : on_submit_button_click(answers))
#     button.pack()
#
#     text_label5 = tk.Label(root, text=f"You got {score} out of {game_length}")
#     text_label5.pack()





    #the following code should be translated to tkinter code
    # score = 0
    # game_length = int(input("how many questions would you like to answer? "))
    # for i in range(game_length):
    #     a = random.randint(1, 10)
    #     b = random.randint(1, 10)
    #     operator = random.choice(["+", "-", "*", "/"]) #, "to the power of" ,"log" | technically usable but very hard to answer correctly so temporarily removed
    #     if operator == "+":
    #         answer = a + b
    #     elif operator == "-":
    #         answer = a - b
    #     elif operator == "*":
    #         answer = a * b
    #     elif operator == "/":
    #         answer = a / b
    #     # elif operator == "to the power of":
    #     #     answer = math.pow(a,b)
    #     # elif operator == "log":
    #     #     answer = math.log(a,b)
    #
    #     user_answer = float(input(f"{a} {operator} {b} = "))
    #     if user_answer == answer:
    #         score += 1
    #         print("Correct!")
    #     else:
    #         print("Incorrect!")
    # print("You got", score, "out of ", game_length)

    # play_again = input("Do you want to play again? (yes/no): ").lower()
    # if play_again == "yes" or play_again == "y":
    #     play()
    # else:
    #     print("Thanks for playing!")
    #     main.menu()

