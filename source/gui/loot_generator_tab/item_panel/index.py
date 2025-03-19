import tkinter as tk
from tkinter import ttk

from source.file_import.items import Items


class ItemTypePanel:
    def __init__(self, root):
        self.root = root
        self.varState = []
        # tempBoolList = []
        # for item_type in Items.item_types:
        #     tempBoolList.append(item_type)
        # Boolean_list = list(map(lambda ele: ele == "True", tempBoolList))

        for idx, item_type in enumerate(Items.item_types):
            tempVar = tk.BooleanVar(value=True)
            ttk.Checkbutton(
                self.root,
                text=item_type,
                variable=tempVar,
                onvalue=1,
                offvalue=0,
            ).grid(sticky="w", row=idx, column=0, pady=3)
            self.varState.append(tempVar)
