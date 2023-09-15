#Функция factorial вычисляет факториал числа n.
def factorial(n):

    if n == 0: # Если n равно 0, то функция возвращает 1 (базовый случай).
        return 1
    # Иначе, функция вызывает саму себя с аргументом n-1 и умножает результат на n
    return n * factorial(n-1)

factorial_number = factorial(5)
print(factorial_number)

