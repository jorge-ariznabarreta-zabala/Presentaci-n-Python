def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la cuenta_atras", num+1)


print("*******************")
def factorial(num):
     print("Valor inicial ->",num)
     if num > 1:
         num = num * factorial(num -1)
     print("valor final ->",num)
     return num

