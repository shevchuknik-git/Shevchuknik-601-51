def calculate_store_inventory():
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

    plurals = {
        'Лампа': 'ламп',
        'Стол': 'столов',
        'Диван': 'диванов',
        'Стул': 'стульев'
    }

    for item_name, item_code in goods.items():
        total_quantity = 0
        total_cost = 0
        
        batches = store[item_code]
        
        for batch in batches:
            quantity = batch['quantity']
            price = batch['price']
            
            print(f"{item_name}: {quantity} шт. - стоимость {price} руб.")
            
            total_quantity += quantity
            total_cost += quantity * price
            
        plural_name = plurals.get(item_name, item_name)
        
        print(f"Общее количество {plural_name}: {total_quantity} шт. - их общая стоимость: {total_cost} руб.\n")

if __name__ == '__main__':
    calculate_store_inventory()