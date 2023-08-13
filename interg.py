import sympy as sp

x = sp.symbols('x')
integral_expr = sp.sin(x)*sp.cos(x)

indefinite_integral = sp.integrate(integral_expr, x)
print(indefinite_integral)
