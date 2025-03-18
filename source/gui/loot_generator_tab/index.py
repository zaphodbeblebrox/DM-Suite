import tkinter as tk
from tkinter import font, ttk

from source.gui.loot_generator_tab.output_panel.index import OutputPanel
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
        self.fGen2 = tk.LabelFrame(
            self.frameGen,
            text="Loot Level",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.fGen3 = tk.LabelFrame(
            self.frameGen,
            text="Type of Generation",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.fGen4 = tk.LabelFrame(
            self.frameGen,
            text="Item Rarity",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )
        self.fGen5 = tk.LabelFrame(
            self.frameGen,
            text="Item Types",
            padx=5,
            pady=5,
            bg=MyStyles.COLOR_BACKGROUND,
            fg=MyStyles.COLOR_HEADER,
            font=font_section_title,
        )

        self.frame_output.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.fGen2.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.fGen3.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.fGen4.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
        self.fGen5.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

        self.textbox = OutputPanel(self.frame_output)
        # self.levelCtrl = Frame_Level(self.color, self.fGen2, 20)
        # self.rarityCtrl = Frame_Rarity(self.color, self.fGen4)

        # self.itCtrl = Frame_ItemTypes(self.color, self.fGen5, programData.itemTypeList)
        # self.buttons = Frame_Gen_Buttons(
        #     self.color,
        #     self.fGen3,
        #     programData,
        #     self.textbox,
        #     self.levelCtrl,
        #     self.rarityCtrl,
        #     self.itCtrl,
        # )
