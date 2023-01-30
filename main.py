import tkinter as tk
from english_words import all_words
import time


# ---------- FUNCTIONS ---------- #

def start_timer():
    window.config(bg="black")
    words_label.config(bg="black", fg="lightgrey")
    timer_label.config(bg="black")
    start_button.destroy()
    add_second()


def add_second():
    global seconds_passed
    seconds_passed += 1
    timer_label.configure(text=f'{seconds_passed}')

    # call this function again after one second if the time is not over.
    window.after(1000, add_second)
    window.after(60000, check_typing_speed)


def check_typing_speed():
    time.sleep(1)
    text_input = textbox.get(1.0, "end")
    text = text_input.split()
    words = words_split
    correct = []
    incorrect = []
    for pos in range(len(text)):
        if text[pos] != words[pos]:
            incorrect.append(f"{words[pos]}: {text[pos]}")
        else:
            correct.append(words[pos])

    window.destroy()
    print(f"Great job! You have a speed of {len(correct)}wpm. Your raw speed is {len(text)}wpm.")
    print(f"Incorrect words: {incorrect}")


# ---------- GUI ---------- #

# window
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry('575x360')
window.configure(bg="white")

# words
words_split = all_words.split()
words_text = ""
for word in range(0, 100):
    if word % 10 == 0 and word != 0:
        words_text += f"{words_split[word]} \n"
    else:
        words_text += f"{words_split[word]} "

words_label = tk.Label(window, text=words_text, font=('Arial', 14), bg="lightpink")
words_label.pack(padx=10, pady=10)

# timer
seconds_passed = 0
timer_label = tk.Label(window, text=seconds_passed, font=('Arial', 24), bg="white", fg="lightgreen")
timer_label.pack()

# start
start_button = tk.Button(window, width=7, text="Start", fg="lightgreen", command=start_timer)
start_button.pack()

# text box
textbox = tk.Text(window, height=2, font=('Arial', 12), bg="white")
textbox.pack(padx=10, pady=10)

window.mainloop()
