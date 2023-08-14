from tkinter import *
import datetime as dtt
import text_options
import random

FONT = ("Helvetica", 10)
DISABLED_BG = '#f0f0f0'
DEFAULT_TXT = 'Text will appear as soon as you hit "Start"'\
              "(so that you don't cheat by memorizing/practicing first)."

start_time = None

text_to_display = None


def start_timer():
    global start_time, text_to_display
    text_to_display = random.choice(text_options.text_strings)
    wpm_count_label.config(text="Words per minute:", fg='black')
    canvas.config(bg='white')
    canvas.itemconfig(message, text=text_to_display)
    stop_button.config(state=NORMAL)
    start_time = dtt.datetime.now()
    user_entry.config(state=NORMAL, bg='white')
    user_entry.focus()


def stop_timer():
    global start_time
    stop_time = dtt.datetime.now()
    time_difference = stop_time - start_time
    char_count = len(user_entry.get(1.0, END))
    if char_count < len(text_to_display):
        wpm_count_label.config(text='Please finish typing the sentence before clicking on "Stop".', fg='red')
        stop_button.config(state=DISABLED)
        canvas.itemconfig(message, text=DEFAULT_TXT)
        canvas.config(bg=DISABLED_BG)
    else:
        # The "char_count" is the number of characters you type per minute, without including any mistakes.
        # "words_per_minute" is the "char_count" divided by 5. That's a de facto international standard.
        words_per_minute = round((char_count / 5) / (time_difference.seconds / 60))
        wpm_count_label.config(text=f'Words per minute: {words_per_minute}')
    user_entry.config(state=DISABLED, bg=DISABLED_BG)


window = Tk()
window.title("PyType - Typing Speed Test")
window.geometry("600x420")
window.resizable(False, False)

app_name = Label(text="PyType", font=("Helvetica", 30, "bold"), pady=10)
app_name.pack()

description_label = Label(text='To measure your typing speed, please click on "Start" and type the text you see '
                               'onscreen', font=FONT, anchor='w')
description_label.pack(padx=(0, 22))

canvas = Canvas(width=550, height=150, bg=DISABLED_BG, highlightthickness=1, highlightbackground="gray")
message = canvas.create_text(10, 10,
                             text=DEFAULT_TXT,
                             font=('Arial', 14), anchor='nw', justify='left', width=530)
canvas.pack(pady=(10, 0))

type_label = Label(text="Type your text below:", font=FONT)
type_label.pack(anchor='w', padx=85, pady=(10, 0))

user_entry = Text(width=60, height=2, bg=DISABLED_BG, font=FONT)
user_entry.config(state=DISABLED)
user_entry.pack(pady=(10, 0))

button_frame = Frame(window)
button_frame.pack()

start_button = Button(button_frame, text="Start", command=start_timer, width=20, font=FONT)
start_button.pack(side='left', padx=(87, 10), pady=(10, 0))

stop_button = Button(button_frame, text='Stop', command=stop_timer, width=20, font=FONT)
stop_button.pack(side='right', padx=(10, 87), pady=(10, 0))
stop_button.config(state=DISABLED)

wpm_count_label = Label(window, text="Words per minute:", font=('Helvetica', 10, 'bold'))
wpm_count_label.pack(anchor='w', pady=(12, 0), padx=20)

window.mainloop()
