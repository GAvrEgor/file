import os
from pprint import pprint
path = os.path.join(os.getcwd(), 'menu.txt')
with open(path, encoding='utf8') as file:
    cook_book = {}

    for dish in file:
        data=[]
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_dish = []
        for item in range(counter):
            a = ingredient_name, quantity, measure = file.readline().split('|')
            data.append(a)
            temp_dish.append({'ingredient_name': ingredient_name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()})
            cook_book[dish_name] = temp_dish
        file.readline()
    # pprint(cook_book)
    def get_shop_list_by_dishes(dish_name, person_count):
        #print(cook_book[dish_name])# меню к блюду
        a = cook_book[dish_name]
        for i in a:
            d = {}
            l = list(i.values())
            d[l[0]] = {'quantity': int(l[1].strip()) * (person_count), 'measure': l[2].strip()}
            print(d)
    pprint(get_shop_list_by_dishes('Фахитос', 1))





