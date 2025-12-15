import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("PYTHON MINI PROJECT")
root.geometry("500x500")
root.config(bg="#ffce1b")
heading = Label(root, text="PYTHON MINI PROJECT", font=("Arial", 30, "bold"),fg="#7f58af",bg="#ffce1b")
heading.pack(pady=20)



def rock_paper_scissor():
    def game(user_choice):
        computer_choice = random.choice(["rock", "paper", "scissor"])

        if user_choice == computer_choice:
            result = "Match die!"
        elif user_choice == "rock" and computer_choice == "scissor":
            result = "You won"
        elif user_choice == "paper" and computer_choice == "rock":
            result = "You won"
        elif user_choice == "scissor" and computer_choice == "rock":
            result = "You won"
        else:
            result = "You lost"
        messagebox.showinfo("Result", f"You choice:{user_choice}\ncomputer choice:{computer_choice}\nresult:{result}")

    inner_screen = tk.Toplevel(root)
    inner_screen.config(bg="#ffb16e")
    inner_screen.title("rock paper scissor")
    inner_screen.geometry("300x300")
    k = tk.Label(inner_screen, text="choose One", font=("Arial", 18))
    k.config(font=("Baskerville Old Face",30,"bold"),bg="#ffb16e")
    k.pack()



    button_1 = tk.Button(inner_screen, text="Rock", width=20, command=lambda: game("rock"))
    button_1.config(font=("Arial",10,"bold"),bg="#fff588")
    button_1.pack(pady=15)
    button_2 = tk.Button(inner_screen, text="Paper", width=20, command=lambda: game("paper"))
    button_2.config(font=("Arial", 10, "bold"), bg="#fff588")
    button_2.pack(pady=15)
    button_3 = tk.Button(inner_screen, text="Scissor", width=20, command=lambda: game("Scissor"))
    button_3.config(font=("Arial", 10, "bold"), bg="#fff588")
    button_3.pack(pady=15)





def dice_roll_simulator():
    from turtle import Turtle, Screen
    import random

    def dice():  # creating the red dots to be displayed
        roll.speed(0)
        roll.begin_fill()
        roll.circle(10)
        roll.color("red")
        roll.end_fill()
        roll.hideturtle()

    def main(positions_list):
        for positions in positions_list:
            roll.penup()
            roll.goto(positions)
            roll.pendown()
            dice()
            roll.hideturtle()

    roll = Turtle()  # creating the turtle and setting up the screen
    roll.color("red")
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(height=300, width=300)

    border_pen = Turtle()  # creating the border for the turtle
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.pensize(5)
    border_pen.up()
    border_pen.goto(-100, -100)
    for i in range(4):
        border_pen.down()
        border_pen.forward(200)
        border_pen.left(90)
        border_pen.up()
        border_pen.hideturtle()

    dice_number = random.randint(1, 6)
    if dice_number == 1:
        POSITIONS = [(0, 0)]
        main(POSITIONS)

    elif dice_number == 2:
        POSITIONS = [(-60, -60), (60, 60)]
        main(POSITIONS)

    elif dice_number == 3:
        POSITIONS = [(-60, -60), (0, 0), (60, 60)]
        main(POSITIONS)

    elif dice_number == 4:
        POSITIONS = [(-60, -60), (60, -60), (-60, 60), (60, 60)]
        main(POSITIONS)

    elif dice_number == 5:
        POSITIONS = [(-60, -60), (60, -60), (0, 0), (-60, 60), (60, 60)]
        main(POSITIONS)
    elif dice_number == 6:
        POSITIONS = [(-60, -60), (60, -60), (-60, 0), (60, 0), (-60, 60), (60, 60)]
        main(POSITIONS)

    screen.exitonclick()

def number_guessing_game():
    number = random.randint(1, 100)
    attempt = 5

    def check_guess():
        nonlocal attempt
        guess = int(entry.get())
        attempt -= 1

        if guess == number:
            messagebox.showinfo("Result", " Correct! You won!")
            root.destroy()
        elif attempt == 0:
            messagebox.showinfo("Result", f" You lost! Number was {number}")
            root.destroy()
        elif guess < number:
            label_result.config(text=f"Too Low! Attempts left: {attempt}")
        else:
            label_result.config(text=f"Too High! Attempts left: {attempt}")

    root = tk.Tk()
    root.title("Number Guessing Game")
    root.config(bg="#fffacd")

    root.geometry("300x250")

    k = tk.Label(root, text="Guess a number (1–100)", font=("Arial", 12))
    k.config(font=("Arial", 15, "bold"), bg="#fffacd", fg="#3d8d7a")

    k.pack(pady=10)


    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Check Guess", command=check_guess)
    button.config(font=("Arial", 15, "bold"),bg="#f9ddd2")
    button.pack(pady=10)

    label_result = tk.Label(root, text=f"Attempts left: {attempt}")
    label_result.config(font=("Arial", 15, "bold"),fg="#cbbd93")
    label_result.pack()


button1 = Button(root, text="rock paper scissor", width=25, command=rock_paper_scissor)
button1.config(font=("Arial",15,"bold"),bg="#93b1b5",fg="#0b2e33")
button1.pack(pady=40)
button2 = Button(root,text="Number guessing game",width=25,command=number_guessing_game)
button2.config(font=("Arial",15,"bold"),bg="#93b1b5",fg="#0b2e33")
button2.pack(pady=0)
button3 = Button(root, text="dice roll simulator", width=25, command=dice_roll_simulator)
button3.config(font=("Arial",15,"bold"),bg="#93b1b5",fg="#0b2e33")
button3.pack(pady=40)
exit_button = Button(root,text="Exit",width=25,command=root.destroy)
exit_button.config(font=("Arial",15,"bold"),bg="#93b1b5",fg="#0b2e33")
exit_button.pack()

root.mainloop()
