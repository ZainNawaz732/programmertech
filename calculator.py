import tkinter as tk

def on_button_click(event):
    num = event.widget['text']
    if num == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "error")
    elif num == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, num)

root = tk.Tk()
root.title("Calculator")
root.geometry("500x300")
entry = tk.Entry(root, font=("Verdana", 25))
entry.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "+", "=",
]

row = 0
col = 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 20))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
    button.bind("<Button-1>", on_button_click)

root.mainloop()