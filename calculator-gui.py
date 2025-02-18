import tkinter as tk

# Function to handle button clicks
def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# GUI Setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Button Layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: on_click(t), width=5, height=2).grid(row=r, column=c)

root.mainloop()
