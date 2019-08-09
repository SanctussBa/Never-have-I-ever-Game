from tkinter import *
import random
import os
import sys

window = Tk()
window.title("Never Have I Ever Game")
window.geometry("700x400")
window.config(bg="#FBE5B3")
window.iconbitmap("icon.ico")

label_front = Label(window, text="Welcome, This is 'Never Have I Ever Game'", bg="#FBE5B3", font=("Helvetica", 20))
label_front.pack(side=TOP)

label_down = Label(window, text="Please choose, who is Player 1 and Player 2", bg="#FBE5B3")
label_down.pack(side=BOTTOM)

photo = PhotoImage(file="face1.gif")
label_pic = Label(window, image=photo)
label_pic.pack()

score_p1 = 0
score_p2 = 0
counter = 0

def no():
    window.destroy()


def again():
    global counter, score_p1, score_p2

    counter = 0
    score_p2 = 0
    score_p1 = 0
    ask_again.pack_forget()
    winner_label.pack_forget()
    yes_b.pack_forget()
    no_b.pack_forget()
    next_window()
    
def results():
    global counter, score_p1, score_p2
    label_front.config(text=f"You had {counter} questions.\n Player 1 got {score_p1} points.\n \
    Player 2 got {score_p2} points.")

    if score_p1 > score_p2:
        winner_label.config(text="Player 1 won! Congratulations!")
        winner_label.pack()
    elif score_p2 > score_p1:
        winner_label.pack()
    else:
        winner_label.config(text="You both are Equals. It's a tie!")
        winner_label.pack()
    
    ask_again.pack()
    yes_b.pack()
    no_b.pack()


def both():
    text()
    global score_p1, score_p2, counter
    score_p1 += 1
    score_p2 += 1
    counter += 1
    b_both.config(command=both)
    if counter >= 10:
        b_p2.pack_forget()
        b_p1.pack_forget()
        b_both.pack_forget()
        b_none.pack_forget()
        results()


def none():
    text()
    global counter
    counter += 1
    b_none.config(command=none)
    if counter >= 10:
        b_p2.pack_forget()
        b_p1.pack_forget()
        b_both.pack_forget()
        b_none.pack_forget()
        results()


def player_one():
    text()
    global score_p1, counter
    score_p1 += 1
    counter += 1
    b_p1.config(command=player_one)
    if counter >= 10:
        b_p2.pack_forget()
        b_p1.pack_forget()
        b_both.pack_forget()
        b_none.pack_forget()
        results()


def player_two():
    text()
    global score_p2, counter
    score_p2 += 1
    counter += 1
    b_p2.config(command=player_two)
    if counter >= 10:
        b_p2.pack_forget()
        b_p1.pack_forget()
        b_both.pack_forget()
        b_none.pack_forget()
        results()


def text():
    with open("never.txt", 'rb') as file:
        file = file.read().splitlines()


    line = random.choice(file)
    label_front.config(text=line)


def next_window():
    label_front.config(command=text())
    label_pic.destroy()
    label_down.destroy()
    button_start.destroy()
    b_both.config(command=both)
    b_none.config(command=none)
    b_p1.config(command=player_one)
    b_p2.config(command=player_two)
    b_both.pack(side="bottom")
    b_none.pack(side="bottom")
    b_p1.pack(side="bottom")
    b_p2.pack(side="bottom")


button_start = Button(window, text="Start Game", padx=50, pady=20, bg="#FBE5B3", font=("Helvetica", 30),\
                      command=next_window)
button_start.pack()

b_both = Button(window, text="Both", padx=30, pady=10, bg="#E2A9F3", font=("Helvetica", 12))
b_none = Button(window, text="None", padx=30, pady=10, bg="#E2A9F3", font=("Helvetica", 12))
b_p1 = Button(window, text="Player 1", padx=30, pady=10, bg="#E2A9F3", font=("Helvetica", 12))
b_p2 = Button(window, text="Player 2", padx=30, pady=10, bg="#E2A9F3", font=("Helvetica", 12))
ask_again = Label(window, text="Would you like to play again?",bg="#FBE5B3", font=("Helvetica", 20))
winner_label = Label(window, text="Player 2 won! Congratulations!", bg="#FBE5B3", font=("Helvetica", 30))
yes_b = Button(window, text="Yes", command=again, bg="green", fg="yellow", padx=20, pady=8, font=("Helvetica", 20))
no_b = Button(window, text="No", command=no, bg="red", fg="yellow", padx=20, pady=8, font=("Helvetica", 20))

window.mainloop()

