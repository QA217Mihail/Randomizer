import random

# list of names
names = ['Сысуева', 'Стрельцов', 'Никитина', 'Кашапов',
         'Гула', 'Скорокосов']

# shuffle the list
random.shuffle(names)

# assign ticket numbers
ticket_numbers = list(range(1, len(names)+10))
random.shuffle(ticket_numbers)

# print the randomized list with ticket numbers
for i in range(len(names)):
    print(f"{ticket_numbers[i]} билет: {names[i]}")
