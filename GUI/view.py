from tkinter import *

global method
global mode
# Functions ---------------------------------------------------------------------------------
def prepare_newton():
    label_current_method.config(text = "  Method  :  Newton" , fg = 'GREEN')
    method = 1

def prepare_fixed_point():
    label_current_method.config(text = "  Method  :  F-Point" , fg = 'GREEN')
    method = 2

def prepare_bisection():
    label_current_method.config(text = "  Method  :  Bisec." , fg = 'GREEN')
    method = 3

def prepare_secant():
    label_current_method.config(text = "  Method  :  Secant" , fg = 'GREEN')
    method = 4

def prepare_bierge_vieta():
    label_current_method.config(text = "  Method  :  B-Vieta" , fg = 'GREEN')
    method = 5

def is_slow():
    label_current_mode.config(text = "  Method  :  Slow" , fg = 'GREEN')
    mode = 1
    iterate.grid(row = 10, rowspan = 5 ,columnspan = 4,sticky=E)
def is_fast():
    label_current_mode.config(text = "  Method  :  Fast" , fg = 'GREEN')
    mode = 0
    iterate.grid_forget()
def solve():
    function = functionEntry.get()
    instance = 0
    if method == 1:
        pass
    elif method == 2:
        pass
    elif method == 3:
        pass
    elif method == 4:
        pass
    elif method == 5:
        pass
    elif method == 6:
        pass
    #todo continue
    if(mode == 0) :
        b = Label(frame, text="Root", font=("Courier", 12), width=12, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=0)
        b = Label(frame, text="Precision", font=("Courier", 12), width=12, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=1)
        height = len(instance.roots)
        width = 2
        for i in range(1, height):  # Rows
            for j in range(0, width):  # Columns
                b = Label(frame, text="5", font=("Courier", 12), width=12, fg="BLUE", bg="white")
                b.grid(sticky=W, row=i, column=j)
    else :
        #todo continue
        b = Label(frame, text="Root", font=("Courier", 12), width=12, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=0)
        b = Label(frame, text="Precision", font=("Courier", 12), width=12, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=1)
        height = len(instance.roots)
        width = 2



    print(function)
    return
def nextIteration(args):
    #todo continue
    pass

# Root------------------------------------------------------------------------------------------

root = Tk()
root.title('Numerical Analysis')
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(1200, 800))

# Labels-----------------------------------------------------------------------------------------

label_empty = Label(root, text = "Enter the function",font=("Courier", 20))
label_empty.grid(row = 0, column = 1)

label_init = Label(root, text = "initial",font=("Courier", 15), fg = 'BLUE')
label_init.grid(row = 0, column = 2, sticky = W)

label_current_method = Label(root, text = "  Method  :  None", font=("Courier", 20), fg = 'RED')
label_current_method.grid(row = 13, column  = 1, sticky = W)

label_current_mode = Label(root, text = "  Mode    :  None", font=("Courier", 20), fg = 'RED')
label_current_mode.grid(row = 12, column  = 1, sticky = W)

label_enter_function = Label(root, text = "                        ", font=("Courier", 20))
label_enter_function.grid(row = 10, column = 0)

# Entries-----------------------------------------------------------------------------------------

functionEntry = Entry(root, font=("Courier", 20))
functionEntry.grid(row = 10, column = 1)

additional_entry = Entry(root, font=("Courier", 20), width = 5)
additional_entry.grid(row = 10, column = 2,sticky = W)

# buttons---------------------------------------------------------------------------------------


evaluate = Button(root, text = "Solve", font=("Courier", 15), command = solve)
evaluate.grid(row = 14, column = 1)

labell = Label(root, text="                                                                                          ")
labell.grid(row = 12, column = 2)

iterate = Button(root, text = "Iterate",fg = "BLUE", font=("Courier", 15), command = nextIteration, height = 7, width = 6)
iterate.grid(row = 10, rowspan = 5 ,columnspan = 3,sticky=E)
iterate.grid_forget()

# menus------------------------------------------------------------------------------------------

menu = Menu(root, font=("Courier", 20))
root.config(menu = menu)
submenu = Menu(menu, font=("Courier", 20))
menu.add_cascade(label = "Methods | ", menu = submenu)
menu.add_separator()
submenu.add_radiobutton(label = "Newton's" ,command = prepare_newton)
submenu.add_radiobutton(label = "Fixed Point", command = prepare_fixed_point)
submenu.add_radiobutton(label = "Bisection" ,command = prepare_bisection)
submenu.add_radiobutton(label = "Secant" ,command = prepare_secant)
submenu.add_radiobutton(label = "Bierge Vieta", command = prepare_bierge_vieta)
submenu.add_radiobutton(label = "Sixth")

submenu2 = Menu(menu, font=("Courier", 20))
menu.add_cascade(label = "Mode", menu = submenu2)
submenu2.add_radiobutton(label = "Slow" ,command = is_slow)
submenu2.add_radiobutton(label = "Fast" ,command = is_fast)

frame = Frame(root)
frame.grid(sticky = W, row = 20, columnspan = 6)


root.mainloop()