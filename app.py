"""
Ivri Korem 2020
description
"""

# TODO Don't use this line, make sure all submodules are included and not through *
# Though doing this is a pain in the ass
from tkinter import *
from tkinter import ttk, filedialog
from os import mkdir, path
from json import load
from scripts.StyleDefine import StyleDefine

# GUI init
root = Tk()
root.title("OpenCode - IDE")
# TODO Get icon
#root.iconbitmap(" ")
root.geometry("1000x750")
root.minsize(240, 200)
#root.attributes("-fullscreen", True)

# NOTE suggestions
# split things up into different files, makes code more managable
# be super careful with memory usage, python is not great at doing big projects and uses a lot of memory (shrink things down)
# tkinter is somewhat limiting, might be a issue for some features

#################### Initalising Colors ####################
# Takes the JSON and finds the names data, uses that as a reference for what data to call corresponding to the button

# Loads JSON data
themeNames = ""
with open('assets/themes/themes.json') as f:
    themesData = load(f)

themeNames = themesData['Names']
themeNames = themeNames.split(',')

# Redefines the colors used in the styles


# Takes the button number and finds the theme inside the theme data
def SetColors():
    x = int(themeNumber.get())
    themeName = themeNames[x]
    theme = themesData[themeName]
    StyleDefine(theme)

theme = themesData["Light"]
StyleDefine(theme)

#------------------- Ending Colors -------------------#


#################### Creating Toolbar ####################

# Init toolbar
toolBar = Menu(root)


# Creating commands for file menu
class FileMenu():
    def CreateNewFile(self):
        fileLocation = filedialog.asksaveasfilename() # it probably doesnt even need to save, just create the new tab
        open(f"{fileLocation}","w+")
        createNewTab(fileLocation)

    # I really dont think you need to create new folders + no support for this in tkinter.filedialog
    def CreateNewFolder(self):
        popup = Tk()
        Label(popup).pack() #for space
        popup.geometry("200x120")
        entry = Entry(popup, width=25)
        entry.pack()
        Label(popup).pack() #for space
        def command():
            mkdir(f"{entry.get()}")
            popup.destroy()
        Button(popup, text="Save", padx=25, pady=10, command=command).pack()

    def OpenFile(self):
        fileLocation = filedialog.askopenfile()
        f = open(f'{fileLocation}', 'r')
        createNewTab(fileLocation)

    def OpenFolder(self):
        filedialog.askdirectory()

    def SaveFile(self):
        filename = Notepads[0] # not the best solution
        if path.exists(filename):
            content = Notepads[0] # not the best solution
            open(filename, "w").write(content)
        else:
            self.SaveFileAs()

    def SaveFileAs(self):
        content = Notepads[0].get(1.0, END)
        fileLocation = filedialog.asksaveasfile()
        open(f"{fileLocation}","w+").write(content)


fm = FileMenu()

# Creating file menu
fileMenu = Menu(toolBar, tearoff=False)

fileMenu.add_command(label="New File", accelerator="Ctrl+N", command=fm.CreateNewFile)
fileMenu.add_command(label="New Folder", accelerator="Ctrl+Shift+N", command=fm.CreateNewFolder)
fileMenu.add_command(label="Open File", accelerator="Ctrl+O", command=fm.OpenFile)
fileMenu.add_command(label="Open Folder", accelerator="Ctrl+Alt+O", command=fm.OpenFolder)
fileMenu.add_command(label="Save", accelerator="Ctrl+S", command=fm.SaveFile)
fileMenu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=fm.SaveFileAs)
fileMenu.add_checkbutton(label="Auto Save")


# Creating commands for edit menu
class EditMenu():
    def Undo(self):
        pass
    def Redo(self):
        pass
    def Cut(self):
        pass
    def Copy(self):
        pass
    def Paste(self):
        pass
    def Find(self):
        # TODO: use Regex, pop up window maybe, seems like a hassle
        pass

em = EditMenu()

# Creating edit menu
editMenu = Menu(toolBar, tearoff=False)

editMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=em.Undo)
editMenu.add_command(label="Redo", accelerator="Ctrl+Y", command=em.Redo)
editMenu.add_command(label="Cut", accelerator="Ctrl+X", command=em.Cut)
editMenu.add_command(label="Copy", accelerator="Ctrl+C", command=em.Copy)
editMenu.add_command(label="Paste", accelerator="Ctrl+V", command=em.Paste)
editMenu.add_command(label="Find", accelerator="Ctrl+F", command=em.Find)


# Creating commands for view menu
class ViewMenu():
    def goFullScreen(self):
        root.attributes("-fullscreen", True)
    
    def createEditorTheme(self):
        pass

    def importEditorTheme(self):
        pass

vm = ViewMenu()

# Creating view menu
viewMenu = Menu(toolBar, tearoff=False)

