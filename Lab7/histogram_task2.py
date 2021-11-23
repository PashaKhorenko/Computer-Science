import matplotlib.pyplot as plt
import pylab

text = "Зобразити гістограму частоти появи літер у певному тексті та зберегти у файла"
frequency_dict = {}

for letter in text.lower():
    if letter != ' ':

        try:

            frequency = frequency_dict.get(letter)
            frequency_dict[letter] = frequency + 1

        except:
            frequency_dict[letter] = 1

values_view = frequency_dict.values()
value_iterator = iter(values_view)
first_value = next(value_iterator)

xdata = []
ydata = []
letter_values = []

for frequency in frequency_dict:
    try:
        xdata.append(xdata[len(xdata) - 1] + 1)
    except:
        xdata.append(0)

    ydata.append(frequency_dict[frequency])
    letter_values.append(frequency)

my_colors = ['#FF0018', '#FFA52C', '#FFFF41', '#008018', '#0000F9', '#86007D']

plt.rcdefaults()

pylab.bar(xdata, ydata, width=1, color=my_colors)
plt.xlabel('Літера')
plt.ylabel('Частота')
plt.xticks(xdata, letter_values)
plt.title('Частота літер у реченні')
plt.savefig('histogram_task2.png', dpi=200)

pylab.show()
