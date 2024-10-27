import re #import regular expression

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_2102403.txt"
handle = open(name)

total = 0

for line in handle:
    line = line.rstrip()
    lst = re.findall('[0-9]+', line)
    if (lst):
        for num in lst:
            intNum = int(num)
            total = total + intNum

 
print(total)