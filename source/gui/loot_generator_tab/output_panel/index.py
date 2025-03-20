import tkinter as tk
from tkinter import ttk

from source.gui.my_styles import MyStyles


class OutputPanel:
    def __init__(self, root: tk.LabelFrame):
        self.root = root
        self.output_scrollbar = ttk.Scrollbar(self.root)
        self.output_scrollbar.grid(row=0, column=1, sticky="nesw")
        self.output = tk.Text(
            self.root,
            height=32,
            width=100,
            state="normal",
            background=MyStyles.COLOR_TXT_BG,
            fg=MyStyles.COLOR_TXT_BG,
            bd=0,
            yscrollcommand=self.output_scrollbar.set,
        )
        self.output.grid(row=0, column=0)
        self.output_scrollbar.config(command=self.output.yview)

        self.newOutput("Welcome to the Loot Generator!\n")

    def newOutput(self, msg: str) -> None:
        msg = msg + "----------\n"
        self.output.config(state="normal")
        self.output.insert("1.0", msg)  #'row.col' position
        self.output.config(state="disabled")
        self.output.see("1.0")
