from doctest import master
from tkinter import *
from tkinter.font import BOLD

from six import b

from equation_solvers.BiergeVieta import BiergeVieta
from equation_solvers.Bisection import Bisection
from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.FalsePosition import FalsePosition
from equation_solvers.FixedPoint import FixedPoint
from equation_solvers.NewtonRaphson import NewtonRaphson
from equation_solvers.Root import Root
from equation_solvers.Secant import Secant



class popupWindow():
    def __init__(self):
        top=self.top=Toplevel(master)
        top.resizable(width=FALSE, height=FALSE)
        top.geometry('{}x{}'.format(200, 100))
        self.l=Label(top, font=("Helvetica", 16), width = 20,text="Enter value")
        self.l.pack()
        self.e=Entry(top, font=("Helvetica", 16), width = 20)
        self.e.pack()
        self.b=Button(top, font=("Helvetica", 16),text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        global globalValue
        globalValue = float(self.e.get())
        self.value=self.e.get()
        self.top.destroy()

rounding = True
globalValue = 0
method = 0
mode = 0
instance = 0
glob_i = 0
glob_h = 0
round_to = 6
# Functions ---------------------------------------------------------------------------------
def prepare_newton():
    label_current_method.config(text = "Method  :  Newton" , fg = 'GREEN')
    additional_entry2.grid_forget()
    global method
    method = 1
def prepare_fixed_point():
    label_current_method.config(text = "Method  :  F-Point" , fg = 'GREEN')
    additional_entry2.grid_forget()
    global method
    method = 2
def prepare_bisection():
    label_current_method.config(text = "Method  :  Bisec." , fg = 'GREEN')
    additional_entry2.grid(row=11, column=2, sticky=W)
    global method
    method = 3
def prepare_secant():
    label_current_method.config(text = "Method  :  Secant" , fg = 'GREEN')
    additional_entry2.grid(row=11, column=2, sticky=W)
    global method
    method = 4
def prepare_bierge_vieta():
    label_current_method.config(text = "Method  :  B-Vieta" , fg = 'GREEN')
    additional_entry2.grid_forget()
    global method
    method = 5
def prepare_false_position():
    label_current_method.config(text = "Method  :  False-Pos" , fg = 'GREEN')
    additional_entry2.grid(row=11, column=2, sticky=W)
    global method
    method = 6
def is_slow():
    label_current_mode.config(text = "Mode     :  Slow" , fg = 'GREEN')
    global mode
    mode = 1
    iterate.grid(row = 0, rowspan = 15 ,columnspan = 4,sticky= W, column = 0)
def is_chopping():
    global rounding
    rounding = False

def is_rounding():
    global rounding
    rounding = True
def is_fast():
    label_current_mode.config(text = "Mode     :  Fast" , fg = 'GREEN')
    global mode
    mode = 0
    iterate.grid_forget()
def solve():
    function = functionEntry.get()
    initial = float(additional_entry.get())
    if additional_entry2.get() is not "" :
         initial2 = float(additional_entry2.get())
    solver = EquationSolver(function, 20, 0.00001)
    global method
    global mode
    global instance
    if method == 1:
        instance = NewtonRaphson(function, initial)
    elif method == 2:
        instance = FixedPoint(function, initial)
    elif method == 3:
        instance = Bisection(function, initial, initial2)
    elif method == 4:
        instance = Secant(function, initial, initial2)
    elif method == 5:
        instance = BiergeVieta(function, initial)
    elif method == 6:
        instance = FalsePosition(function, initial, initial2)
    height = len(instance.roots)

    if(mode == 0) :
        b = Label(frame, borderwidth=2, relief="solid", text="i", font=("Courier", 12), width=5, fg="RED",
                  bg="YELLOW")
        b.grid(sticky=W, row=0, column=0)
        b = Label(frame,borderwidth=2, relief="solid", text="Root", font=("Courier", 12), width=15, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=1)
        b = Label(frame,borderwidth=2, relief="solid", text="Precision", font=("Courier", 12), width=15, fg="RED", bg="YELLOW")
        b.grid(sticky=W, row=0, column=2)
        width = 2
        global round_to
        for i in range(0, height):  # Rows
            b = Label(frame, borderwidth=2, relief="groove", text=str(i + 1), font=("Courier", 12), width=5, fg="RED",
                      bg="YELLOW")
            b.grid(sticky=W, row=i+1, column=0)
            for j in range(0, width):  # Columns
                if j == 0 :
                    root = instance.roots[i].root
                    if root != None :
                        root = round(root, round_to)
                    r = str(root)
                    b = Label(frame, borderwidth=2, relief="groove", text= r, font=("Courier", 12), width=15, fg="BLUE", bg="white")
                    b.grid(sticky=W, row=i + 1, column=j + 1)
                else :
                    precision = instance.roots[i].precision
                    if precision != None :
                        precision = round(precision, round_to)
                    p = str(precision)
                    b = Label(frame,borderwidth=2, relief="groove", text= p , font=("Courier", 12), width=15, fg="BLUE", bg="white")
                    b.grid(sticky=W, row=i + 1, column=j + 1)
    else :
        b = Label(frame, borderwidth=2, relief="solid", text="i", font=("Courier", 12), width=5, fg="RED",
                  bg="YELLOW")
        b.grid(sticky=W, row=0, column=0)
        b = Label(frame, borderwidth=2, relief="solid", text="Root", font=("Courier", 12), width=15, fg="RED",
                  bg="YELLOW")
        b.grid(sticky=W, row=0, column=1)
        b = Label(frame, borderwidth=2, relief="solid", text="Precision", font=("Courier", 12), width=15, fg="RED",
                  bg="YELLOW")
        b.grid(sticky=W, row=0, column=2)
        global glob_i, glob_h
        glob_i = 0
        glob_h = height
        nextIteration()
def popup():
    w = popupWindow()

def nextIteration():
    global glob_i
    global glob_h
    global rounding
    if glob_i >=glob_h :
        return
    else :
        b = Label(frame, borderwidth=2, relief="groove", text=str(glob_i + 1), font=("Courier", 12), width=5, fg="RED",
                  bg="YELLOW")
        b.grid(sticky=W, row=glob_i + 1, column=0)

        root = instance.roots[glob_i].root
        if root != None :
                root = round(root, round_to)
        r = str(root)
        b = Label(frame, borderwidth=2, relief="groove", text=r, font=("Courier", 12), width=15, fg="BLUE", bg="white")
        b.grid(sticky=W, row=glob_i + 1, column=1)

        precision = instance.roots[glob_i].precision
        if precision != None :
          precision = round(precision, round_to)
        p = str(precision)
        b = Label(frame, borderwidth=2, relief="groove", text=p, font=("Courier", 12), width=15, fg="BLUE", bg="white")
        b.grid(sticky=W, row=glob_i + 1, column=2)
        glob_i += 1

root = Tk()
root.title('Numerical Analysis')
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(1300, 800))

