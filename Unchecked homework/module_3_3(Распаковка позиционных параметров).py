def print_params(a = 1, b = 'строка', c = True):
    global count
    count += 1
    print(f'Использование №{count}:\n'
          f'a = {a}, тип: {type(a)}\n'
          f'b = {b}, тип: {type(b)}\n'
          f'c = {c}, тип: {type(c)}')

count = 0
values_list = ['НеСтрокаЧестноАвтичаю', ['Down', 'with', 'the,' 'sickness'], 69.420]
values_dict = {'a': 27, 'b': ([([(["FFDP"])])],[([(["AILD"])], [(["Ice Nine Kills"])])]), 'c': False}
values_list_2 = [54.32, 'Строка' ]

print_params(*values_list)
print_params(**values_dict)
print_params(42, *values_list_2, )
