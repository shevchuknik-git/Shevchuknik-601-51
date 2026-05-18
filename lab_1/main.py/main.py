from T0D0 import get_distances
from T1D1 import check_points_in_circle
from T2D2 import find_solutions
from T3D3 import print_favorite_movies
from T4D4 import process_family_heights
from T5D5 import process_zoo
from T6D6 import calculate_songs_duration
from T7D7 import decode_secret_message
from T8D8 import process_flowers
from T9D9 import print_sweets_prices
from T10D10_2 import calculate_store_inventory

def main():
    print("="*50)
    print("ЗАПУСК ЗАДАЧИ 0: Расстояния между городами")
    print("="*50)
    distances = get_distances()
    for cities, dist in distances.items():
        print(f"Расстояние между {cities[0]} и {cities[1]}: {dist:.2f}")
        
    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 1: Площадь круга и точки")
    print("="*50)
    check_points_in_circle()
    
    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 2: Комбинаторика операций")
    print("="*50)
    solutions = find_solutions()
    if solutions:
        print(f"Найдено {len(solutions)} решений для получения числа 25:")
        for exp, res in solutions:
            print(f"{exp} = {res}")
    else:
        print("Решений не найдено.")

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 3: Любимые фильмы (срезы)")
    print("="*50)
    print_favorite_movies()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 4: Рост семьи")
    print("="*50)
    process_family_heights()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 5: Зоопарк")
    print("="*50)
    process_zoo()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 6: Длительность песен")
    print("="*50)
    calculate_songs_duration()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 7: Секретное сообщение")
    print("="*50)
    decode_secret_message()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 8: Сад и луг (множества)")
    print("="*50)
    process_flowers()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 9: Цены на сладости (словари)")
    print("="*50)
    print_sweets_prices()

    print("\n" + "="*50)
    print("ЗАПУСК ЗАДАЧИ 10: Магазин мебели (словари и списки)")
    print("="*50)
    calculate_store_inventory()
    
    print("\n" + "="*50)
    print("ВСЕ ЗАДАЧИ УСПЕШНО ВЫПОЛНЕНЫ!")
    print("="*50)

if __name__ == '__main__':
    main()