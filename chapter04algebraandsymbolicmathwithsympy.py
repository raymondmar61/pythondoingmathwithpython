#Chapter 4 Algebra And Symbolic Math With Sympy

from sympy import Symbol, symbols
x = Symbol("x")
print(x + x + 1) #print 2*x + 1
a = Symbol("x")
print(a + a + 1) #print 2*x + 1.  Instructor recommends a label matching the same letter with the symbol.
print(x.name) #print x
x,y,z = symbols("x,y,z")
print(x.name) #print x
print(y.name) #print y
print(z.name) #print z
print((x*y)+(x*y)) #print 2*x*y
print(x*(x+x)) #print 2*x**2
print((x + 2)*(x + 3)) #print (x + 2)*(x + 3)  RM:  not (x**2+2*x)+(3*x+6)-->x**2+5*x+6

from sympy import factor, expand
x = Symbol("x")
y = Symbol("y")
expression = x**2 - y**2
print(factor(expression)) #print (x - y)*(x + y)
factors = factor(expression)
print(expand(factors)) #print x**2 - y**2
expression = (x**3 + 3*x**2*y + 3*x*y**2 + y**3)
factors = factor(expression)
print(factors) #print (x + y)**3
print(expand(factors)) #print (x**3 + 3*x**2*y + 3*x*y**2 + y**3)
#If there is a expression for which there's no factorization, then the original expression is returned.  Likewise for an expression.
expression = x + y + x*y
print(factor(expression)) #print x*y + x + y

from sympy import pprint, init_printing
expression = x*x + 2*x*y + y*y
print(factor(expression)) #print (x + y)**2
pprint(expression)
'''
 2            2
x  + 2⋅x⋅y + y 
'''
expression = 1 + 2*x + 2*x**2
print(factor(expression)) #print 2*x**2 + 2*x + 1
pprint(expression)
'''
   2          
2⋅x  + 2⋅x + 1
'''
#If you want the expression in the opposite order, with the highest power of x last, you can make that happen with the init_printing() function.
expression = 1 + 2*x + 2*x**2
init_printing(order="rev-lex")
pprint(expression)
'''
   2          
2⋅x  + 2⋅x + 1
'''
#RM:  init_printing(order="rev-lex") didn't print the opposite order
#RM:  skipped the rest of the chapter.  I don't see practical purposes in my future career.