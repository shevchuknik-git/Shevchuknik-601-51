k = int(input())

field = ""
for i in range(4):
	field += input()

score = 0
for digit in "123456789":
	count = field.count(digit)
	if count > 0 and count <= 2 * k:
		score += 1

print(score)
