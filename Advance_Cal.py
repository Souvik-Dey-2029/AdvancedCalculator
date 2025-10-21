import tkinter as tk
import math

# Global expression
expression = ""

# Update display
def click(event):
    global expression
    expression += event.widget.cget("text")
    input_text.set(expression)

def evaluate(event=None):
    global expression
    try:
        # Handle percentage %
        if "%" in expression:
            expression_eval = expression.replace("%", "/100")
            result = str(eval(expression_eval))
        else:
            result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def clear(event=None):
    global expression
    expression = ""
    input_text.set("")

def sqrt_func():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")
root.configure(bg="#222")  # Dark background

expression = ""
input_text = tk.StringVar()

# Display entry
entry = tk.Entry(root, textvar=input_text, font="Arial 24", bd=5, relief="sunken",
                 justify="right", bg="#333", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
entry.bind("<Return>", evaluate)  # Press Enter to calculate
entry.focus()

# Buttons layout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','%','+']
]

# Create number/operator buttons
for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font="Arial 18", bd=2, bg="#444", fg="white")
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", click)
        # Hover effect
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#666"))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#444"))

# Equal button
equal_btn = tk.Button(root, text="=", font="Arial 18", bd=2, bg="#0a7", fg="white")
equal_btn.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
equal_btn.bind("<Button-1>", evaluate)

# Clear button
clear_btn = tk.Button(root, text="C", font="Arial 18", bd=2, bg="#f33", fg="white")
clear_btn.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)
clear_btn.bind("<Button-1>", clear)

# Square root button
sqrt_btn = tk.Button(root, text="√", font="Arial 18", bd=2, bg="#fa0", fg="white", command=sqrt_func)
sqrt_btn.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

# Make grid expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Keyboard support
root.bind("<Return>", evaluate)   # Enter key
root.bind("<BackSpace>", lambda e: input_text.set(expression[:-1]))  # Backspace

root.mainloop()