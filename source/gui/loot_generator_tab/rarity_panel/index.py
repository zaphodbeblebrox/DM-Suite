import tkinter as tk
from tkinter import ttk


class RarityPanel:
    def __init__(self, root):
        self.root = root

        self.varRty = tk.StringVar()

        ttk.Radiobutton(
            self.root,
            text="Common",
            variable=self.varRty,
            value="C",
            style="TRadiobutton",
        ).grid(sticky="w", row=0, column=0, pady=3)

        ttk.Radiobutton(
            self.root,
            text="Uncommon",
            variable=self.varRty,
            value="U",
            style="TRadiobutton",
        ).grid(sticky="w", row=1, column=0, pady=3)

        ttk.Radiobutton(
            self.root,
            text="Rare",
            variable=self.varRty,
            value="R",
            style="TRadiobutton",
        ).grid(sticky="w", row=2, column=0, pady=3)

        ttk.Radiobutton(
            self.root,
            text="Very Rare",
            variable=self.varRty,
            value="V",
            style="TRadiobutton",
        ).grid(sticky="w", row=3, column=0, pady=3)

        ttk.Radiobutton(
            self.root,
            text="Legendary",
            variable=self.varRty,
            value="L",
            style="TRadiobutton",
        ).grid(sticky="w", row=4, column=0, pady=3)

        self.varRty.set("C")
