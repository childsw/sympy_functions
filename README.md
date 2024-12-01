# sympy_functions
Lab 7 for CS256 in Fall 2024. Program for single and multi varialbe derivatives, basic-integrals, and common ODEs. 

You will need to install sympy for these functions to work

For each derivative and antiderivatives:
  1. Import sympy as sp
  2. Define variables with sp.symbols
  3. Define a function using terms recognized by sympy
  4. Find the derivative or antiderivative with sp.diff or sp.integral
  5. Print (optionally with sp.latex for easier display dependent on platform)
  
Sympy is able to calculate all derivatives but struggles with complex integrals esspecially involving substitution.
If the substitution is done ahead of time it is rarely an issue.

For each ODE:
  1. Import sympy as sp
