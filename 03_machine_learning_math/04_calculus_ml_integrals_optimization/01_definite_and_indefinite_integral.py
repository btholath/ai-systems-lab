import sympy as sp                # bring in sympy so we can do symbolic math

# Define the variable x and the function f(x) = e^(–x)
x = sp.Symbol('x')               
f = sp.exp(-x)                   

# Compute the indefinite integral ∫ e^(–x) dx = –e^(–x) + C
indefinite_integral = sp.integrate(f, x)  
print("Indefinite integral: ", indefinite_integral)

# Compute the definite integral ∫₀^∞ e^(–x) dx = 1
definite_integral = sp.integrate(f, (x, 0, sp.oo))  
print("Definite integral: ", definite_integral)