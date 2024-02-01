def f(x):
    return 1 / (1 + x**2)

def list_areas(a, n, h, func, counter):
    # Создание пустого списка для площадей прямоугольников
    areas = []
    # Цикл по каждому из n прямоугольников
    for i in range(n):
        # Вычисляем координату x для i-ого прямоугольника
        x = a + i*h
        # Вычисляем значение функции в точке x
        func_value = func(x)
        # Вычисляем площадь i-ого прямоугольника и добавляем в список
        areas.append(h * func_value)
        counter += 1
    return areas, counter


# Функция для нахождения интеграла методом прямоугольников
def rectangle_method(a, b, n, func, epsilon):
    counter = 0
    # Разбиваем отрезок [a, b] на равные части
    h = (b - a) / n
    # Вычисляем списком включения все площади прямоугольников
    areas_prev, counter = list_areas(a, n, h, func, counter)
    n *= 2 # Увеличиваем число прямоугольников в 2 раза
    while True: # Цикл, который будет исполняться до достижения необходимой точности
        h = (b - a) / n # Перевычисляем ширину прямоугольника
        # Вычисляем новую сумму площадей прямоугольников
        areas_curr, counter = list_areas(a, n, h, func, counter)
        # Если разница между старой и новой суммами меньше заданной точности, останавливаем цикл
        if abs(sum(areas_curr) - sum(areas_prev)) < epsilon:
            break
        areas_prev = areas_curr # Сохраняем текущую сумму как предыдущую для следующей итерации
        n *= 2 # Увеличиваем число прямоугольников в 2 раза
    # Возвращаем сумму площадей прямоугольников
    integral_approx = sum(areas_curr)
    return integral_approx, n, counter # Возвращаем приближенное значение интеграла и количество шагов разбиения

a = 0
b = 1
epsilon = 0.785 # Задаём точность
counter = 0

approx, steps, counter = rectangle_method(a, b, 2, f, epsilon)

import math

exact_value = math.atan(b) - math.atan(a) # Вычисляем точное значение интеграла по формуле
error = abs(exact_value - approx) # Вычисляем погрешность

print("Приближенное значение интеграла: ", approx)
print("Количество шагов разбиения: ", steps)
print("Количество прохождений по циклу: ", counter)
print("Абсолютная погрешность: ", error)