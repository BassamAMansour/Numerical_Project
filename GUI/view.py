import tkinter
from doctest import master
from tkinter import *
from tkinter.font import BOLD

from six import b
from sympy import simplify

from GUI.Plots.Plotter import Plotter
from Interpolatin import Newton
from Interpolation import LagrangeInterpolation
from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.FalsePosition import FalsePosition
from equation_solvers.FixedPoint import FixedPoint
from equation_solvers.NewtonRaphson import NewtonRaphson
from equation_solvers.Root import Root
from equation_solvers.Secant import Secant
from equation_solvers.BiergeVieta import BiergeVieta
from equation_solvers.Bisection import Bisection

rounding = True
globalValue = 0
method = 0
mode = 0
instance = 0
glob_i = 0
glob_h = 0
round_to = 6
table_as_list = []
MAX_ITERATIONS = 49
EPSILON_PRESICION = 0.0001
globalInterpolation = 0
x_labels_as_list = []
fx_labels_as_list = []
x_list = []
fx_list = []
lagrange = False
class InterpolationWindow():
    lblfunc = 0
    lblfuncSimp = 0
    def __init__(self):
        root2 = Tk()
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - ((globalInterpolation+1)*128 / 2)
        y = (hs / 2) - (170 / 2)
        root2.geometry('%dx%d+%d+%d' % ((globalInterpolation+1)*128, 170, x, y))
        root2.title('Interpolation')
        lblx = Label(root2, font=("Helvetica", 20), width = 8 , borderwidth=2, relief="groove", bg = "yellow", fg = "black", text = "X")
        lblFx = Label(root2, font=("Helvetica", 20), width = 8 ,  borderwidth=2, relief="groove",bg = "yellow", fg = "black", text = "F(x)")
        lblx.grid(row = 0, column = 0)
        lblFx.grid(row = 1, column = 0)
        for i in range (0, globalInterpolation) :
            b = Entry(root2, font=("Helvetica", 20), borderwidth=2, relief="groove", width = 8 )
            b.grid(row = 0, column = i + 1)
            x_labels_as_list.append(b)
        for i in range (0, globalInterpolation) :
            b = Entry(root2, font=("Helvetica", 20), borderwidth=2, relief="groove", width = 8 )
            b.grid(row = 1, column = i + 1)
            fx_labels_as_list.append(b)
        btn = Button(root2, text = "get function وان", width = str(globalInterpolation*17),borderwidth=2, relief="groove", command = self.prepare_interpolation_sets)
        btn.grid(row = 2, columnspan = globalInterpolation+1)
        self.lblFunc = Label(root2, text="", font=("Helvetica", 9), fg = "black")
        self.lblFunc.grid(row=3, column=0, columnspan=50)

        self.lblFuncSimp = Label(root2, text="", font=("Helvetica", 15), fg="blue")
        self.lblFuncSimp.grid(row=4, column=0, columnspan=50)

    function_from_interpolation = ""
    def prepare_interpolation_sets(self):
        for i in range (0, len(x_labels_as_list)) :
            x_list.append(float(x_labels_as_list[i].get()))
        for i in range (0, len(fx_labels_as_list)) :
            fx_list.append(float(fx_labels_as_list[i].get()))
        global function_from_interpolation
        if(lagrange == False) :
            fn = Newton(x_list,fx_list)
            function_from_interpolation = fn.get_function()
        else :
            fn = LagrangeInterpolation()
            function_from_interpolation = fn.getFunction(x_list,fx_list)
        self.lblFunc.config(text=function_from_interpolation)
        function_from_interpolation = simplify(function_from_interpolation)
        s1 = 'F(x) = '
        s2 = str(function_from_interpolation)
        s3 = str(s1 + s2)
        print(s3)
        self.lblFuncSimp.config(text = s3 )


