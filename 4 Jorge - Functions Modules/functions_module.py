# Fibonacci numbers module functions_module.py
'''Module managing to supply Fibonacci series'''
def my_function():
    '''This function is an example'''
    print('Hello, my first function');

def fib(n):
    ''' write Fibonacci series up to n '''
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