# Задание 4
m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

n = len(m) - 1

for i in range(n):
    for j in range(n):
        a = m[i][j]
        m[i][j] = m[n - j][n - i]
        m[n - j][n - i] = a


print(m)


# Задание 6