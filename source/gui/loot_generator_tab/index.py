import tkinter as tk
from tkinter import font, ttk

from source.gui.loot_generator_tab.item_panel.index import ItemTypePanel
from source.gui.loot_generator_tab.level_panel.index import LevelPanel
from source.gui.loot_generator_tab.output_panel.index import OutputPanel
from source.gui.loot_generator_tab.rarity_panel.index import RarityPanel
from source.gui.my_styles import MyStyles


class TabLootGenerator:

    def __init__(self, root):
        self.root = root

        font_section_title = font.Font(weight="bold", size=10)

        # Generator Frame Definitions----------

        self.frameGen = tk.LabelFrame(
            self.root, bd=0, padx=5, pady=5, bg=MyStyles.COLOR_BACKGROUND
        )
        self.frameGen.grid(row=0, column=0)

        self.frame_output = tk.LabelFrame(
            self.frameGen,
            text="Generator Output",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_actions = tk.LabelFrame(
            self.frameGen,
            text="Actions",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_lvl = tk.LabelFrame(
            self.frameGen,
            text="Loot Level",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_rarity = tk.LabelFrame(
            self.frameGen,
            text="Item Rarity",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_types = tk.LabelFrame(
            self.frameGen,
            text="Item Types",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )

        self.frame_output.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.frame_actions.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.frame_lvl.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.frame_rarity.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
        self.frame_types.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

        self.output_panel = OutputPanel(self.frame_output)
        self.level_panel = LevelPanel(self.frame_lvl)
        self.rarity_panel = RarityPanel(self.frame_rarity)
        self.item_type_panel = ItemTypePanel(self.frame_types)
        # self.buttons = Frame_Gen_Buttons(
        #     self.color,
        #     self.fGen3,
        #     programData,
        #     self.textbox,
        #     self.levelCtrl,
        #     self.rarityCtrl,
        #     self.itCtrl,
        # )
