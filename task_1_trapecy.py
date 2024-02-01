def f(x):
    return 1 / (1 + x**2)

def trapezoid_method(a, b, n, func, epsilon):
    # Инициализация шага и первоначального приближения интеграла
    h = (b - a) / n
    # Вычисление значения функции на левой границе отрезка
    left_term = 0.5 * func(a)

    # Вычисление значения функции на равномерной сетке, без учета крайних точек (сами трапеции)
    middle_terms = [func(a + i*h) for i in range(1, n)]

    # Вычисление значения функции на правой границе отрезка
    right_term = 0.5 * func(b)

    # Комбинирование всех термов вместе и умножение на шаг h
    integral_prev = h * (left_term + sum(middle_terms) + right_term)

    while True:
        h /= 2
        # Множество точек, в которых вычисляется функция при уменьшении шага в 2 раза (точки между прежними точками)
        x = [a + i*h for i in range(1, 2*n, 2)]
        # Вычисляем значения функции в новых точках
        func_values = []
        for x_coord in x:
            func_values.append(func(x_coord))

        # Обновляем приближение интеграла
        integral_curr = 0.5 * integral_prev + h * sum(func_values)
        # Проверка условия окончания
        if abs(integral_curr - integral_prev) < epsilon:
            return integral_curr, int(h / (b - a))
        
        integral_prev = integral_curr
        n *= 2

a = 0
b = 1
epsilon = 0.785

approx, steps = trapezoid_method(a, b, 2, f, epsilon)
print("Приближенное значение интеграла: ", approx)
print("Количество шагов разбиения: ", steps)