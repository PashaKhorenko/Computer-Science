# сортировка по среднему балу

a_dictionary = {}
a_file = open("students567.txt")
for line in a_file:
    key, value = line.split(",")
    a_dictionary[key] = value

for i in sorted(a_dictionary.items(), key = lambda para: para[1]):
    print(i)
