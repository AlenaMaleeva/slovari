my_dict= {'Сава': 2009, 'Федя': 2016, 'Алена': 1987}
print( my_dict)
print( my_dict['Алена'])
my_dict ['Миша'] = 1978
print( my_dict)
print( my_dict.get ('Вика'))
my_dict.update({ 'дедешка': 1961, 'бабушка': 1962})
print( my_dict)
a = my_dict. pop ('бабушка')
print( my_dict)
print(a)
print( my_dict)

my_set = {1, 2, 3, 3, 2, 1, 'солнце', 'луна', 'солнце'}
print(my_set)
my_set. update({9, 11})
print( my_set)
my_set. discard(2)
print(my_set)