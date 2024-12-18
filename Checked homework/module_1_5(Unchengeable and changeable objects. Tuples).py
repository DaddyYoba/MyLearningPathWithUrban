immutable_var = 1, True, 'String', 3.15
print(immutable_var)
#immutable_var[0] = 2 #невозможно всвязи с природой кортежа - изменить возможно только список, вложенный в элемент кортежа
mutable_var = [2, False, "Needle", 9.99]
mutable_var[3] = 420.69
mutable_var += ["Ну, допустим, добавлено"]
print(mutable_var)