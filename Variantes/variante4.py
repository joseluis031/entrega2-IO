# Modelo 1V4
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
#y=4
f3 = "4" #<=
#creame una linea paralela al eje x que pase por 16
#creame una linea paralela al eje x que pase por 14
#creame una linea paralela al eje x que pase por 13
Z1 = "(5)"
Z2 = "(6)"
Z3 = "(7)"


x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -1, 15))