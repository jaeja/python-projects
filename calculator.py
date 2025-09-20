import tkinter as tk
master= tk.Tk()
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("calculator")
        master.geometry("300x400")
        self.expression = ""
        self.text_input = tk.StringVar()
        self.create_widgets()
        master.mainloop()

    def create_widgets(self):
        entry = tk.Entry(self.master, textvariable=self.text_input, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.master, text=button, padx=20, pady=20, font=('arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif char == 'C':
            self.expression = ""
        else:
            self.expression += str(char)
        self.text_input.set(self.expression)

Calculator( master)