editorTheme = Menu(viewMenu, tearoff=False)
viewMenu.add_command(label="Full Screen", accelerator="F11", command=vm.goFullScreen)
viewMenu.add_checkbutton(label="Enable Mark Errors")
viewMenu.add_command(label="Create Editor Theme", command=vm.createEditorTheme)
viewMenu.add_command(label="Import Editor Theme", command=vm.importEditorTheme)

# Takes theme names out of list and generates them with numbers
themeNumber = StringVar()
i = 0
for theme in themeNames:
    editorTheme.add_radiobutton(label=theme, variable=themeNumber, value=str(i), command=SetColors)
    i += 1


# Creating commands for prefrences menu
class PrefrencesMenu():
    def popupConfigure(self):
        pass
    
    def popupShortcuts(self):
        pass
    
    def createEditorExtension(self):
        pass

pm = PrefrencesMenu()

# Creating prefrences menu
prefrencesMenu = Menu(toolBar, tearoff=False)

prefrencesMenu.add_command(label="Configure", command=pm.popupConfigure)
prefrencesMenu.add_checkbutton(label="Enable Hints")
prefrencesMenu.add_command(label="Shortcuts", command=pm.popupShortcuts)
prefrencesMenu.add_command(label="Create Extension", command=pm.createEditorExtension)


# Creating commands for help menu
class HelpMenu():
    def popupHelp(self):
        pass

    def openWelcomeFile(self):
        content = open('assets/content/welcome.txt', 'r').read()
        global comp

        # Creating the notepad tab
        Tabs[comp] = Frame(tabs, padx=5, pady=5)       #not finished
        Notepads[comp] = Text(Tabs[comp], padx=500, pady=300)
        Notepads[comp].config(wrap="word", relief=FLAT)

        scroll = Scrollbar(Tabs[comp])
        Notepads[comp].focus_set()
        scroll.config(command=Notepads[comp].yview)
        Notepads[comp].config(yscrollcommand=scroll.set)
        Notepads[comp].insert(END, content)

        # Displaying everything
        Notepads[comp].pack(fill=BOTH, expand=True)
        Tabs[comp].pack(fill=BOTH, expand=True)
        tabs.add(Tabs[comp], text="Welcome")
    
        # Incremeting the comparison
        comp += 1

    
    def openExplanationFile(self):
        pass
    
    def openContributeFile(self):
        pass

hm = HelpMenu()

# Creating help menu
helpMenu = Menu(toolBar, tearoff=False)

helpMenu.add_command(label="Help", accelerator="Ctrl+Shift+H", command=hm.popupHelp)
helpMenu.add_command(label="How to get started?", accelerator="Ctrl+Shift+W", command=hm.openWelcomeFile)
helpMenu.add_command(label="What is OpenCode?", command=hm.openExplanationFile)
helpMenu.add_command(label="How can I contribute?", command=hm.openContributeFile)
helpMenu.add_command(label="How to create editor themes?", command=hm.openContributeFile)
helpMenu.add_command(label="How to create an extension?", command=hm.openContributeFile)

# Adding all the menus to the toolbar
toolBar.add_cascade(label="File", menu=fileMenu)

toolBar.add_cascade(label="Edit", menu=editMenu)

toolBar.add_cascade(label="View", menu=viewMenu)
viewMenu.add_cascade(label="Editor Theme", menu=editorTheme)

toolBar.add_cascade(label="Prefrences", menu=prefrencesMenu)

toolBar.add_cascade(label="Help", menu=helpMenu)

# Displaying the toolbar
root.config(menu = toolBar)

#------------------- Ending Toolbar -------------------#


#################### Creating Sidebar ####################

#------------------- Ending Sidebar -------------------#


#################### Creating File Explorer ####################

#------------------- Ending File Explorer -------------------#


#################### Creating NotePad ####################
# Creating tabs
tabs = ttk.Notebook(root, style='TNotebook')
tabs.pack(pady=10)
Tabs = {}
Notepads = {}
comp = 0

def createNewTab(fileName):
    global comp

    # Creating the notepad tab
    Tabs[comp] = Frame(tabs, padx=5, pady=5)       #not finished
    Notepads[comp] = Text(Tabs[comp], padx=500, pady=300)
    Notepads[comp].config(wrap="word", relief=FLAT)

    scroll = Scrollbar(Tabs[comp])
    Notepads[comp].focus_set()
    scroll.config(command=Notepads[comp].yview)
    Notepads[comp].config(yscrollcommand=scroll.set)

    # Displaying everything
    Notepads[comp].pack(fill=BOTH, expand=True)
    Tabs[comp].pack(fill=BOTH, expand=True)
    tabs.add(Tabs[comp], text=fileName)
    
    # Incremeting the comparison
    comp += 1

hm.openWelcomeFile()

# Font family and font size usage

##
#------------------- Ending NotePad -------------------#


#################### Creating Terminal ####################

#------------------- Ending Terminal  -------------------#


# Running main loop
root.mainloop()