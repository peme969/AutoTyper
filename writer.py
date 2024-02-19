import time
import pyautogui
import tkinter as tk
from tkinter import simpledialog, messagebox

def get_input():
    user_input = simpledialog.askstring("Text Input", "Enter the text to write:")
    return user_input

def write_sentence(sentence):
    for char in sentence:
        pyautogui.typewrite(char)
        time.sleep(0.000001)

def write():
    user_input = get_input()
    
    if not user_input:
        messagebox.showwarning("No Text", "You didn't enter any text.")
        return

    time.sleep(3)
    write_sentence(user_input)
    result_window = tk.Tk()
    result_window.title("Text Wrote!")

    text_box = tk.Text(result_window, height=1, width=20, bg="green", fg="white")
    text_box.insert(tk.END, "Finished Writing Text!")
    text_box.config(state=tk.DISABLED)
    text_box.pack(pady=20)

    checkmark_label = tk.Label(result_window, text="✔", font=("Helvetica", 24), fg="green")
    checkmark_label.pack()

    result_window.after(3000, result_window.destroy)

def on_button_click():
    write()

root = tk.Tk()
root.title("Text Writer")
root.geometry("300x300")

paste_button = tk.Button(root, text="Write Now", command=on_button_click, bg="blue", fg="white", font=("Helvetica", 16))
paste_button.config(highlightthickness=4, highlightbackground="blue")
paste_button.bind("<Enter>", lambda event: paste_button.config(bg="lightblue"))
paste_button.bind("<Leave>", lambda event: paste_button.config(bg="blue"))
paste_button.pack(pady=50)

root.mainloop()
