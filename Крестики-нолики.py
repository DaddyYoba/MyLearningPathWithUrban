# Если вы это читаете, то я прошу Вас оценить адекватность данной версии крестиков-ноликов и дать советы для улучшения)
import random

def draw_area(): # отрисовка поля игры
    for i in area:
        print(*i)

def check_win_condition(): # проверка завершения игры
    global condition
    if counter > 8:
        return True
    if area[0][0] != '*' and ((area[0][0] == area[0][1] and area[0][1] == area[0][2]) or
                              (area[0][0] == area[1][0] and area[1][0] == area[2][0]) or
                              (area[0][0] == area[1][1] and area[1][1] == area[2][2])):
        if area[0][0] == 'X':
            condition = 'X'
        else:
            condition = '0'
        return True
    elif area[2][2] != '*' and ((area[2][2] == area[2][1] and area[2][1] == area[2][0]) or
                                (area[2][2] == area[1][2] and area[1][2] == area[0][2])):
        if area[2][2] == 'X':
            condition = 'X'
        else:
            condition = '0'
        return True
    elif area[1][1] != '*' and ((area[1][1] == area[2][1] and area[2][1] == area[0][1]) or
                                (area[1][1] == area[1][2] and area[1][2] == area[1][0]) or
                                (area[1][1] == area[2][0] and area[2][0] == area[0][2])):
        if area[1][1] == 'X':
            condition = 'X'
        else:
            condition = '0'
        return True
    return False

def make_move(): # присвоение клетке значения
    global area, counter
    if counter % 2 == 0:
        area[row][column] = 'X'
    else:
        area[row][column] = '0'
    counter += 1

def robot_move(): # выполнение хода компьютером
    global row, column
    while True:
        row = random.randint(0,2) # случайный выбор клетки для хода
        column = random.randint(0, 2)
        if area[row][column] == '*':
            make_move()
            print(f'Компьютер на ходу №{counter} походил на клетку {row * 3 + column + 1}')
            break

counter = 0 # счётчик ходов
condition = '*' # условие завершения игры
playing_as = 2 # выбор при игре против ПК, за кого играть (1 - X, 0 - 0)
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

print('Приветствую! Давайте сыграем в игру крестики-нолики!\n----------------------------------------------------')

game_mode = int(input('Выберите режим игры! "1" - против человека, "2" - против компьютера: '))
if game_mode == 2:
    playing_as = int(input('Выберите, чем будете ходить! Напоминаю, что всегда начинают крестики.\n'
                       '"1" - за крестики, "0" - за нолики: '))

while not check_win_condition():
    if game_mode == 1 or (counter + playing_as + 1) % 2 == 0:
        draw_area()
        move = int(input(f'Ход №{counter + 1}. Введите номер незанятой клетки от 1 до 9: ')) - 1
        print('')
        row = move // 3
        column = move % 3
        if area[row][column] != '*':
            print('!!!Клетка занята, попробуйте ещё раз...!!!')
            continue
        make_move()
    else:
        robot_move()

draw_area()
if condition == '*':
    print("Это ничья!")
elif condition == 'X':
    print("Победили крестики!")
elif condition == '0':
    print("Победили нолики!")
else:
    print('В рот мне ноги, Девид Блейн! Раскукожь этот код обратно!!!')
print(f'Игра завершилась за {counter} ходов.')
