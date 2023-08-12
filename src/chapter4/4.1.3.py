import matplotlib.pyplot as plt 
import numpy as np 

def main():
    a()
    b()
    c()
    d()

def a():
    plt.figure()

    def fn(x):
        return x**2.0 - x - 2

    x = np.linspace(-10, 10, 1000)
    y = fn(x)
    
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of y = x^2 - x - 2")
    plt.savefig("src/chapter4/a.png")

def b():
    plt.figure()
    x = np.linspace(-10, 10, 1000)

    # Define the corresponding y values
    y = x

    # Create the plot

    # Plot the line y = x
    plt.plot(x, y, "b-", label="y = x")

    # Shade the area where y < x
    plt.fill_between(x, y, -10, color="lightcoral", alpha=0.5, label="y < x")

    # Set labels and title
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of y < x")
    plt.legend()
    plt.grid()
    plt.savefig("src/chapter4/b.png")

def c():
    plt.figure()
    def fn(x):
        return x**2.0 - x - 2

    def fn2(x):
        return 3*x - 2

    x = np.linspace(-10, 10, 1000)
    y = fn(x)

    plt.plot(x, y, label="y = x^2 - x - 2")

    y = fn2(x)

    plt.plot(x, y, label="y = 3x - 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of y = x^2 - x - 2 and y = 3x - 2")
    plt.legend()
    plt.savefig("src/chapter4/c.png")

def d(): 
    plt.figure()
    def fn(x):
        return x**2.0 - x - 2

    def fn2(x):
        return 3*x - 2

    x = np.linspace(-5, 5, 1000)
    y = fn(x)

    new_x = []
    new_y = []
    for (a, b) in zip(x, y):
        if b < a:
            new_x.append(a)
            new_y.append(b)
    

    plt.plot(np.array(new_x), np.array(new_y), label="y = x^2 - x - 2")

    y = fn2(x)

    new_x = []
    new_y = []
    for (a, b) in zip(x, y):
        if b < a:
            new_x.append(a)
            new_y.append(b)

    plt.plot(np.array(new_x), np.array(new_y), label="y = 3x - 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of y = x^2 - x - 2 and y = 3x - 2, where y < x")
    plt.legend()
    plt.savefig("src/chapter4/d.png")
    

if __name__ == "__main__":
    main()