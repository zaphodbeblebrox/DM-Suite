import tkinter as tk
from tkinter import ttk
from typing import List


class LevelPanel:
    def __init__(self, root: tk.LabelFrame):
        self.root = root
        maxLevel = 20

        self.varLvl = tk.IntVar()
        self.rbLevels: List[ttk.Radiobutton] = []

        for i in range(maxLevel):
            self.label = "Level " + str(i + 1)
            self.rbLevels.append(
                ttk.Radiobutton(
                    self.root, text=self.label, variable=self.varLvl, value=(i + 1)
                )
            )
            self.rbLevels[i].grid(sticky="w", row=(i + 1), column=0, pady=3)

        self.varLvl.set(1)
