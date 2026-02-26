garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

garden_set = set(garden)
meadow_set = set(meadow)

or_flowers = garden_set | meadow_set
print(f"\nВсе виды уникальных цветов: {or_flowers}")

and_flowers = garden_set & meadow_set
print(f"\nЦветы, растущие сразу в двух местах: {and_flowers}")

garden_flowers = or_flowers - meadow_set
print(f"\nЦветы, ратсущие только в саду: {garden_flowers}")

meadow_flowers = or_flowers - garden_flowers - and_flowers
print(f"\nЦветы, ратсущие только на лугу: {garden_flowers}")