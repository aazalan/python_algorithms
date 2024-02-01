def norma(a, b):
    max = abs(a[0] - b[0])
    for i in range(1, len(a)):
        if abs(a[i] - b[i]) > max:
            max = abs(a[i] - b[i])
    return max

def iterate(x):
    counter = 0
    while True:
        counter += 1
        x_new = b.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        if norma(x_new, x) < e:
            break
        x = x_new
    return x, counter


A = [[5, 0, 1], [1, 3, -1], [-3, 2, 10]]
b = [11, 4, 6]
n = len(A)
e = 0.01
x = [0, 0, 0] # начальные приближения

solution, counter = iterate(x)
print("Решение: ", solution)
print("Количество итераций: ", counter)