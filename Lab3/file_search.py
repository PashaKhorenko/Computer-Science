# поиск по файлу

a = str(input("Введите имя и фамилию студента: "))
file1 = open("students5.txt","r")
text1 = file1.read()
if a in text1:
    print ("Студент есть в 5 группе.")
else:
    print("Такой студент не найден в 5 группе.")


file2 = open("students6.txt","r")
text2 = file2.read()
if a in text2:
    print ("Студент есть в 6 группе.")
else:
    print("Такой студент не найден в 6 группе.")


file3 = open("students7.txt","r")
text3 = file3.read()
if a in text3:
    print ("Студент есть в 7 группе.")
else:
    print("Такой студент не найден в 7 группе.")
