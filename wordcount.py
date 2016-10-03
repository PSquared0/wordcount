my_text= open("twain.txt")
count_dictionary = {}
import string
exclude = set(string.punctuation)

for line in my_text:
    stripped_line = line.rstrip()
    splitline = stripped_line.split(' ')
    for item in splitline:
        loweritem =  item.lower()
        loweritem = ''.join(ch for ch in loweritem if ch not in exclude)
        count_dictionary[loweritem] = count_dictionary.get(loweritem, 0) + 1

for key, value in count_dictionary.items():
    print key, value