my_famaly = ["я", "мама", "папа", "бабушка", "дешушка"]

my_family_height = [
["я",        168],
["мама",     148],
["папа",     175],
["бабушка",  166],
["дешушка",  176]
]

for object in my_family_height:
    if object[0] == "папа":
        print(f"Рост отца - {object[1]} см")
        break

total_height = 0

for object in my_family_height:
    total_height += object[1]

print(f"Общий рост моей семьи - {total_height} см")