goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа:', lamps_quantity, 'шт. - стоимость', lamps_cost, 'руб.')

print('Общее количество ламп:', lamps_quantity, 'шт. - их общая стоимость: ', lamps_cost, 'руб.')
print()

table_cost = store[goods['Стол' ]][0]['quantity']  * store[goods['Стол' ]][0]['price']
print('Стол:', store[goods['Стол' ]][0]['quantity'], 'шт. - стоимость', store[goods['Стол' ]][0]['price'], 'руб.')
print('Стол:', store[goods['Стол' ]][1]['quantity'], 'шт. - стоимость', store[goods['Стол' ]][1]['price'], 'руб.')
temp_A  = store[goods['Стол' ]][0]['quantity']
temp_A += store[goods['Стол' ]][1]['quantity']
temp_B  = store[goods['Стол' ]][0]['price'] * store[goods['Стол' ]][0]['quantity']
temp_B += store[goods['Стол' ]][1]['price'] * store[goods['Стол' ]][1]['quantity']
print('Общее количество столов:', temp_A, 'шт. - их общая стоимость', temp_B, 'руб.')
print()

sofa_cost  = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
print('Диван:', store[goods['Диван' ]][0]['quantity'], 'шт. - стоимость', store[goods['Диван' ]][0]['price'], 'руб.')
print('Диван:', store[goods['Диван' ]][1]['quantity'], 'шт. - стоимость', store[goods['Диван' ]][1]['price'], 'руб.')
temp_A  = store[goods['Диван' ]][0]['quantity']
temp_A += store[goods['Диван' ]][1]['quantity']
temp_B  = store[goods['Диван' ]][0]['price'] * store[goods['Диван' ]][0]['quantity']
temp_B += store[goods['Диван' ]][1]['price'] * store[goods['Диван' ]][1]['quantity']
print('Общее количество диванов: ', temp_A, 'шт. - их общая стоимость', temp_B, 'руб')
print()

chair_cost = store[goods['Стул' ]][0]['quantity']  * store[goods['Стул' ]][0]['price']
print('Стул:', store[goods['Стул' ]][0]['quantity'], 'шт. - стоимость', store[goods['Стул' ]][0]['price'], 'руб')
print('Стул:', store[goods['Стул' ]][1]['quantity'], 'шт. - стоимость', store[goods['Стул' ]][1]['price'], 'руб')
print('Стул:', store[goods['Стул' ]][2]['quantity'], 'шт. - стоимость', store[goods['Стул' ]][2]['price'], 'руб')
temp_A  = store[goods['Стул' ]][0]['quantity']
temp_A += store[goods['Стул' ]][1]['quantity']
temp_A += store[goods['Стул' ]][2]['quantity']
temp_B  = store[goods['Стул' ]][0]['price'] * store[goods['Стул' ]][0]['quantity']
temp_B += store[goods['Стул' ]][1]['price'] * store[goods['Стул' ]][1]['quantity']
temp_B += store[goods['Стул' ]][2]['price'] * store[goods['Стул' ]][2]['quantity']
print('Общее количество стульев:', temp_A, 'шт. - их общая стоимость', temp_B, 'руб.')
print()