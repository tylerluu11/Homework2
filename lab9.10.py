import csv
file = input()
with open(file, 'r') as wordsfile:
    words_reader = csv.reader(wordsfile)
    for row in words_reader:
        list1 = row

list2 = list(dict.fromkeys(list1))
lenlist = len(list2)

for i in range(lenlist):
    print(list2[i], list1.count(list2[i]))