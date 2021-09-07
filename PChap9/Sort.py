import random
lyst = list(range(1,20))
random.shuffle(lyst)


def bubbleSortList(lyst):
    print("before: ", lyst)
    listLength = (len(lyst))
    for i in range(listLength):
        for j in range(i + 1,listLength):
            if lyst[i] > lyst[j]:
                temp  = lyst[i]
                lyst[i] = lyst[j]
                lyst[j] = temp

    print("After:  ",lyst)
    return lyst           



bubbleSortList(lyst)





