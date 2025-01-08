def calculate_structure_sum(data):
    sum = 0

    match data: # превратить if-elif-else в match-case помог chatgpt (ну и выглядит аккуратней)
        case int() | float() | bool():
            sum += data
        case str():
            sum += len(data)
        case list() | tuple() | set():
            for i in data:
                sum += calculate_structure_sum(i)
        case dict():
            for key, value in data.items():
                sum += calculate_structure_sum(key)
                sum += calculate_structure_sum(value)
        case _:
            raise TypeError(f"Неподдерживаемый тип данных: {type(data)}")

    # if isinstance(data, int) or isinstance(data, float) or isinstance(data, bool):
    #     sum += (data)
    # elif isinstance(data, str):
    #     sum += (len(data))
    # elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
    #     sum += calculate_structure_sum(*args)
    # elif isinstance(data, dict):
    #     for key, value in data.items():
    #         sum += calculate_structure_sum(key)
    #         sum += calculate_structure_sum(value)
    # else:
    #     raise TypeError(f"Неподдерживаемый тип данных: {type(data)}")
    # return sum

    return sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)