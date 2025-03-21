import tkinter as tk

from tkinter import ttk
from functools import partial

from source.gui.loot_generator_tab.action_panel.button_actions import ButtonActions
from source.gui.loot_generator_tab.item_panel.index import ItemTypePanel
from source.gui.loot_generator_tab.level_panel.index import LevelPanel
from source.gui.loot_generator_tab.output_panel.index import OutputPanel
from source.gui.loot_generator_tab.rarity_panel.index import RarityPanel
from source.gui.my_styles import MyStyles


class ActionPanel:
    def __init__(
        self,
        root: tk.LabelFrame,
        output_panel: OutputPanel,
        level_panel: LevelPanel,
        rarity_panel: RarityPanel,
        item_type_panel: ItemTypePanel,
    ):
        self.root = root
        self.textFrame = output_panel
        self.levelFrame = level_panel
        self.rarityFrame = rarity_panel
        self.itemTypeFrame = item_type_panel

        self.levelFrame.varLvl.get()

        self.buttons = [
            {
                "name": "Individual\nTreasure",
                "func": partial(
                    ButtonActions.individual_loot,
                    self.levelFrame.varLvl.get(),
                    output_panel,
                ),
            },
            {
                "name": "Horde\nTreasure",
                "func": partial(
                    ButtonActions.horde_loot,
                    self.levelFrame.varLvl.get(),
                    output_panel,
                ),
            },
            {"name": "Weapon Drop", "func": partial(self.dummy)},  # weaponDropB
            {"name": "Art & Gems", "func": partial(self.dummy)},  # artgemB
            {"name": "Enchanted Rune", "func": partial(self.dummy)},  # runeB
            {"name": "Roll Specific Item", "func": partial(self.dummy)},  # rollItemB
        ]

        for idx, btn in enumerate(self.buttons):
            border = self.create_border()
            ttk.Button(
                border,
                text=btn["name"],
                state="normal",
                command=btn["func"],
            ).grid(row=0, column=0, sticky="nesw", ipady=15)
            border.grid(row=idx, column=0, sticky="nsew", padx=5, pady=5)

    # Functions-------------------
    def dummy(self):
        pass

    def create_border(self) -> tk.Frame:
        return tk.Frame(
            self.root,
            highlightcolor=MyStyles.COLOR_LABEL_TXT,
            highlightbackground=MyStyles.COLOR_LABEL_TXT,
            highlightthickness=2,
            bd=0,
            height=5,
            width=18,
        )
