# Modelo 1v3
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
f3 = "4" #<=
f4 = "0" #<=
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))