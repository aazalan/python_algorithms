def f(x):
    return x**4 - 3*x - 20

def hord_method(f, a, b, e):
    if f(a) * f(b) > 0:
        raise ValueError("Функция f должна иметь разные знаки на концах интервала [a, b]")

    count = 0 
    c = b - (f(b) * (b - a)) / (f(b) - f(a)) 
    while abs(f(c)) > e:
        count += 1  
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = b - (f(b) * (b - a)) / (f(b) - f(a)) 

    return c, count

a = 1
b = 4
e = 0.01

solution, iterations = hord_method(f, a, b, e)
residual = f(solution)
print(f"Приближенное решение уравнения: {solution}")
print(f"Остаток уравнения при подстановке полученного корня: {residual}")
print(f"Количество итераций: {iterations}")