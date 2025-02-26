import tkinter as tk
from tkinter import ttk
import json

from baseConverter import BaseConverter

class UnitConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        self.current_theme = "light"
        
        self.converters = self.load_converters('converters.json')
        self.converter = BaseConverter(self.converters)

        self.selected_category = tk.StringVar(value="length")
        self.units = list(self.converters[self.selected_category.get()].keys())

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0)

        self.category_combobox = ttk.Combobox(root, values=list(self.converters.keys()), textvariable=self.selected_category)
        self.category_combobox.grid(row=1, column=1)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_units)

        self.from_unit_label = tk.Label(root, text="From Unit:")
        self.from_unit_label.grid(row=2, column=0)

        self.from_unit_combobox = ttk.Combobox(root, values=self.units)
        self.from_unit_combobox.grid(row=2, column=1)

        self.to_unit_label = tk.Label(root, text="To Unit:")
        self.to_unit_label.grid(row=3, column=0)

        self.to_unit_combobox = ttk.Combobox(root, values=self.units)
        self.to_unit_combobox.grid(row=3, column=1)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_units)
        self.convert_button.grid(row=4, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=5, column=0)

        self.result_display = tk.Label(root, text="")
        self.result_display.grid(row=5, column=1)

        self.theme_button = tk.Button(root, text="Switch to Dark Mode", command=self.switch_theme)
        self.theme_button.grid(row=6, column=0, columnspan=2)

        self.apply_theme()

    def load_converters(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def update_units(self, event=None):
        category = self.selected_category.get()
        self.units = list(self.converters[category].keys())
        self.from_unit_combobox['values'] = self.units
        self.to_unit_combobox['values'] = self.units

    def convert_units(self):
        try:
            amount = float(self.amount_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()

            category = self.selected_category.get()

            result = self.converter.convert(from_unit, amount, to_unit, category)
            self.result_display.config(text=f"{result[to_unit]:.2f} {to_unit}")

        except ValueError:
            self.result_display.config(text="Invalid input")

    def switch_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.theme_button.config(text="Light")
        else:
            self.current_theme = "light"
            self.theme_button.config(text="Dark")
        
        self.apply_theme()

    def apply_theme(self):
        if self.current_theme == "light":
            self.root.config(bg="white")
            self.amount_label.config(bg="white", fg="black")
            self.amount_entry.config(bg="white", fg="black")
            self.category_label.config(bg="white", fg="black")
            self.category_combobox.config( background="white", foreground="black")
            self.from_unit_label.config(bg="white", fg="black")
            self.from_unit_combobox.config( background="white", foreground="black")
            self.to_unit_label.config(bg="white", fg="black")
            self.to_unit_combobox.config( background="white", foreground="black")
            self.convert_button.config(bg="lightgray", fg="black")
            self.result_label.config(bg="white", fg="black")
            self.result_display.config(bg="white", fg="black")
        else:
            self.root.config(bg="black")
            self.amount_label.config(bg="black", fg="white")
            self.amount_entry.config(bg="black", fg="white")
            self.category_label.config(bg="black", fg="white")
            self.category_combobox.config( background="black", foreground="white")
            self.from_unit_label.config(bg="black", fg="white")
            self.from_unit_combobox.config( background="black", foreground="white")
            self.to_unit_label.config(bg="black", fg="white")
            self.to_unit_combobox.config( background="black", foreground="white")
            self.convert_button.config(bg="darkgray", fg="white")
            self.result_label.config(bg="black", fg="white")
            self.result_display.config(bg="black", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterGUI(root)
    root.mainloop()