def totalcount():
print('Total Words:', len(per_word))

def wordsbynum():
print('Word Frequency:', counts)

file = open("debuggingwiki.txt", "r")
read_data = file.read()
per_word = read_data.split()

file = open("debuggingwiki.txt")
counts = dict()
for line in file:
words = line.split()
for word in words:
if word in counts:
counts[word] += 1
else:
counts[word] = 1

totalcount()
wordsbynum()
