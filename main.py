from pprint import pprint

cook_book = {}

with open('recipes.txt', encoding='utf-8') as file:
    lines = file.readlines()
    food = lines[0].strip()
    row_count = int(lines[1])
    line = 0
    for count in range(len(lines)):
        if len(lines[count]) == 1:
            row_count = int(lines[(count + 2)])
            food = lines[count + 1].strip()
            line = count + 1
        ingredients_list = []
        for i in range(row_count):
            ingredients = lines[line + 2 + i].split('|')
            ingredients_list.append({'ingredient_name': ingredients[0].strip(), 'quantity': int(ingredients[1]),
                                     'measure': ingredients[2].strip()})
            cook_book[food] = ingredients_list

pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    book = {}
    count = {}
    for i in range(len(dishes)):
        ingredients = cook_book.get(dishes[i])
        s_list = {}

        for i in ingredients:
            if (i['ingredient_name']) in book:
                if (count.get(i['ingredient_name'])) == None:
                    count[(i['ingredient_name'])] = 2
                else:
                    count[(i['ingredient_name'])] += 1
                multiple = (count.get(i['ingredient_name']))
            else:
                multiple = 1
            s_list = {'measure': (i['measure']), 'quantity': (i['quantity']) * person_count * multiple}
            book[(i['ingredient_name'])] = (s_list)

    return book

pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос', 'Запеченный картофель с мясом', 'Яичница'], 2))
