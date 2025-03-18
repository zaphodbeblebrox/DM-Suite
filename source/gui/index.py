import tkinter as tk
from tkinter import ttk

from source.gui.loot_generator_tab.index import TabLootGenerator
from source.gui.my_styles import MyStyles


class ProgramWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random Loot Generator")
        # self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background=MyStyles.COLOR_BACKGROUND)
        MyStyles.set_ttk_element_styles()

        # Tab Definitions
        self.notebook = ttk.Notebook(self.root)

        self.tabGen = ttk.Frame(self.notebook)
        self.tabEnchantment = ttk.Frame(self.notebook)
        self.tabGems = ttk.Frame(self.notebook)
        self.tabMagic = ttk.Frame(self.notebook)
        self.tabStatusEffects = ttk.Frame(self.notebook)
        self.tag_definitions = ttk.Frame(self.notebook)

        self.notebook.add(self.tabGen, text="Loot Generator")
        self.notebook.add(self.tabEnchantment, text="Enchantments")
        self.notebook.add(self.tabGems, text="Gem & Art Table")
        self.notebook.add(self.tabMagic, text="Magic Reference")
        self.notebook.add(self.tabStatusEffects, text="Status Effects")
        self.notebook.add(self.tag_definitions, text="Tag Definitions")
        self.notebook.grid(row=0, column=0)

        TabLootGenerator(self.tabGen)
        # Tab_Enchantments(self.color, self.tabEnchantment, program_data)
        # Tab_Gem_Art(self.color, self.tabEnchantment, program_data)

    def start(self):
        self.root.mainloop()  # start monitoring and updating the GUI
