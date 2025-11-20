import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps

    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "BREAK", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text = "BREAK", fg=PINK)
    
    else:
        count_down(work_sec)
        timer_label.config(text = "WORK", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for x in range (work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Timer")
window.config(padx=200, pady=100, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photoimage = tkinter.PhotoImage(file="./Day 28/tomato.png")
canvas.create_image(100, 112, image=photoimage)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, "35", "bold"))
canvas.grid(column=1, row=2)


timer_label = tkinter.Label(text="TIMER",bg=YELLOW, fg=GREEN, font=(FONT_NAME, "50"), highlightthickness=0)
timer_label.grid(column=1, row=1)

button_1 = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_1.grid(column=0, row=3)

button_2 = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_2.grid(column=2, row=3)

checkmark_label = tkinter.Label(bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmark_label.grid(column=1, row=4, padx=10, pady=10)


window.mainloop()