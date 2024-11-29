import sympy as sp #import sympy
x = sp.symbols('x') #set symbols for variables
h = sp.symbols('h')

f = sp.tan((x+h)) #define functions 
f_int = sp.integrate(f,x) #integrate function f by varaible x 

print(f'antiderivative: {f_int}',
      f'\nLaTeX: {sp.latex(f_int)}') 
#sp.latex printout preferred if code editor does not display math figures
