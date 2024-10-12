#8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
flag = 0
for line in fh:
    line.rstrip()
    t = line.split()
    if len(lst) == 0:
        lst.append(t[0])

    for word in range(len(t)):
        for item in range(len(lst)):
            if t[word] == lst[item]:
                flag = 1
        if flag == 0:
            lst.append(t[word])
        else:
            flag = 0

lst.sort()
print(lst)
