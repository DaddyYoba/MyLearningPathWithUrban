my_dict = {"Bilbo": 2890, "Frodo": 2968, "Sam": 2980}
print(f'Dict: {my_dict}')

print(f'Existing value: {my_dict["Sam"]}')
print(f'Not existing value: {my_dict.get("Gandalf")}')

my_dict.update({'Pippin': 2990,
                'Merry': 2892})

deletedValue = my_dict.pop('Bilbo')
print(f'Modified dictionary: {deletedValue}')

print(f'Dict: {my_dict}\n')


my_set = {1, 2, 'One Ring', 'One Ring', 2.25, 2.25}
print(f'Set: {my_set}')

my_set.update([False,
               ('Sword',
                'Bow',
                'Axe')])

print(f'Modified set: {my_set}')