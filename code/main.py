from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import calculate as cal



x0 = 0
y0 = 1
b = 20
n = 40
n1 = 10  # start of the interval
n2 = 30 # end of the interval



root = Tk()
root.wm_title("DE Computation Practicum")  # set tkinter window

fig = Figure(figsize=(6, 5), dpi=100)  # graph size set

t = np.arange(0, 3, .01)
plt = fig.add_subplot()

# plt.plot(t, 2 * t)
# plt.plot(t, 3*t)
plt.set_title("Graph Window!")
# plt.legend(['First line', 'Second line'])


frame = Frame(root, width=600)
frame.pack(side=RIGHT, expand=1)

frame2 = Frame(root)
frame2.pack(side=TOP, fill=X, expand=0)


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

toolbar.pack(side=BOTTOM, fill=X)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH)




class PlotGraph:


    def plotMethods(exact, euler, improved, runge_kutta, checks):
        
        global canvas, toolbar, plt
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        plt.remove()
        plt = fig.add_subplot()


        
        line1, = plt.plot(exact[0], exact[1])

        lines = [line1]
        names = ['Exact solution']

        if checks[0] == 1:
            line2, = plt.plot(euler[0], euler[1])
            lines.append(line2)
            names.append('Euler method')

        if checks[1] == 1:
            line3, = plt.plot(improved[0], improved[1])
            lines.append(line3)
            names.append('Improved Euler method')

        if checks[2] == 1:
            line4, = plt.plot(runge_kutta[0], runge_kutta[1])
            lines.append(line4)
            names.append('Runge-Kutta method')

        plt.legend(lines,names)
        plt.set_title("Methods")

        
        canvas = FigureCanvasTkAgg(fig, master=root)  
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        toolbar.pack(side=BOTTOM, fill=X)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
        


    def plotErrors(error1, error2, error3, checks):
        

        global canvas, toolbar, plt
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        plt.remove()
        plt = fig.add_subplot()

        lines = []
        names = []

        if checks[0] == 1:
            err_line1, = plt.plot(error1)
            lines.append(err_line1)
            names.append('Euler method error')
        
        if checks[1] == 1:
            err_line2, = plt.plot(error2)
            lines.append(err_line2)
            names.append('Improved Euler method error')
        
        if checks[2] == 1:
            err_line3, = plt.plot(error3)
            lines.append(err_line3)
            names.append('Runge-Kutta method error')
        
        plt.legend(lines,names)


        plt.set_title("Local Errors")
        canvas = FigureCanvasTkAgg(fig, master=root) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        toolbar.pack(side=BOTTOM, fill=X)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)


    def plot_total_errors(x0, y0, b, n1, n2, checks):

        global canvas, toolbar, plt
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        plt.remove()
        plt = fig.add_subplot()

        total_errors_e = []  # Euler
        total_errors_ie = []  # Improved Euler
        total_errors_rk = []  # Runge-Kutta
        for i in range(n1, n2):
            # values of exact solution and numerical methods when we use i computational steps
            exact_i = cal.exact_solution(x0, y0, b, i)
            euler_i = cal.euler_method(x0, y0, b, i)
            improved_i = cal.improved_euler_method(x0, y0, b, i)
            runge_kutta_i = cal.runge_kutta_method(x0, y0, b, i)

            # compute their errors
            error1_i = cal.compute_error(exact_i[1], euler_i[1])
            error2_i = cal.compute_error(exact_i[1], improved_i[1])
            error3_i = cal.compute_error(exact_i[1], runge_kutta_i[1])

            # append average values of errors
            total_errors_e.append(sum(error1_i) / i)
            total_errors_ie.append(sum(error2_i) / i)
            total_errors_rk.append(sum(error3_i) / i)

        #print(total_errors_e, total_errors_ie, total_errors_rk)

        lines = []
        names = []

        if checks[0] == 1:
            err_line1, = plt.plot(total_errors_e)
            lines.append(err_line1)
            names.append('Euler method error')

        if checks[1] == 1:
            err_line2, = plt.plot(total_errors_ie)
            lines.append(err_line2)
            names.append('Improved Euler method error')
        
        if checks[2] == 1:
            err_line3, = plt.plot(total_errors_rk)
            lines.append(err_line3)
            names.append('Runge-Kutta method error')
        
        plt.legend(lines,names)

        plt.set_title("Global Errors")


        canvas = FigureCanvasTkAgg(fig, master=root)  
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        toolbar.pack(side=BOTTOM, fill=X)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)


pg = PlotGraph

