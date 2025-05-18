import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_sqrt(n):
    if n == 0:
        return (0, 1)
    factor = 1
    for i in range(2, int(math.isqrt(abs(n))) + 1):
        while n % (i * i) == 0:
            factor *= i
            n //= i * i
    return (factor, n)

def solve_quadratic():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "Coefficient 'a' cannot be zero.")
            return

        d = b ** 2 - 4 * a * c
        two_a = 2 * a

        if d > 0:
            root_factor, remaining = simplify_sqrt(d)
            if remaining == 1:
                root_val = root_factor
                num1 = Fraction(-b + root_val, two_a)
                num2 = Fraction(-b - root_val, two_a)
                result = f"Two real solutions:\nx = {num1}\nx = {num2}"
            else:
                g = gcd(gcd(abs(b), abs(root_factor)), abs(two_a))
                result = f"Simplified radical form:\nx = ({-b//g} ± {root_factor//g}√{remaining}) / {two_a//g}"
        elif d == 0:
            root = Fraction(-b, two_a)
            result = f"One real solution:\nx = {root}"
        else:
            d = -d
            root_factor, remaining = simplify_sqrt(d)
            if remaining == 1:
                root_val = root_factor
                g = gcd(gcd(abs(b), abs(root_val)), abs(two_a))
                result = f"Two imaginary solutions:\nx = ({-b//g} ± {root_val//g}i) / {two_a//g}"
            else:
                g = gcd(gcd(abs(b), abs(root_factor)), abs(two_a))
                result = f"Imaginary solutions in radical form:\nx = ({-b//g} ± {root_factor//g}√{remaining}i) / {two_a//g}"

        messagebox.showinfo("Solution", result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for a, b, and c.")

root = tk.Tk()
root.title("QuadraticSolver")
root.geometry("300x220")

tk.Label(root, text="Enter a:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Enter b:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Enter c:").pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack()

solve_btn = tk.Button(root, text="Solve", command=solve_quadratic)
solve_btn.pack(pady=20)

root.mainloop()