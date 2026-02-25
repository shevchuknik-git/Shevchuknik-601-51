zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

print(f"Список животных в зоопарке: \n{zoo}")

result = zoo
for i in range(len(zoo) -1):
    if zoo[i] == 'lion' and zoo[i + 1] == 'kangaroo':
        result.insert(i + 1, 'bear')
print(f"\nПосадите медведя (bear) между львом и кенгуру: \n{result}")

birds = ['rooster', 'ostrich', 'lark', ]

for i in range(len(birds)):
    result.append(birds[i])
print(f"\nДобавьте птиц из списка 'birds' в последние клетки зоопарка: \n{result}")

value_to_remove = 'elephant'
while value_to_remove in result:
    result.remove(value_to_remove)
print(f"\nУберите слона и выведите список на консоль: \n{result}")

def find_Animal(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i + 1
        
print(f"\nВыведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark)")
print(f"\nНомер клетки в которой сидет (lion): {find_Animal(result, 'lion')}")
print(f"\nНомер клетки в которой сидет (lion): {find_Animal(result, 'lark')}")
