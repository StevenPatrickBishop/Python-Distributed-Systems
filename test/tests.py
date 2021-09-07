from functools import reduce


filepath = input("Enter a filename: ") #"numbers.txt"

f = open(filepath,"r")
stringList = []

for each in f.read().split():
    stringList.append(each)

numList = list(map(int,stringList))
total = reduce(lambda x,y: x + y,numList)
count = len(numList)

print(total/count)


f.close() 