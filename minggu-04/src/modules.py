def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

import fibo
fibo.fib(1000)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
fibo.fib2(100)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibo.__name__
#'fibo'
fib = fibo.fib
fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib, fib2
fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import *
fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo as fib
fib.fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib as fibonacci
fibonacci(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

import sys
sys.ps1
#'>>> '
sys.ps2
#'... '
sys.ps1 = 'C> '
#C> print('Yuck!')
#Yuck!
#C>

import fibo
import sys
sys.path.append('/ufs/guido/lib/python')

import fibo, sys
dir(fibo)
#['__name__', 'fib', 'fib2']

import fibo, sys
dir(sys) 

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
import builtins
dir(builtins)  

import builtins
dir(builtins)  