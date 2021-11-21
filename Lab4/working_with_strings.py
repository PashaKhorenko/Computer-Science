# Task 1
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
from nltk.util import ngrams
import nltk
import random
import os

first_list = ['Java', 'Python', 'C++', 'C', 'C#', 'JS', 'PHP', 'Kotlin']
second_list = ['Hello', 'Bye', 'Tommorow', 'Yesterday',
               'Day', 'Night', 'Midnight', 'Afternoon']
third_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']

list_of_strings_list = [first_list, second_list, third_list]


def random_phrase():
    result_string = ""
    for i in range(0, 3):
        random_index = random.randrange(0, 7)
        result_string = result_string + \
            list_of_strings_list[i][random_index] + " "

    return result_string

print(random_phrase())



# Task2

book = "Алхимик. Пауло Коэльо.txt"
test = "test.txt"
filename = book
os.chdir('Lab4')


def count_total_amout_of_chars_with_spaces():

    file = open(filename, 'r')

    data = file.read()
    total_amount = len(data)

    file.close()

    return total_amount


def count_total_amout_of_chars_without_spaces():

    num_chars = 0

    with open(filename, 'r') as f:
        for line in f:
            for letter in line:
                for i in letter:
                    if(i != ' ' and i != '\n'):
                        num_chars += 1

    return num_chars


def total_amout_of_words_in_file():
    num_words = 0
    words_set = set()  # Amount of different words
    # Amount of unique words that appears only once.
    one_time_words = set()
    words_array = []

    with open(filename, 'r') as f:
        for line in f:

            words = line.split()
            num_words += len(words)

            for word in words:
                words_set.add(word)
                words_array.append(word)

    for i in range(0, len(words_array)):
        if(words_array.count(words_array[i]) == 1):
            one_time_words.add(words_array[i])

    print(f'Total amount of different words {len(words_set)}')
    print(f'Total amount of unique words {len(one_time_words)}')

    return num_words


print(f'With spaces {count_total_amout_of_chars_with_spaces()}')
print(f'Without spaces {count_total_amout_of_chars_without_spaces()}')
print(f'Amout of words {total_amout_of_words_in_file()}')


# Task 3 Variant 9
# Варіант 9. Визначте, 10 найчастіше зустрічаємих послідовностей з N слів у тексті. N вказується користувачем.

test_for_task3_filename = "text_for_task3.txt"

nltk.download('punkt')


def task3(amount_of_words):
    f = open(test_for_task3_filename, 'r', encoding="utf-8")
    raw = f.read()

    tokens = nltk.word_tokenize(raw)

    # Create your bigrams
    bgs = nltk.ngrams(tokens, amount_of_words)

    # Compute frequency distribution for all the bigrams in the text
    fdist = nltk.FreqDist(bgs)
    dict = {}
    for k, v in fdist.items():
        dict[k] = v

    sorted_dict_by_int_key = sorted(
        dict.items(), key=lambda x: x[1], reverse=True)  # Sort list by value. Value is a frequency distribution

    total_output_amount = 0
    for k, v in sorted_dict_by_int_key:

        if(total_output_amount == 10):
            return

        print(k, v)
        total_output_amount += 1


task3(3)
