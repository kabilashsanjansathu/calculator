import tkinter as tk
from tkinter import font

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Custom font
        self.default_font = font.Font(size=20)
        
        # Variables
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
        
        # Create UI
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, height=100)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Display label
        self.display_var = tk.StringVar()
        self.display_var.set(self.current_input)
        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            anchor="e",
            font=font.Font(size=36),
            bg="#f0f0f0",
            padx=20
        )
        display_label.pack(expand=True, fill="both")
    
    def create_buttons(self):
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]
        
        # Create buttons
        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")
            
            for btn_text in row:
                btn = tk.Button(
                    row_frame,
                    text=btn_text,
                    font=self.default_font,
                    command=lambda t=btn_text: self.on_button_click(t)
                )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
                
                # Style special buttons
                if btn_text in ['/', '*', '-', '+', '=']:
                    btn.config(bg="#ff9933", fg="white")
                elif btn_text == 'C':
                    btn.config(bg="#ff3333", fg="white")
    
    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.handle_digit_input(button_text)
        elif button_text == 'C':
            self.clear_all()
        elif button_text in ['/', '*', '-', '+']:
            self.handle_operation(button_text)
        elif button_text == '=':
            self.calculate_result()
        
        self.update_display()
    
    def handle_digit_input(self, digit):
        if self.reset_input:
            self.current_input = "0"
            self.reset_input = False
        
        if digit == '.':
            if '.' not in self.current_input:
                self.current_input += digit
        else:
            if self.current_input == "0":
                self.current_input = digit
            else:
                self.current_input += digit
    
    def handle_operation(self, op):
        if self.stored_value is None:
            self.stored_value = float(self.current_input)
        else:
            self.calculate_result()
        
        self.operation = op
        self.reset_input = True
    
    def calculate_result(self):
        if self.operation and self.stored_value is not None:
            try:
                current_value = float(self.current_input)
                if self.operation == '+':
                    result = self.stored_value + current_value
                elif self.operation == '-':
                    result = self.stored_value - current_value
                elif self.operation == '*':
                    result = self.stored_value * current_value
                elif self.operation == '/':
                    result = self.stored_value / current_value
                
                self.current_input = str(result)
                if self.current_input.endswith('.0'):
                    self.current_input = self.current_input[:-2]
                
                self.stored_value = None
                self.operation = None
                self.reset_input = True
            except ZeroDivisionError:
                self.current_input = "Error"
                self.stored_value = None
                self.operation = None
                self.reset_input = True
    
    def clear_all(self):
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
    
    def update_display(self):
        if len(self.current_input) > 12:
            self.display_var.set(self.current_input[:12] + "...")
        else:
            self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
