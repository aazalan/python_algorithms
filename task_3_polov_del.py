def f(x):
    return x**4 - 3*x - 20

def bisection_method(f, a, b, e):
    if f(a) * f(b) > 0:
        raise ValueError("Функция f должна иметь разные знаки на концах интервала [a, b]")

    count = 0  
    while (b - a) / 2 > e:
        count += 1  
        midpoint = (a + b) / 2
        if f(midpoint) == 0:  # Нашли точный корень
            return midpoint, count
        elif f(midpoint) * f(a) < 0:  # Корень находится в левой половине
            b = midpoint
        else:  # Корень находится в правой половине
            a = midpoint

    # Возвращаем среднюю точку последнего интервала и количество итераций
    return (a + b) / 2, count


a = 0
b = 5 
e = 0.01

solution, counter = bisection_method(f, a, b, e)
residual = f(solution)
print(f"Приближенное решение уравнения: {solution}")
print(f"Остаток уравнения при подстановке полученного корня: {residual}")
print(f"Количество итераций: {counter}")
