def f(x):
    return x**4 - 3*x - 20

# Функция phi(x) задается по уравнению x = phi(x) для уравнения x^4 - 3*x - 20 = 0
def phi_1(x):
    return (x**4 - 20) / 3

def phi_2(x):
    return ((3*x + 20)**0.25)

# в цикле последовательно вычисляем x0, x1, x2, ..., пока |x_i - x_(i-1)| не станет меньше заданной точности e
def simple_iteration_method(phi, initial_guess, e):
    count = 0
    prev_x = initial_guess
    cur_x = phi(prev_x)
    while abs(cur_x - prev_x) > e:
        prev_x = cur_x
        cur_x = phi(cur_x)
        count += 1
    return cur_x, count

initial_guess = 3 # Начальное приближение
e = 0.01

solution, iterations = simple_iteration_method(phi_2, initial_guess, e)
residual = f(solution)
print(f"Приближенное решение уравнения: {solution}")
print(f"Остаток уравнения при подстановке полученного корня: {residual}")
print(f"Количество итераций: {iterations}")