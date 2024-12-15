import tkinter as tk
import math

# Constants
WORK = 25 * 60  # Duration of work in seconds
SHORT_BREAK = 5 * 60  # Duration of a short break in seconds
LONG_BREAK = 20 * 60  # Duration of a long break in seconds
SESSIONS_BEFORE_LONG_BREAK = 4  # Number of work sessions before a long break

# Variables
repitition = 0  # Number of completed work sessions
timer = None


def reset_timer():
    global repitition, timer
    repitition = 0
    if timer:
        root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    check_marks.config(text="")
    start_button["state"] = "normal"


def start_timer():
    start_button["state"] = "disabled"
    global repitition
    if repitition % SESSIONS_BEFORE_LONG_BREAK == 0 and repitition != 0:
        count_down(LONG_BREAK)
    else:
        count_down(WORK)


def switch_to_break():
    global repitition
    repitition += 1
    marks = "✓" * (repitition // 2)
    check_marks.config(text=marks)
    if repitition % SESSIONS_BEFORE_LONG_BREAK == 0:
        count_down(LONG_BREAK)
    else:
        count_down(SHORT_BREAK)


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        if repitition % 2 != 0 or repitition == 0:
            switch_to_break()
        else:
            start_timer()


root = tk.Tk()
root.title("Hiruys POMODORO")
root.config(padx=100, pady=50, bg="#f7f5dd")

title_label = tk.Label(text="TIMER", fg='#A020f0', bg='#f7f5dd', font=("Arial", 50))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, highlightthickness=0, bg="#f7f5dd")
# tomato_img = tk.PhotoImage(file="tomato.png")  # Ensure you have a 'tomato.png' image in the same directory as your script
# canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="black", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer, bg="#e7305b", font=("Arial", 15, "bold"))
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer, bg="#e7305b", font=("Arial", 15, "bold"))
reset_button.grid(column=2, row=2)

check_marks = tk.Label(text="", fg='#00FF00', bg="#f7f5dd", font=("Arial", 25, "bold"))
check_marks.grid(column=1, row=3)

root.mainloop()
