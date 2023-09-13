# Создайте функцию генератор чисел Фибоначчи 

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
fib = fibonacci_generator()
for i in range(10):
    print(next(fib))