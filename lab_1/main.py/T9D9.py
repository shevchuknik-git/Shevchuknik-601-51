def print_sweets_prices():
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ]
    }

    sweets = {
        'печенье': [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99},
        ],
        'конфеты': [
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99},
        ],
        'карамель': [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'магнит', 'price': 41.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ]
    }

    for sweet_name, shops_list in sweets.items():
        print(f"{sweet_name}:")
        for item in shops_list:
            print(f"  {item['shop']} - {item['price']} ₽")
        print()

if __name__ == '__main__':
    print_sweets_prices()