# Math Library
# Author: Hadrien Hachez
# Version: February 3, 2016

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if(n<0):
        raise ValueError
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -integrate('x ** 2 - 1', -1, 1)
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta=b**2-4*a*c
    if a!=0:
        if delta>0:
            x1=(-b-delta**(1/2))/(2*a)
            x2=(-b+delta**(1/2))/(2*a)
            result=(x1,x2)
        elif delta==0:
            result=-b/(2*a)
        else:
            result=()
    elif b!=0:
        result=-c/b
    else:
        result=()
    return result
    
        
        

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    step=(upper-lower)/10000
    x=lower
    result=0
    while x<upper:
        result+=eval(function)*step
        x+=step
    return result
    

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
