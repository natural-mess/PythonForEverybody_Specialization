name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dic = dict()

for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        word = words[5]
        # print (word)
        num = word.split(":")
        dic[num[0]] = dic.get(num[0],0) + 1
        
l = list(dic.items())
l.sort()
for key, val in l:
    print(key, val)
