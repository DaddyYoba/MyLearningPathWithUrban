def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
# Результат второго вывода равен нулю, а задание заявляет, что 24. Честно говоря, я не могу этого понять.
# Примечание 1 указывает именно на первые нули числа, а если число состоит из нуля?
# Не должно же оно исчезать или равняться единице, таких требований нет.
# Стек вызовов же выглядит так:
# get_multiplied_digits(402030) ->
# 4 * get_multiplied_digits(2030) ->
# 4 * 2 * get_multiplied_digits(30) ->
# 4 * 2 * 3 * get_multiplied_digits(0) ->
# 4 * 2 * 3 * 0