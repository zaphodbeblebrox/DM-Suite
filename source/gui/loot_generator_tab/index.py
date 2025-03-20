import tkinter as tk
from tkinter import font, ttk

from source.gui.loot_generator_tab.action_panel.index import ActionPanel
from source.gui.loot_generator_tab.item_panel.index import ItemTypePanel
from source.gui.loot_generator_tab.level_panel.index import LevelPanel
from source.gui.loot_generator_tab.output_panel.index import OutputPanel
from source.gui.loot_generator_tab.rarity_panel.index import RarityPanel
from source.gui.my_styles import MyStyles


class TabLootGenerator:

    def __init__(self, root: ttk.Frame):
        self.root = root

        font_section_title = font.Font(weight="bold", size=10)

        # Generator Frame Definitions----------

        self.frame_generator = tk.LabelFrame(
            self.root, bd=0, padx=5, pady=5, bg=MyStyles.COLOR_BACKGROUND
        )
        self.frame_generator.grid(row=0, column=0)

        self.frame_output = tk.LabelFrame(
            self.frame_generator,
            text="Output Console",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_actions = tk.LabelFrame(
            self.frame_generator,
            text="Actions",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_lvl = tk.LabelFrame(
            self.frame_generator,
            text="Loot Level",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_rarity = tk.LabelFrame(
            self.frame_generator,
            text="Item Rarity",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.frame_types = tk.LabelFrame(
            self.frame_generator,
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
        self.action_panel = ActionPanel(
            root=self.frame_actions,
            output_panel=self.output_panel,
            level_panel=self.level_panel,
            rarity_panel=self.rarity_panel,
            item_type_panel=self.item_type_panel,
        )
