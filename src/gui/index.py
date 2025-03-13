import tkinter as tk
from tkinter import ttk, font
from my_styles import MyStyles
from Tab_Enchantments import *
from Tab_Loot_Generator import *
# from Tab_Gem_Art import *

class ProgramWindow:
    def __init__(self, program_data):
        self.root = tk.Tk() #Makes the window
        self.root.title("Random Loot Generator")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background = MyStyles.color['background'])

        # Create Notebook Style
        f = ('Segoe UI','10','bold')
        t = ('Segoe UI','10','normal')
        flabel = ('Segoe UI','16','underline')
        style = ttk.Style()
        style.theme_use('default')

        style.configure('TNotebook.Tab', background = MyStyles.color['untab'], foreground = MyStyles.color['notebookfg'], font=f, padding=(19,1))
        style.configure('TNotebook', borderwidth=0, background = MyStyles.color['notebookbg'])
        style.map('TNotebook.Tab', background = [('selected', MyStyles.color['background'])], foreground = [('selected', MyStyles.color['label text'])])
        
        # Label Style
        style.configure('TLabel', font = flabel, padx=0, pady=0, background=MyStyles.color['background'], foreground=MyStyles.color['selected'], 
                        height=4, width=5, focuscolor=MyStyles.color['button'], justify ="center")

        # Button Style
        style.configure('TButton', font = f, padx=0, pady=0, background=MyStyles.color['button'], foreground=MyStyles.color['label text'], 
                        height=4, width=18, focuscolor=MyStyles.color['button'], justify ="center")
        style.map('TButton', 
            foreground = [('disabled', MyStyles.color["disabled"]),
                        ('pressed', MyStyles.color["label text"]),
                        ('selected', MyStyles.color['label text'])], 
            background = [('disabled', MyStyles.color["button"]),
                        ('pressed', MyStyles.color["button"]),
                        ('active', MyStyles.color["button"])])
        
        # Radio Button Style
        style.configure('TRadiobutton', foreground=MyStyles.color["label text"], background=MyStyles.color["background"], 
                        indicatorcolor=MyStyles.color["not selected"], focuscolor=MyStyles.color["background"], font=f)
        style.map('TRadiobutton',
            foreground = [('disabled', MyStyles.color["disabled"]),
                        ('pressed', MyStyles.color["pressed"]),
                        ('active', MyStyles.color["highlight"])],
            background = [('disabled', MyStyles.color["background"]),
                        ('pressed', '!focus', MyStyles.color["background"]),
                        ('active', MyStyles.color["background"])],
            indicatorcolor=[('selected', MyStyles.color["selected"]),
                        ('pressed', MyStyles.color["selected"])]
        )
        
        #  Check Box Style 
        style.configure('TCheckbutton', foreground=MyStyles.color["label text"], background=MyStyles.color["background"], 
                        indicatorcolor=MyStyles.color["not selected"], font=f, focuscolor=MyStyles.color['background'])
        style.map('TCheckbutton',
            foreground = [('disabled', MyStyles.color["disabled"]),
                        ('pressed', MyStyles.color["pressed"]),
                        ('active', MyStyles.color["highlight"])],
            background = [('disabled', MyStyles.color["background"]),
                        ('pressed', '!focus', MyStyles.color["background"]),
                        ('active', MyStyles.color["background"])],
            indicatorcolor=[('selected', MyStyles.color["selected"]),
                        ('pressed', MyStyles.color["selected"])]
            )

        #  Scrollbar Style 
        style.configure('Vertical.TScrollbar', arrowcolor=MyStyles.color["selected"], background=MyStyles.color["scrollbar"], 
                        bordercolor=MyStyles.color['disabled'], troughcolor=MyStyles.color["background"], borderwidth=0)
        style.map('Vertical.TScrollbar',
            foreground = [('disabled', MyStyles.color["disabled"]),
                        ('pressed', MyStyles.color["scrollbar"]),
                        ('active', MyStyles.color["highlight"])],
            background = [('disabled', MyStyles.color["background"]),
                        ('pressed', '!focus', MyStyles.color["background"]),
                        ('active', MyStyles.color["background"])],
            indicatorcolor=[('selected', MyStyles.color["scrollbar"]),
                        ('pressed', MyStyles.color["scrollbar"])]
            )

        #  Treeview Style
        style.configure('Treeview', foreground=MyStyles.color["txt fg"], background=MyStyles.color["txt bg"], 
                        indicatorcolor=MyStyles.color["not selected"], focuscolor=MyStyles.color["background"], font=t,
                        fieldbackground=MyStyles.color["txt bg"])
        style.map('Treeview',
            foreground = [('disabled', MyStyles.color["disabled"]),
                        ('pressed', MyStyles.color["pressed"]),
                        ('active', MyStyles.color["highlight"])],
            background = [('disabled', MyStyles.color["background"]),
                        ('pressed', '!focus', MyStyles.color["background"]),
                        ('active', MyStyles.color["background"])],
            indicatorcolor=[('selected', MyStyles.color["selected"]),
                        ('pressed', MyStyles.color["selected"])]
            )
        style.configure('Treeview.Heading', foreground=MyStyles.color["txt fg"], background=MyStyles.color["txt bg"], 
                        indicatorcolor=MyStyles.color["not selected"], focuscolor=MyStyles.color["background"], font=t)
        style.map('Treeview.Heading',
            foreground = [('disabled', MyStyles.color["disabled"]),
                        ('pressed', MyStyles.color["pressed"]),
                        ('active', MyStyles.color["highlight"])],
            background = [('disabled', MyStyles.color["background"]),
                        ('pressed', '!focus', MyStyles.color["background"]),
                        ('active', MyStyles.color["background"])],
            indicatorcolor=[('selected', MyStyles.color["selected"]),
                        ('pressed', MyStyles.color["selected"])]
            )

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

        Tab_Loot_Generator(self.color, self.tabGen, program_data)
        Tab_Enchantments(self.color, self.tabEnchantment, program_data)
        # Tab_Gem_Art(self.color, self.tabEnchantment, program_data)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI