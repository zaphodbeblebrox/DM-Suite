import tkinter as tk
from tkinter import ttk, font

class MyStyles():

    COLOR_BACKGROUND = "#232323"
    COLOR_NOTEBOOK_BG = "#1a1a1a"
    COLOR_NOTEBOOK_FG = "#000000"
    COLOR_BUTTON = "#333333"
    COLOR_UNTAB = "#BB86FC"
    COLOR_SELECTED = "#FFDD03"
    COLOR_NOT_SELECTED = "#333333"
    COLOR_HEADER = "#FFDD00"
    COLOR_LABEL_TXT = "#BB86FC"
    COLOR_PRESSED = "#D3D3D3"
    COLOR_TXT_BG = "#232323"
    COLOR_TXT_FG = "#ffffff"
    COLOR_HIGHLIGHT = "#D3D3D3"
    COLOR_DISABLED = "#FF9494"
    COLOR_SCROLLBAR = "#4d4d4d"
    
    # Call AFTER tk.TK() window creation
    @classmethod
    def set_ttk_element_styles(cls) -> None:
        if not tk._default_root:
            tk._default_root = tk.Tk()
            tk._default_root.withdraw()
        # Create Notebook Style
        std_font = ('Segoe UI','10','bold')
        treeview_font = ('Segoe UI','10','normal')
        label_font = ('Segoe UI','16','underline')
        style = ttk.Style()
        style.theme_use('default')

        # Notebook Style
        style.configure('TNotebook.Tab', background = cls.COLOR_UNTAB, foreground = cls.COLOR_NOTEBOOK_FG, font=std_font, padding=(19,1))
        style.configure('TNotebook', borderwidth=0, background = cls.COLOR_NOTEBOOK_BG)
        style.map('TNotebook.Tab', background = [('selected', cls.COLOR_BACKGROUND)], foreground = [('selected', cls.COLOR_LABEL_TXT)])
        
        # Label Style
        style.configure('TLabel', font = label_font, padx=0, pady=0, background=cls.COLOR_BACKGROUND, foreground=cls.COLOR_SELECTED, 
                        height=4, width=5, focuscolor=cls.COLOR_BUTTON, justify ="center")

        # Button Style
        style.configure('TButton', font = std_font, padx=0, pady=0, background=cls.COLOR_BUTTON, foreground=cls.COLOR_LABEL_TXT, 
                        height=4, width=18, focuscolor=cls.COLOR_BUTTON, justify ="center")
        style.map('TButton', 
            foreground = [('disabled', cls.COLOR_DISABLED),
                        ('pressed', cls.COLOR_LABEL_TXT),
                        ('selected', cls.COLOR_LABEL_TXT)], 
            background = [('disabled', cls.COLOR_BUTTON),
                        ('pressed', cls.COLOR_BUTTON),
                        ('active', cls.COLOR_BUTTON)])
        
        # Radio Button Style
        style.configure('TRadiobutton', foreground=cls.COLOR_LABEL_TXT, background=cls.COLOR_BACKGROUND, 
                        indicatorcolor=cls.COLOR_NOT_SELECTED, focuscolor=cls.COLOR_BACKGROUND, font=std_font)
        style.map('TRadiobutton',
            foreground = [('disabled', cls.COLOR_DISABLED),
                        ('pressed', cls.COLOR_PRESSED),
                        ('active', cls.COLOR_HIGHLIGHT)],
            background = [('disabled', cls.COLOR_BACKGROUND),
                        ('pressed', '!focus', cls.COLOR_BACKGROUND),
                        ('active', cls.COLOR_BACKGROUND)],
            indicatorcolor=[('selected', cls.COLOR_SELECTED),
                        ('pressed', cls.COLOR_SELECTED)]
        )
        
        #  Check Box Style 
        style.configure('TCheckbutton', foreground=cls.COLOR_LABEL_TXT, background=cls.COLOR_BACKGROUND, 
                        indicatorcolor=cls.COLOR_NOT_SELECTED, font=std_font, focuscolor=cls.COLOR_BACKGROUND)
        style.map('TCheckbutton',
            foreground = [('disabled', cls.COLOR_DISABLED),
                        ('pressed', cls.COLOR_PRESSED),
                        ('active', cls.COLOR_HIGHLIGHT)],
            background = [('disabled', cls.COLOR_BACKGROUND),
                        ('pressed', '!focus', cls.COLOR_BACKGROUND),
                        ('active', cls.COLOR_BACKGROUND)],
            indicatorcolor=[('selected', cls.COLOR_SELECTED),
                        ('pressed', cls.COLOR_SELECTED)]
            )

        #  Scrollbar Style 
        style.configure('Vertical.TScrollbar', arrowcolor=cls.COLOR_SELECTED, background=cls.COLOR_SCROLLBAR, 
                        bordercolor=cls.COLOR_DISABLED, troughcolor=cls.COLOR_BACKGROUND, borderwidth=0)
        style.map('Vertical.TScrollbar',
            foreground = [('disabled', cls.COLOR_DISABLED),
                        ('pressed', cls.COLOR_SCROLLBAR),
                        ('active', cls.COLOR_HIGHLIGHT)],
            background = [('disabled', cls.COLOR_BACKGROUND),
                        ('pressed', '!focus', cls.COLOR_BACKGROUND),
                        ('active', cls.COLOR_BACKGROUND)],
            indicatorcolor=[('selected', cls.COLOR_SCROLLBAR),
                        ('pressed', cls.COLOR_SCROLLBAR)]
            )

        #  Treeview Style
        style.configure('Treeview', foreground=cls.COLOR_TXT_FG, background=cls.COLOR_TXT_BG, 
                        indicatorcolor=cls.COLOR_NOT_SELECTED, focuscolor=cls.COLOR_BACKGROUND, font=treeview_font,
                        fieldbackground=cls.COLOR_TXT_BG)
        style.map('Treeview',
            foreground = [('disabled', cls.COLOR_DISABLED),
                        ('pressed', cls.COLOR_PRESSED),
                        ('active', cls.COLOR_HIGHLIGHT)],
            background = [('disabled', cls.COLOR_BACKGROUND),
                        ('pressed', '!focus', cls.COLOR_BACKGROUND),
                        ('active', cls.COLOR_BACKGROUND)],
            indicatorcolor=[('selected', cls.COLOR_SELECTED),
                        ('pressed', cls.COLOR_SELECTED)]
            )
        style.configure('Treeview.Heading', foreground=cls.COLOR_TXT_FG, background=cls.COLOR_TXT_BG, 
                        indicatorcolor=cls.COLOR_NOT_SELECTED, focuscolor=cls.COLOR_BACKGROUND, font=treeview_font)
        style.map('Treeview.Heading',
            foreground = [('disabled', cls.COLOR_DISABLED),
                        ('pressed', cls.COLOR_PRESSED),
                        ('active', cls.COLOR_HIGHLIGHT)],
            background = [('disabled', cls.COLOR_BACKGROUND),
                        ('pressed', '!focus', cls.COLOR_BACKGROUND),
                        ('active', cls.COLOR_BACKGROUND)],
            indicatorcolor=[('selected', cls.COLOR_SELECTED),
                        ('pressed', cls.COLOR_SELECTED)]
            )