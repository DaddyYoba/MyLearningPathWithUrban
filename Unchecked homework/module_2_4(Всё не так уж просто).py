"""
В задании про это ничего нет, но решил для себя перемешать список,
тем самым немного усложнив задачу. Понимаю, что можно так же, как и в конце,
воспользоваться функцией .sort() или sorted(), но так неинтересно  :-)
"""
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
random.shuffle(numbers)

primes = []
not_primes = []

for i in range(len(numbers)): # для сортированного списка проще было бы указать range(1, len(numbers))
    is_prime = True # установка/обновление флага

    if numbers[i] == 1: # проверка на единицу (если список не отсортирован, не будет проверяться)
        continue

    for j in range(len(numbers)):
        if numbers[j] == 1: # проверка на единицу (если список не отсортирован, не помешает расчёту)
            continue
        if numbers[j] < numbers[i]: # основная проверка на простоту числа и прекращение перебора
            if numbers[i] % numbers[j] == 0:
                is_prime = False
                break
        """
        else: # убрал, чтобы код работал с несортированным списком
            break
        """

    if is_prime: # выбор списка для добавления числа
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

primes.sort() # сортировка итоговых списков
not_primes = sorted(not_primes)

print(primes, not_primes)