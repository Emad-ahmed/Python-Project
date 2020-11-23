from tkinter import*
import os
from tkinter.filedialog import asksaveasfile,askopenfilename
root = Tk()
root.geometry("1600x1600+0+0")
root.title("Emad Note Pad")

def mainsave():
    m = textarea.get('1.0', END)
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)

    n = file.name

    f1 = open(n, "w")
    f1.write(m)
    f1.close()

def new():
    textarea.delete('1.0', END)

def newwindow():
    n = Toplevel()
    n.geometry("1600x1600+0+0")
    my_menu = Menu(n)
    n.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=0)

    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new)
    file_menu.add_command(label="New Window", command=newwindow)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save As", command=mainsave)

    frame1 = Frame(n, bg="powderblue", bd=10, relief=GROOVE)
    frame1.place(x=0, y=0, width=1600, height=700)

    scroll_y = Scrollbar(frame1, orient=VERTICAL)
    textarea = Text(frame1, yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    textarea.place(width=1600, height=700)

    n.mainloop()

def openall():
    filename = askopenfilename(parent=root)
    f = open(filename)
    f.read()

def cbg():
    textarea.configure(background = "grey",font="Times 15 bold", fg="cyan")

my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu, tearoff = 0, font="times 15 bold")

my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new)
file_menu.add_command(label = "New Window", command = newwindow)
file_menu.add_command(label = "Open", command =openall)
file_menu.add_command(label = "Save As", command =mainsave)
file_menu.add_command(label = "Exit", command =root.quit)



file_menu = Menu(my_menu, tearoff = 0, font="times 15 bold")

my_menu.add_cascade(label = "Edit", menu = file_menu)
file_menu.add_command(label="Undo")
file_menu.add_separator()
file_menu.add_command(label = "Cut")

file_menu.add_command(label = "Copy")
file_menu.add_command(label = "Paste")
file_menu.add_command(label = "Delete")

file_menu.add_separator()
file_menu.add_command(label = "Change Background", command = cbg)
file_menu.add_command(label = "Find")
file_menu.add_command(label = "Find Next")
file_menu.add_command(label = "Find Previous")
file_menu.add_command(label = "Replace")
file_menu.add_command(label = "Go To")
file_menu.add_separator()
file_menu.add_command(label = "Select All")
file_menu.add_command(label = "Time Date")



file_menu = Menu(my_menu, tearoff = 0, font="times 15 bold")

my_menu.add_cascade(label = "Format", menu = file_menu)
file_menu.add_command(label = "Word Wrap")
file_menu.add_command(label = "Font")


file_menu = Menu(my_menu, tearoff = 0, font="times 15 bold")
my_menu.add_cascade(label = "View", menu = file_menu)
file_menu.add_command(label = "Zoom")

file_menu.add_command(label = "Status Bar")




file_menu = Menu(my_menu, tearoff = 0, font="times 15 bold")

my_menu.add_cascade(label = "Help", menu = file_menu)
file_menu.add_command(label = "View Help")
file_menu.add_command(label = "Send Feedback")
file_menu.add_separator()
file_menu.add_command(label = "About Notepad")


frame1 = Frame(root, bg="powderblue", bd=10, relief = GROOVE)
frame1.place(x=0, y=0, width=1600, height=700)

scroll_y = Scrollbar(frame1, orient = VERTICAL)
textarea = Text(frame1, yscrollcommand = scroll_y.set, font="Times 15 bold")
scroll_y.pack(side=RIGHT, fill=Y)
textarea.place(width=1600, height=700)






root.mainloop()