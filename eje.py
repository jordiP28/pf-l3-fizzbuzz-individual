def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
 
if __name__ == "__main__":
    # Importante: El test 3 pide hasta el 1000.
    # Al imprimir 1000, los tests de 10 y 100 pasarán porque
    # usan el operador 'in' (buscan si su pedazo está dentro de tu salida).
    fizzbuzz(1000)