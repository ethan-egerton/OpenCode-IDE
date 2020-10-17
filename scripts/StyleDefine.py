from tkinter import ttk

def StyleDefine(style):
    s = ttk.Style()
    color1 = style['Color1']
    color2 = style['Color2']
    color3 = style['Color3']
    color4 = style['Color4']
    color5 = style['Color5']

    # TODO All widgets need to be defined here
    s.configure('TNotebook', foreground=color1, background=color4)