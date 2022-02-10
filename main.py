# https://docs.sympy.org/latest/tutorial/intro.html#what-is-symbolic-computation
from sympy import *

x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)

# Take a derivative of sin(x)*e**x
print(diff(sin(x) * exp(x), x))

# Compute Integral
print(integrate(exp(x) * sin(x) + exp(x) * cos(x), x))

# Compute another integral from -infinity to +infinity
print(integrate(sin(x ** 2), (x, -oo, 00)))

# Calculate limit of sin(x)/x
print(limit(sin(x) / x, x, 0))

# Solve the equation x**2 - 2 = 0
print(solve(x ** 2 - 2, x))

# Solve differential equation y**n - y = e**t
y = Function('y')
print(dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))

# Find eigenvalues of [1 2][2 2]
print(Matrix([[1, 2], [2, 2]]).eigenvals())

# Rewrite the Bessel function
print(besselj(nu, z).rewrite(jn))

# Print equation in Latex
print(latex(Integral(cos(x) ** 2, (x, 0, pi))))
