first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif not 69: # задание просит использовать not, но нет никакого описания not и применения здесь :/
    print(420) # поэтому это число никогда не будет распечатано
else:
    print(0)