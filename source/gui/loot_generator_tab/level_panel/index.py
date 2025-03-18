import tkinter as tk
from tkinter import ttk


class LevelPanel:
    def __init__(self, root, numLevels):
        self.root = root
        self.numLevels = numLevels

        self.varLvl = tk.IntVar()
        self.rbLevels = []

        for i in range(self.numLevels):
            self.label = "Level " + str(i + 1)
            self.rbLevels.append(
                ttk.Radiobutton(
                    self.root, text=self.label, variable=self.varLvl, value=(i + 1)
                )
            )
            self.rbLevels[i].grid(sticky="w", row=(i + 1), column=0, pady=3)

        self.varLvl.set(1)