class TkMenu:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.but = False
        self.warn = False
    
        self.inputs()


    
    def inputs(self):
        l1 = Label(self.root, text="x0: ")
        l1.grid(row=0, column=0)
        self.var_x0 = Entry(self.root, width=10)
        self.var_x0.insert(0, x0)
        self.var_x0.grid(row=0, column=1, pady=4)

        l2 = Label(self.root, text="y0: ")
        l2.grid(row=1, column=0)
        self.var_y0 = Entry(self.root, width=10)
        self.var_y0.insert(0, y0)
        self.var_y0.grid(row=1, column=1, pady=4)

        l3 = Label(self.root, text="X: ")
        l3.grid(row=2, column=0)
        self.var_b = Entry(self.root, width=10)
        self.var_b.insert(0, b)
        self.var_b.grid(row=2, column=1, pady=4)

        l4 = Label(self.root, text="N:")
        l4.grid(row=3, column=0)
        self.var_n = Entry(self.root, width=10)
        self.var_n.insert(0, n)
        self.var_n.grid(row=3, column=1, pady=4)

        l5 = Label(self.root, text="N1: ")
        l5.grid(row=4, column=0)
        self.var_l = Entry(self.root, width=10)
        self.var_l.insert(0, n1)
        self.var_l.grid(row=4, column=1, pady=4)

        l5 = Label(self.root, text="N2: ")
        l5.grid(row=5, column=0)
        self.var_r = Entry(self.root, width=10)
        self.var_r.insert(0, n2)
        self.var_r.grid(row=5, column=1, pady=4)

        submit = Button(self.root, text="Apply", command=self.buttons, fg="red")
        submit.grid(row=9, column=1, pady=4)

        self.var1 = IntVar()
        Checkbutton(self.root, text="Euler", variable=self.var1).grid(row=6, column=1, sticky="W")
        self.var2 = IntVar()
        Checkbutton(self.root, text="Improved Euler", variable=self.var2).grid(row=7, column=1, sticky="W")
        self.var3 = IntVar()
        Checkbutton(self.root, text="Runge Kutta", variable=self.var3).grid(row=8, column=1, sticky="W")


    def get_values(self):

        try:
            global x0, y0, b, n, n1, n2
            x0 = int(self.var_x0.get())
            y0 = int(self.var_y0.get())
            b = int(self.var_b.get())
            n = int(self.var_n.get())
            n1 = int(self.var_l.get())
            n2 = int(self.var_r.get())

            n1 = max(x0, n1)
            n2 = min(n, n2)
            

        except Exception:
            return False

        else:
            return True

    def convergency(self):

        print("Euler method", end="")
        cal.investigate_convergence(self.error1)
        print("Improved Euler method", end="")
        cal.investigate_convergence(self.error2)
        print("Runge-Kutta method", end="")
        cal.investigate_convergence(self.error3)

    
    def calculating(self):
        eul = self.var1.get()
        imp_eul = self.var2.get()
        run_kut = self.var3.get()

        self.checks = [eul, imp_eul, run_kut]

    

        self.exact = cal.exact_solution(x0, y0, b, n)
        self.euler = cal.euler_method(x0, y0, b, n)
        self.improved = cal.improved_euler_method(x0, y0, b, n)
        self.runge_kutta = cal.runge_kutta_method(x0, y0, b, n)

        self.error1 = cal.compute_error(self.exact[1], self.euler[1])
        self.error2 = cal.compute_error(self.exact[1], self.improved[1])
        self.error3 = cal.compute_error(self.exact[1], self.runge_kutta[1])
        

    

    def buttons(self):

        if self.get_values():

            self.calculating()
        
            self.clear_place()

            
            pg.plotMethods(self.exact, self.euler, self.improved, self.runge_kutta, self.checks)

            
            self.methods_btn =  Button(self.frame, text="Methods", command=self.method_show, fg="red")
            self.methods_btn.grid(row=0, column=0, padx=1)
            self.methods_btn.configure(bg="yellow")

            self.local_btn =  Button(self.frame, text="Local Errors", command=self.local_show, fg="blue")
            self.local_btn.grid(row=0, column=1, padx=1)

            self.global_btn =  Button(self.frame, text="Global Errors", command=self.global_show, fg="green")
            self.global_btn.grid(row=0, column=2, padx=1)

            self.but = True

            self.convergency()
            


        else:
            self.clear_place()


            self.warning = Label(self.frame, text="Please fill all inputs with numbers!", fg="red")
            self.warning.grid(row=0, column=0, padx=200)
            

            self.warn = True


    def clear_place(self):

        if self.but:
            self.methods_btn.destroy()
            self.local_btn.destroy()
            self.global_btn.destroy()
            self.but = False

        if self.warn:
            self.warning.destroy()
            self.warn = False


    def method_show(self):
        self.methods_btn.configure(bg="yellow")
        self.local_btn.configure(bg="white")
        self.global_btn.configure(bg="white")
        pg.plotMethods(self.exact, self.euler, self.improved, self.runge_kutta, self.checks)


    def local_show(self):
        self.local_btn.configure(bg="yellow")
        self.methods_btn.configure(bg="white")
        self.global_btn.configure(bg="white")
        pg.plotErrors(self.error1, self.error2, self.error3, self.checks)


    def global_show(self):
        self.global_btn.configure(bg="yellow")
        self.local_btn.configure(bg="white")
        self.methods_btn.configure(bg="white")
        pg.plot_total_errors(x0, y0, b, n1, n2, self.checks)




robot = TkMenu(frame, frame2)



mainloop()