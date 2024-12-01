import sympy as sp # import sympy
x = sp.symbols('x') # set symbol
y = sp.Function('y')(x) # set function

eq = sp.Eq((x*y.diff(x)-2*y),((x**5)*sp.sin(2*x)-x**3+4*x**4)) # define diff eq
sol = sp.dsolve(eq, y) #solve de

print(f'derivative: {sol}',
      f'\nLaTeX: {sp.latex(sol)}') 
#sp.latex printout preferred if code editor does not display math figures