# Labels-----------------------------------------------------------------------------------------

label_empty = Label(root, text = "Enter the function",font=("Helvetica", 20))
#label_empty.grid(row = 0, column = 1)

label_init = Label(root, text = "initials",font=("Helvetica", 15), fg = 'BLUE')
label_init.grid(row = 0, column = 2, sticky = W)


label_current_method = Label(root, text = "Method  :   None", font=("Helvetica", 17), fg = 'RED')
label_current_method.grid(row = 7, column  = 3, sticky = W, rowspan = 5)

label_current_mode = Label(root, text = "Mode     :   None", font=("Helvetica", 17), fg = 'RED')
label_current_mode.grid(row = 11, column  = 3, sticky = W, rowspan = 5)

label_enter_function = Label(root, text = "                        ", font=("Courier", 20))
label_enter_function.grid(row = 10, column = 0)

# Entries-----------------------------------------------------------------------------------------

functionEntry = Entry(root, font=("Helvetica", 20), width = 23)
functionEntry.grid(row = 10, column = 1)
functionEntry.config(text = "heeh", fg = "blue")

additional_entry = Entry(root, font=("Helvetica", 20), width = 5)
additional_entry.grid(row = 10, column = 2,sticky = W)

additional_entry2 = Entry(root, font=("Helvetica", 20), width = 5)
additional_entry2.grid(row = 11, column = 2,sticky = W)
additional_entry2.grid_forget()


# buttons---------------------------------------------------------------------------------------


evaluate = Button(root, text = "Solve",borderwidth=4,relief="groove", font=("Helvetica", 15), command = solve, width = 28)
evaluate.grid(row = 11, column = 1, sticky = W)

labell = Label(root, text="                                                                                          ")
labell.grid(row = 12, column = 2)

iterate = Button(root,borderwidth=4, bg="lightgrey", relief="groove", text = "Click to iterate",fg = "yellow", font=("Helvetica BOLD", 17), command = nextIteration, height = 3, width = 23)
iterate.grid(row = 3, rowspan = 5 ,columnspan = 3,sticky=W, column = 0)
iterate.grid_forget()

# menus------------------------------------------------------------------------------------------

menu = Menu(root, font=("Helvetica", 20))
root.config(menu = menu)
submenu = Menu(menu, font=("Helvetica", 20), borderwidth=2, relief="solid")
menu.add_cascade(label = "Methods | ", menu = submenu)
menu.add_separator()
submenu.add_radiobutton(label = "Newton's" ,command = prepare_newton)
submenu.add_radiobutton(label = "Fixed Point", command = prepare_fixed_point)
submenu.add_radiobutton(label = "Bisection" ,command = prepare_bisection)
submenu.add_radiobutton(label = "Secant" ,command = prepare_secant)
submenu.add_radiobutton(label = "Bierge Vieta", command = prepare_bierge_vieta)
submenu.add_radiobutton(label = "False Position", command = prepare_false_position)

submenu2 = Menu(menu, font=("Helvetica", 20),borderwidth=2, relief="groove")
menu.add_cascade(label = "Mode | ", menu = submenu2)
submenu2.add_radiobutton(label = "Slow" ,command = is_slow)
submenu2.add_radiobutton(label = "Fast" ,command = is_fast)


submenu3 = Menu(menu, font=("Helvetica", 20),borderwidth=2, relief="groove")
menu.add_cascade(label = "Approximation | ", menu = submenu3)
submenu3.add_radiobutton(label = "Rounding" ,command = is_rounding)
submenu3.add_radiobutton(label = "Chopping" ,command = is_chopping)

submenu4 = Menu(menu, font=("Helvetica", 20),borderwidth=2, relief="groove")
menu.add_cascade(label = "Constants", menu = submenu4)
submenu4.add_radiobutton(label = "Precision" ,command = popup)
submenu4.add_radiobutton(label = "Maximum Iteration" ,command = popup)
submenu4.add_radiobutton(label = "Segnificant Figures" ,command = popup)


frame = Frame(root)
frame.grid(sticky = W, row = 20, columnspan = 6)
root.mainloop()


