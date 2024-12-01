import sympy as sp # import sympy
x = sp.symbols('x') #set symbols for variables
h = sp.symbols('h')

f = sp.acos(sp.log((x-h)**.5)) #define functions 
f_prime = sp.diff(f, x) #differentiate function f by varaible x 

print(f'derivative: {f_prime}',
      f'\nLaTeX: {sp.latex(f_prime)}') 
#sp.latex printout preferred if code editor does not display math figures
