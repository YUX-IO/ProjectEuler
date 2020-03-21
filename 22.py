"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

f = open("p022_names.txt", mode='r')
names = f.read()
f.close()
names = [x[1:-1] for x in names.split(",")]
names.sort()
for n in range(len(names)):
    names[n] = sum(ord(letter) - 64 for letter in list(names[n])) * (n + 1)
print(sum(names))
