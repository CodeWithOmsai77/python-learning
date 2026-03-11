# calc_gui.py
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("260x320")
        self.resizable(False, False)

        self.expr = ""
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.pack(fill="both", padx=8, pady=8, ipady=8)

        btns = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+'],
            ['C','%','//','**']
        ]
        for row in btns:
            frame = tk.Frame(self)
            frame.pack(expand=True, fill="both")
            for label in row:
                b = tk.Button(frame, text=label, font=("Arial", 16),
                              command=lambda t=label: self.on_click(t))
                b.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_click(self, key):
        if key == 'C':
            self.expr = ""
            self.display.delete(0, tk.END)
            return
        if key == '=':
            try:
                # eval with restricted globals for safety
                result = eval(self.expr, {"__builtins__": None}, {})
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expr = str(result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expr = ""
            return
        # append pressed key; for operators like // and ** user has dedicated buttons
        self.expr += key
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expr)

if __name__ == "__main__":
    Calculator().mainloop()
