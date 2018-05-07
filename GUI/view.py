from tkinter import *

from equation_solvers.BiergeVieta import BiergeVieta
from equation_solvers.Bisection import Bisection
from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.FalsePosition import FalsePosition
from equation_solvers.FixedPoint import FixedPoint
from equation_solvers.NewtonRaphson import NewtonRaphson
from equation_solvers.Secant import Secant

method = 0
mode = 0
# Functions ---------------------------------------------------------------------------------
def prepare_newton():
    label_current_method.config(text = "  Method  :  Newton" , fg = 'GREEN')
    global method
    method = 1
def prepare_fixed_point():
    label_current_method.config(text = "  Method  :  F-Point" , fg = 'GREEN')
    global method
    method = 2
def prepare_bisection():
    label_current_method.config(text = "  Method  :  Bisec." , fg = 'GREEN')
    global method
    method = 3
def prepare_secant():
    label_current_method.config(text = "  Method  :  Secant" , fg = 'GREEN')
    global method
    method = 4
def prepare_bierge_vieta():
    label_current_method.config(text = "  Method  :  B-Vieta" , fg = 'GREEN')
    global method
    method = 5
def prepare_false_position():
    label_current_method.config(text = "  Method  :  False-Pos" , fg = 'GREEN')
    global method
    method = 6
def is_slow():
    label_current_mode.config(text = "  Method  :  Slow" , fg = 'GREEN')
    global mode
    mode = 1
    iterate.grid(row = 10, rowspan = 5 ,columnspan = 4,sticky=E)
def is_fast():
    label_current_mode.config(text = "  Method  :  Fast" , fg = 'GREEN')
    global mode
    mode = 0
    iterate.grid_forget()
def solve():
    function = functionEntry.get()
    initial = float(additional_entry.get())
    solver = EquationSolver(function, 20, 0.00001)
    global method
    global mode
    if method == 1:
        instance = NewtonRaphson(function, initial)
    elif method == 2:
        instance = FixedPoint(function, initial)
    elif method == 3:
        instance = Bisection()
    elif method == 4:
        instance = Secant()
    elif method == 5:
        instance = BiergeVieta()
    elif method == 6:
        instance = FalsePosition()
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
                if j == 0 :
                    root = instance.roots[i].root
                    r = str(root)
                    b = Label(frame, text= r, font=("Courier", 12), width=12, fg="BLUE", bg="white")
                    b.grid(sticky=W, row=i, column=j)
                else :
                    precision = instance.roots[i].precision
                    p = str(precision)
                    b = Label(frame, text= p , font=("Courier", 12), width=12, fg="BLUE", bg="white")
                    b.grid(sticky=W, row=i, column=j)
    else :
        #todo continue
        b = Label(frame, text="Root", font=("Courier", 12), width=12, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=0)
        b = Label(frame, text="Precision", font=("Courier", 12), width=12, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=1)
        height = len(instance.roots)
        width = 2
def nextIteration(args):
    #todo continue
    pass


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
submenu.add_radiobutton(label = "False Position", command = prepare_false_position)

submenu2 = Menu(menu, font=("Courier", 20))
menu.add_cascade(label = "Mode", menu = submenu2)
submenu2.add_radiobutton(label = "Slow" ,command = is_slow)
submenu2.add_radiobutton(label = "Fast" ,command = is_fast)

frame = Frame(root)
frame.grid(sticky = W, row = 20, columnspan = 6)
root.mainloop()
