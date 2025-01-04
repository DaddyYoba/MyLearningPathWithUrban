def calculate_structure_sum(data, *, result=None):
    if result is None:
        result = []

    match data: # превратить if-elif-else в match-case помог chatgpt (ну и выглядит аккуратней)
        case int() | float():
            result.append(data)
        case str():
            result.append(len(data))
        case bool(): # Для добавления единицы при True и нуля при False
            result.append(int(data)) # в целом можно добавить функционал подсчёта количества конечных значений
        case list() | tuple() | set():
            for i in data:
                calculate_structure_sum(i, result=result)
        case dict():
            for key, value in data.items():
                calculate_structure_sum(key, result=result)
                calculate_structure_sum(value, result=result)
        case _:
            raise TypeError(f"Неподдерживаемый тип данных: {type(data)}")

    # if isinstance(data, int):
    #     result.append(data)
    # elif isinstance(data, str):
    #     result.append(len(data))
    # elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
    #     for i in data:
    #         calculate_structure_sum(i, result=result)
    # elif isinstance(data, dict):
    #     for i, t in data.items():
    #         calculate_structure_sum(i, result=result)
    #         calculate_structure_sum(t, result=result)
    # return sum(result)

    return sum(result)


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)