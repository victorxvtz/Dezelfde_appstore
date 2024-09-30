import random
import math
import tkinter as tk

def startup_game():
    math_quiz_window = tk.Toplevel()
    math_quiz_window.title("Math Quiz")

    text_label1 = tk.Label(math_quiz_window, text="Welcome to the math quiz!")
    text_label2 = tk.Label(math_quiz_window, text="How many questions would you like to answer?")
    text_label1.pack()
    text_label2.pack()

    entry = tk.Entry(math_quiz_window)
    entry.pack()

    def on_submit_button_click():
        game_length = int(entry.get())
        play(game_length)
        math_quiz_window.destroy()

    button = tk.Button(math_quiz_window, text="Submit", command=on_submit_button_click)
    button.pack()

    math_quiz_window.mainloop()

def play(game_length):
    math_problem = ""

    root = tk.Tk()
    root.title("Math Quiz")
    print("Welcome to the math quiz!")

    text_label1 = tk.Label(root, text="Let's play the math quiz!")
    text_label2 = tk.Label(root, text=f"Answer {game_length} questions")
    text_label1.pack()
    text_label2.pack()

    score = 0
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
            answer = a / b

        math_problem = f"{a} {operator} {b} = "
        text_label3 = tk.Label(root, text=math_problem)
        text_label3.pack()

        entry = tk.Entry(root)
        entry.pack()

        def on_submit_button_click():
            user_answer = float(entry.get())
            nonlocal score
            if user_answer == answer:
                score += 1
                text_label4 = tk.Label(root, text="Correct!")
                text_label4.pack()
            else:
                text_label4 = tk.Label(root, text="Incorrect!")
                text_label4.pack()

        button = tk.Button(root, text="Submit", command=on_submit_button_click)
        button.pack()

    text_label5 = tk.Label(root, text=f"You got {score} out of {game_length}")
    text_label5.pack()





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

