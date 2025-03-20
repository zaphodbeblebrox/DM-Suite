import tkinter as tk
from tkinter import ttk

from source.gui.loot_generator_tab.index import TabLootGenerator
from source.gui.my_styles import MyStyles


class ProgramWindow:
    def __init__(self):
        MyStyles.set_ttk_element_styles()
        self.root = tk.Tk()
        self.root.title("DM Suite")
        # self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background=MyStyles.COLOR_BACKGROUND)

        # Tab Definitions
        self.notebook = ttk.Notebook(self.root)

        self.tab_generator = ttk.Frame(self.notebook)
        self.tab_enchantment = ttk.Frame(self.notebook)
        self.tab_gems = ttk.Frame(self.notebook)
        self.tab_magic = ttk.Frame(self.notebook)
        self.tab_status_effects = ttk.Frame(self.notebook)
        self.tag_definitions = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_generator, text="Loot Generator")
        self.notebook.add(self.tab_enchantment, text="Enchantments")
        self.notebook.add(self.tab_gems, text="Gem & Art Table")
        self.notebook.add(self.tab_magic, text="Magic Reference")
        self.notebook.add(self.tab_status_effects, text="Status Effects")
        self.notebook.add(self.tag_definitions, text="Tag Definitions")
        self.notebook.grid(row=0, column=0)

        TabLootGenerator(self.tab_generator)
        # Tab_Enchantments(self.color, self.tabEnchantment, program_data)
        # Tab_Gem_Art(self.color, self.tabEnchantment, program_data)

    def start(self) -> None:
        self.root.mainloop()  # start monitoring and updating the GUI
