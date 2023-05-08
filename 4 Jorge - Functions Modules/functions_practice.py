import functions_module as fm  # imports functions from functions_module
import recursive

print('111 Escribe las funciones disponibles en fm 111 \n', dir(fm))
#print('222 Escribe las funciones disponibles 222 \n', fm.__dir__())
#print('555 Escribe la ayuda del modulo importado 555 \n', help(fm.fib))
print()
print('666 Escribe la info que metemos entre 3 comillas 666 \n', fm.__doc__)
print()


#print('Escribe el objeto importado', fm)

print('*** Series Fibbonacci ***')
  # write Fibonacci series up 1000

print ('fibonaci = fm.fib  # assing function to fib variable \n fibonaci(500)  # write Fibonacci series up 500 thru the variable')
fibonaci = fm.fib  # assing function to fib variable
fibonaci(500)  # write Fibonacci series up 500 thru the variable
print()
print('prints the list that is returned by fib2 funtion in module =>fm.fib2(100)',fm.fib2(100)) # prints the list that is returned by fib2 funtion in module
print()
recursive.cuenta_atras(9)
print()
recursive.factorial(5)