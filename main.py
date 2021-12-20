import os
from pprint import pprint
path = os.path.join(os.getcwd(), 'menu.txt')
with open(path, encoding='utf8') as file:
    cook_book = {}
    menu = []
    for dish in file:
        data=[]
        menu.append(dish.strip())
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

    def get_shop_list_by_dishes(dishes, person_count):
        ingradient_list = {}
        for dish in dishes:
            for item in (cook_book[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*int(person_count)})])
                # pprint(items_list)
                if ingradient_list.get(item['ingredient_name']):
                    extra_item = (int(ingradient_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    ingradient_list[item['ingredient_name']]['quantity'] = extra_item
                    # pprint(items_list)
                else:
                    ingradient_list.update(items_list)
        pprint(ingradient_list)
    get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель'], 2)