class InterpolationPopUp():
    def __init__(self):
        top=self.top=Toplevel(master)
        ws = top.winfo_screenwidth()
        hs = top.winfo_screenheight()
        x = (ws / 2) - (200 / 2)
        y = (hs / 2) - (100 / 2)
        top.geometry('%dx%d+%d+%d' % (200,100, x, y))
        #top.geometry('{}x{}'.format(200, 100))
        self.l=Label(top, font=("Helvetica", 16), width = 20, text="Interpolation Order")
        self.l.pack()
        self.e=Entry(top, font=("Helvetica", 16), width = 20)
        self.e.pack()
        self.b=Button(top, font=("Helvetica", 16),text='Done',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        global globalInterpolation
        globalInterpolation = int(self.e.get()) + 1
        self.top.destroy()
        i = InterpolationWindow()


class popupWindow():
    def __init__(self):
        top=self.top=Toplevel(master)
        ws = top.winfo_screenwidth()
        hs = top.winfo_screenheight()
        x = (ws / 2) - (200 / 2)
        y = (hs / 2) - (200 / 2)
        top.geometry('%dx%d+%d+%d' % (200, 150, x, y))
        #top.geometry('{}x{}'.format(200, 100))
        self.l=Label(top, font=("Helvetica", 16), width = 20, text="Enter value")
        self.l.pack()
        self.e=Entry(top, font=("Helvetica", 16), width = 20)
        self.e.pack()
        self.b=Button(top, font=("Helvetica", 16),text='Maximum Iterations',command=self.cleanup)
        self.b.pack()
        self.c = Button(top, font=("Helvetica", 16), text='Epsilon  Precision', command=self.cleanup2)
        self.c.pack()
    def cleanup(self):
        global globalValue
        globalValue = int(self.e.get())
        global MAX_ITERATIONS
        MAX_ITERATIONS = globalValue - 1;
        self.value=self.e.get()
        self.top.destroy()
    def cleanup2(self):
        global globalValue
        globalValue = float(self.e.get())
        global EPSILON_PRESICION
        EPSILON_PRESICION = globalValue;
        self.value=self.e.get()
        self.top.destroy()

# Functions ---------------------------------------------------------------------------------
def prepare_newton():
    label_current_method.config(text = "=> Newton Raphson <=  " , fg = 'GREEN')
    additional_entry2.grid_forget()
    global method
    method = 1
def prepare_fixed_point():
    label_current_method.config(text = "=> Fixed Point <=  " , fg = 'GREEN')
    additional_entry2.grid_forget()
    global method
    method = 3
def prepare_bisection():
    label_current_method.config(text = "=> Bisection <=  " , fg = 'GREEN')
    additional_entry2.grid(row=11, column=2, sticky=W)
    global method
    method = 2
def prepare_secant():
    label_current_method.config(text = "=> Secant <=  " , fg = 'GREEN')
    additional_entry2.grid(row=11, column=2, sticky=W)
    global method
    method = 4
def prepare_bierge_vieta():
    label_current_method.config(text = "=> Bierge Vieta <=  " , fg = 'GREEN')
    additional_entry2.grid_forget()
    global method
    method = 5
def prepare_false_position():
    label_current_method.config(text = "=> False Position <=  " , fg = 'GREEN')
    additional_entry2.grid(row=11, column=2, sticky=W)
    global method
    method = 6
def is_slow():
    label_current_mode.config(text = "=> Slow Iteration <=  " , fg = 'GREEN')
    global mode
    mode = 1
    root.geometry('{}x{}'.format(1100, 800))
    iterate.grid(row = 0, rowspan = 15 ,columnspan = 4,sticky= W, column = 0)
def is_chopping():
    global rounding
    rounding = False
def is_rounding():
    global rounding
    rounding = True
def on_entry_click(event):
    if functionEntry.get() == 'Enter the function':
        functionEntry.delete(0, "end")
        functionEntry.insert(0, '')
        functionEntry.config(fg = 'black')
def on_focusout(event):
    if functionEntry.get() == '':
        functionEntry.insert(0, 'Enter the function')
        functionEntry.config(fg = 'grey')
def is_fast():
    label_current_mode.config(text = "=> Fast Iteration <=  " , fg = 'GREEN')
    global mode
    mode = 0
    root.geometry('{}x{}'.format(730, 800))
    iterate.grid_forget()
def solve():
    function = functionEntry.get()
    initial = float(additional_entry.get())
    if additional_entry2.get() is not "" :
         initial2 = float(additional_entry2.get())
    # solver = EquationSolver(function, MAX_ITERATIONS, EPSILON_PRESICION)
    # solver.max_iterations = MAX_ITERATIONS
    # solver.precision =EPSILON_PRESICION
    # solver.__init__(function,MAX_ITERATIONS , EPSILON_PRESICION)
    global method
    global mode
    global instance
    if method == 1:
        instance = NewtonRaphson(function, initial, MAX_ITERATIONS , EPSILON_PRESICION)
        instance.get_root()
    elif method == 3:
        instance = FixedPoint(function, initial, MAX_ITERATIONS , EPSILON_PRESICION)
        instance.get_root()
    elif method == 2:
        instance = Bisection(function, initial, initial2,MAX_ITERATIONS , EPSILON_PRESICION)
        instance.get_root()
    elif method == 4:
        instance = Secant(function, MAX_ITERATIONS , EPSILON_PRESICION, initial, initial2)
        instance.start_root_finding()
    elif method == 5:
        instance = BiergeVieta(function, initial, MAX_ITERATIONS , EPSILON_PRESICION)
        instance.get_root()
    elif method == 6:
        instance = FalsePosition(function,initial, initial2, MAX_ITERATIONS , EPSILON_PRESICION)
        instance.get_root()
    height = len(instance.roots)

    if(mode == 0) :
        b = Label(frame_labels, borderwidth=2, relief="solid", text="i", font=("Courier", 12), width=5, fg="RED",
                  bg="YELLOW")
        b.grid(sticky='news', row=0, column=0)
        table_as_list.append(b)
        b = Label(frame_labels,borderwidth=2, relief="solid", text="Root", font=("Courier", 12), width=15, fg="RED", bg="YELLOW")
        b.grid(sticky='news', row=0, column=1)
        table_as_list.append(b)
        b = Label(frame_labels,borderwidth=2, relief="solid", text="Precision", font=("Courier", 12), width=15, fg="RED", bg="YELLOW")
        b.grid(sticky='news', row=0, column=2)
        table_as_list.append(b)
        width = 2
        global round_to

        for i in range(0, height):  # Rows
            f = 0
            g = 0
            if (i > 25):
                f = 26
                g = 3
            if (i > 51):
                f = 52
                g = 6
            if (i > 77):
                root.geometry('{}x{}'.format(1480, 800))
                f = 78
                g = 9
            b = Label(frame_labels, borderwidth=2, relief="groove", text=str(i + 1), font=("Courier", 12), width=5, fg="RED",
                      bg="YELLOW")
            b.grid(sticky='news', row=i+1-f, column=0+g)
            table_as_list.append(b)
            for j in range(0, width):  # Columns
                if j == 0 :
                    current_root = instance.roots[i].root
                    if current_root != None :
                        current_root = round(current_root, round_to)
                    r = str(current_root)
                    b = Label(frame_labels, borderwidth=2, relief="groove", text= r, font=("Courier", 12), width=15, fg="BLUE", bg="white")
                    b.grid(sticky='news', row=i + 1-f , column=j + 1+g)
                    table_as_list.append(b)

                else :
                    precision = instance.roots[i].precision
                    if precision != None :
                        precision = round(precision, round_to)
                    p = str(precision)
                    b = Label(frame_labels,borderwidth=2, relief="groove", text= p , font=("Courier", 12), width=15, fg="BLUE", bg="white")
                    b.grid(sticky='news', row=i + 1-f, column=j + 1+g)
                    table_as_list.append(b)
        plot = Plotter(function,instance.roots,0)
        plot.plot_equation()

    else :
        b = Label(frame_labels, borderwidth=2, relief="solid", text="i", font=("Courier", 12), width=5, fg="RED",
                  bg="YELLOW")
        b.grid(sticky='news', row=0, column=0)
        table_as_list.append(b)
        b = Label(frame_labels, borderwidth=2, relief="solid", text="Root", font=("Courier", 12), width=15, fg="RED",
                  bg="YELLOW")
        b.grid(sticky='news', row=0, column=1)
        table_as_list.append(b)
        b = Label(frame_labels, borderwidth=2, relief="solid", text="Precision", font=("Courier", 12), width=15, fg="RED",
                  bg="YELLOW")
        b.grid(sticky='news', row=0, column=2)
        table_as_list.append(b)
        global glob_i, glob_h
        glob_i = 0
        glob_h = height
        plot = Plotter(function, instance.roots, 1)
        plot.plot_equation()
        nextIteration()
def popup():
    w1 = popupWindow()
def popup2():
    global lagrange
    w2 = InterpolationPopUp()
    lagrange = False
def popup3():
    global lagrange
    lagrange = True
    w3 = InterpolationPopUp()
def createNew() :
    functionEntry.delete(0, 'end')
    functionEntry.config(fg = "black")
    additional_entry.delete(0, 'end')
    additional_entry2.delete(0, 'end')
    label_current_method.config(fg = "brown", text = "Please select method")
    label_current_mode.config(fg = "brown", text = "please select a mode")
    root.geometry('{}x{}'.format(730, 800))
    iterate.grid_forget()
    global table_as_list
    for i in range (0, len(table_as_list)) :
        table_as_list[i].grid_forget()
def nextIteration():
    global glob_i
    global glob_h
    global rounding
    if glob_i >=glob_h :
        return
    else :
        f=0
        g = 0
        if (glob_i > 25):
            f = 26
            g = 3
        if (glob_i > 51):
            f = 52
            g = 6
        if (glob_i > 77):
            root.geometry('{}x{}'.format(1480, 800))
            f = 78
            g = 9
        b = Label(frame_labels, borderwidth=2, relief="groove", text=str(glob_i + 1), font=("Courier", 12), width=5, fg="RED",
                  bg="YELLOW")
        b.grid(sticky='news', row=glob_i - f + 1, column=0 + g)
        table_as_list.append(b)
        current_root = instance.roots[glob_i].root
        if current_root != None :
            current_root = round(current_root, round_to)
        r = str(current_root)
        b = Label(frame_labels, borderwidth=2, relief="groove", text=r, font=("Courier", 12), width=15, fg="BLUE", bg="white")
        b.grid(sticky='news', row=glob_i - f + 1, column=1 + g)
        table_as_list.append(b)
        precision = instance.roots[glob_i].precision
        if precision != None :
          precision = round(precision, round_to)
        p = str(precision)
        b = Label(frame_labels, borderwidth=2, relief="groove", text=p, font=("Courier", 12), width=15, fg="BLUE", bg="white")
        b.grid(sticky='news', row=glob_i + 1 - f, column=2 + g )
        table_as_list.append(b)
        glob_i += 1

root = Tk()
root.title('Numerical Analysis')
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry('{}x{}'.format(730, 800))


canvas = Canvas(root, width = 800, height = 800)
canvas.grid(row = 20, column = 0, sticky="news",columnspan = 4)

frame_labels = Frame(canvas)
canvas.create_window((0, 0), window=frame_labels, anchor='nw')


# Labels-----------------------------------------------------------------------------------------

label_empty = Label(root, text = "Enter the function",font=("Helvetica", 20))
#label_empty.grid(row = 0, column = 1)

label_init = Label(root, text = "initials",font=("Courier", 15), fg = 'BLUE')
label_init.grid(row = 0, column = 2, sticky = W)


label_current_method = Label(root, text = "Please choose method  ", font=("Helvetica", 17), fg = 'brown')
label_current_method.grid(row = 7, column  = 2, sticky = E, rowspan = 5)

label_current_mode = Label(root, text = "Please choose a mode  ", font=("Helvetica", 17), fg = 'brown')
label_current_mode.grid(row = 11, column  = 2, sticky = E, rowspan = 5)

label_enter_function = Label(root, text = "                        ", font=("Courier", 20))
label_enter_function.grid(row = 10, column = 0)

# Entries-----------------------------------------------------------------------------------------

functionEntry = Entry(root, font=("Helvetica", 20), width = 23, fg = "grey")
functionEntry.grid(row = 10, column = 1)
functionEntry.insert(END, 'Enter the function')
functionEntry.bind('<FocusIn>', on_entry_click)
functionEntry.bind('<FocusOut>', on_focusout)

additional_entry = Entry(root, font=("Helvetica", 20), width = 5)
additional_entry.grid(row = 10, column = 2,sticky = W)

additional_entry2 = Entry(root, font=("Helvetica", 20), width = 5)
additional_entry2.grid(row = 11, column = 2,sticky = W)
additional_entry2.grid_forget()


# buttons---------------------------------------------------------------------------------------


evaluate = Button(root, text = "Solve",borderwidth=4,relief="groove", font=("Helvetica", 15), command = solve, width = 29)
evaluate.grid(row = 11, column = 1, sticky = W)

labell = Label(root, text="                                                                                          ")
labell.grid(row = 12, column = 2)

iterate = Button(root,borderwidth=4, bg="lightgrey", relief="groove", text = "Click to iterate",fg = "yellow", font=("Helvetica BOLD", 17), command = nextIteration, height = 3, width = 23)
iterate.grid(row = 3, rowspan = 5 ,columnspan = 2,sticky=W, column = 0)
iterate.grid_forget()

# menus------------------------------------------------------------------------------------------

menu = Menu(root, font=("Helvetica", 17), fg = "black")
root.config(menu = menu)
submenu = Menu(menu, font=("Helvetica", 18), borderwidth=2, relief="solid")
submenu0 = Menu(menu, font=("Helvetica", 18),borderwidth=2, relief="groove")
menu.add_cascade(label = "File | ", menu = submenu0)
submenu0.add_radiobutton(label = "New" ,command = createNew)
submenu0.add_radiobutton(label = "Exit" ,command = exit)

menu.add_cascade(label = "Methods | ", menu = submenu)
menu.add_separator()
submenu.add_radiobutton(label = "Newton's" ,command = prepare_newton)
submenu.add_radiobutton(label = "Fixed Point", command = prepare_fixed_point)
submenu.add_radiobutton(label = "Bisection" ,command = prepare_bisection)
submenu.add_radiobutton(label = "Secant" ,command = prepare_secant)
submenu.add_radiobutton(label = "Bierge Vieta", command = prepare_bierge_vieta)
submenu.add_radiobutton(label = "False Position", command = prepare_false_position)

submenu2 = Menu(menu, font=("Helvetica", 18),borderwidth=2, relief="groove")
menu.add_cascade(label = "Mode | ", menu = submenu2)
submenu2.add_radiobutton(label = "Slow" ,command = is_slow)
submenu2.add_radiobutton(label = "Fast" ,command = is_fast)


submenu3 = Menu(menu, font=("Helvetica", 18),borderwidth=2, relief="groove")
menu.add_cascade(label = "Approximation | ", menu = submenu3)
submenu3.add_radiobutton(label = "Rounding" ,command = is_rounding)
submenu3.add_radiobutton(label = "Chopping" ,command = is_chopping)

submenu4 = Menu(menu, font=("Helvetica", 18),borderwidth=2, relief="groove")
menu.add_cascade(label = "Constants | ", menu = submenu4)
submenu4.add_radiobutton(label = "Precision" ,command = popup)
submenu4.add_radiobutton(label = "Maximum Iteration" ,command = popup)
submenu4.add_radiobutton(label = "Segnificant Figures" ,command = popup)

submenu5 = Menu(menu, font=("Helvetica", 18),borderwidth=2, relief="groove")
menu.add_cascade(label = "Interpolation", menu = submenu5)
submenu5.add_radiobutton(label = "Newton's Interpolation" ,command = popup2)
submenu5.add_radiobutton(label = "Lagrange Interpolation" ,command = popup3)



frame = Frame(root)
frame.grid(sticky = W, row = 20, columnspan = 6)
root.mainloop()


