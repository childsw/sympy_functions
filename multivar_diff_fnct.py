import sympy as sp # import sympy
[x,y,z,h,j] = sp.symbols(['x','y','z','h','j'])
# define variables with sp.symbols [ensure list order matches variable order]

f = (3*x**2)*(sp.sin(z-h))/(sp.log(2*(y-8*j))) #define functions 
f_prime = sp.diff(f, x, y, z) #differentiate function, f, by varaibles x, y, z

print(f'derivative: {f_prime}',
      f'\nLaTeX: {sp.latex(f_prime)}') 
#sp.latex printout preferred if code editor does not display math figures
