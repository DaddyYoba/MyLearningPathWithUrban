def get_matrix(n, m, value):
    matrix = []
    i = 0
    while i < n and m > 0: # вывод абсолютно пустого списка, если n или m <= 0
        matrix.append([])
        j = 0
        while j < m:
            matrix[i].append(value)
            j += 1
        i += 1
    return matrix

height = int(input('Введите количество строк матрицы: ')) # заполнение значений матрицы пользователем
width = int(input('Введите количество столбцов матрицы: '))
value = int(input('Введите значение для заполнения матрицы: '))

result = get_matrix(height, width, value)

for row in result: # решил сделать построчный вывод (спасибо гуглу, я не знаю про *row и вообще про звёзды)
    print(*row, sep=', ')

print(result, '\n') # обычный вывод с отделением от примера

result1 = get_matrix(2, 2, 10) # строки из примера
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)