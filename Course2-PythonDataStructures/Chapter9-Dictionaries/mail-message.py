name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dic = dict()

for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        word = words[1]
        dic[word] = dic.get(word,0) + 1

bigCount = None
bigWord = None
for word,count in dic.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print (bigWord, bigCount)
