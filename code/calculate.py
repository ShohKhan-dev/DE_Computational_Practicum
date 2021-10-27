
import math


def f(x, y):  # canculates general solution 
    
    result = round((5-x**2-y**2+2*x*y), 5) 

    return result


def y(x):  # calcuates y, exact solution
    
    #x = min(4, x)
    return 4/(-3*pow(math.e, 4*x)-1) +x+2 


def cal_steps(x0, b, n):  # canculates h (step)
    h = round((b - x0) / (n-1), 3)

    h = min(h, 0.6)  # result will exceed from limit when h is greater than 0.6, that's why it takes minimum.

    x = []
    for i in range(0, n):
        
        x.append(round(x0 + i * h, 3))

    return h, x



def exact_solution(x0, y0, b, n):  # calculates exact solution
    
    h, x = cal_steps(x0, b, n)

    e = []
    for i in range(n):
        e.append(round(y(x[i]), 5))

    exact = [x, e]


    return exact


def euler_method(x0, y0, b, n):   # calculates euler method

    h, x = cal_steps(x0, b, n)

    y = [y0]
    for i in range(1, n):

        y.append(round(y[i - 1] + h * f(x[i - 1], y[i - 1]), 5))

    euler = [x, y]

    return euler


def improved_euler_method(x0, y0, b, n): # calculates improved euler method

    h, x = cal_steps(x0, b, n)

    y = [y0]
    for i in range(1, n):
        
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h, y[i - 1] + h * k1)
        
        y.append(round(y[i - 1] + (h / 2) * (k1 + k2), 5))

    improved = [x, y]


    return improved


def runge_kutta_method(x0, y0, b, n):  # calculates runge-kutta method 

    h, x = cal_steps(x0, b, n)

    y = [y0]
    for i in range(1, n):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k1)
        k3 = f(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)
        y.append(round(y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4), 5))

    runge_kutta = [x, y]


    return runge_kutta



def compute_error(method1, method2):  # compute difference between numerical method and exact solution at each step
    m = len(method1)
    answer = m * [0]
    for i in range(m):
        answer[i] = abs(method1[i] - method2[i])


    return answer


def investigate_convergence(error):  # check if any error doesn't tend to 0, in that case method is not convergent
    for element in error:
        if round(element) != 0:
            print(" is not convergent.")
            return
    print(" is convergent.")
