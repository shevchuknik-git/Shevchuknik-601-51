def make_line_reader(filename):
    file = open(filename, 'r', encoding='utf-8')
    
    def get_next_line():
        line = file.readline()
        if not line:
            file.close()
            return None
        return line.strip()
        
    return get_next_line

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("Строка 1\nСтрока 2\nСтрока 3")

reader = make_line_reader('test.txt')

print(reader())
print(reader())
print(reader())
print(reader())