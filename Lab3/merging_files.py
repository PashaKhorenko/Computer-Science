# объеденение файлов

filenames = ['students5.txt', 'students6.txt', 'students7.txt']

with open('students567.txt', 'w') as outfile:

    for names in filenames:
        with open(names) as infile:

            outfile.write(infile.read())
