import math

from T0D0 import get_distances
from T1D1 import check_points_in_circle
from T2D2 import find_solutions
from T3D3 import print_favorite_movies
from T4D4 import process_family_heights
from T5D5 import process_zoo, find_Animal
from T6D6 import calculate_songs_duration
from T7D7 import decode_secret_message
from T8D8 import process_flowers
from T9D9 import print_sweets_prices
from T10D10_2 import calculate_store_inventory

def test_t0d0_distances():
    """Тест задачи 0: Расстояния (проверяем возвращаемый словарь)"""
    distances = get_distances()
    assert isinstance(distances, dict)
    assert ('Moscow', 'London') in distances
    expected_dist = math.sqrt((550 - 510)**2 + (370 - 510)**2)
    assert distances[('Moscow', 'London')] == expected_dist

def test_t1d1_circle(capsys):
    """Тест задачи 1: Круг (перехватываем print)"""
    check_points_in_circle()
    captured = capsys.readouterr()
    assert "Площадь круга: 5541.7693" in captured.out
    assert "Точка 1 (23, 34): True" in captured.out
    assert "Точка 2 (30, 30): False" in captured.out

def test_t2d2_solutions():
    """Тест задачи 2: Комбинаторика (проверяем возвращаемый список)"""
    solutions = find_solutions()
    assert isinstance(solutions, list)
    for exp, res in solutions:
        assert res == 25

def test_t3d3_movies(capsys):
    """Тест задачи 3: Срезы строк"""
    print_favorite_movies()
    captured = capsys.readouterr()
    assert "Терминатор" in captured.out
    assert "Назад в будущее" in captured.out

def test_t4d4_family(capsys):
    """Тест задачи 4: Рост семьи"""
    process_family_heights()
    captured = capsys.readouterr()
    assert "Рост отца - 175 см" in captured.out
    assert "Общий рост моей семьи - 833 см" in captured.out

def test_t5d5_zoo(capsys):
    """Тест задачи 5: Зоопарк"""
    lst = ['lion', 'bear', 'kangaroo']
    assert find_Animal(lst, 'lion') == 1
    assert find_Animal(lst, 'kangaroo') == 3
    assert find_Animal(lst, 'tiger') is None

    process_zoo()
    captured = capsys.readouterr()
    assert "bear" in captured.out
    assert "rooster" in captured.out

def test_t6d6_songs(capsys):
    """Тест задачи 6: Длительность песен"""
    calculate_songs_duration()
    captured = capsys.readouterr()
    assert "Три песни звучат 14.93 минут" in captured.out
    assert "А другие три песни звучат 13.49 минут" in captured.out

def test_t7d7_secret(capsys):
    """Тест задачи 7: Секретное сообщение"""
    decode_secret_message()
    captured = capsys.readouterr()
    assert len(captured.out.strip()) > 0

def test_t8d8_flowers(capsys):
    """Тест задачи 8: Множества (сад и луг)"""
    process_flowers()
    captured = capsys.readouterr()
    assert "Все виды уникальных цветов:" in captured.out
    assert "Цветы, растущие сразу в двух местах:" in captured.out

def test_t9d9_sweets(capsys):
    """Тест задачи 9: Словари (сладости)"""
    print_sweets_prices()
    captured = capsys.readouterr()
    assert "печенье:" in captured.out
    assert "ашан - 10.99" in captured.out

def test_t10d10_store(capsys):
    """Тест задачи 10: Магазин мебели"""
    calculate_store_inventory()
    captured = capsys.readouterr()
    assert "Общее количество ламп: 27 шт. - их общая стоимость: 1134 руб." in captured.out
    assert "Общее количество столов: 54 шт. - их общая стоимость: 27860 руб." in captured.out