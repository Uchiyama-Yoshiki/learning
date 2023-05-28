import random

def binary_search(list,search):
    low = 0
    high = len(list) -1
    while low <=high:
        mid = low + (high -low) // 2

        print(mid)
        if (search == list[mid]):
            return mid
        elif (search > list[mid]):
            low = mid +1
        else:
            high = mid -1
    return -1
    

list=[]
for _ in range(1000000):
    list.append(random.randrange(100))

list.sort()

result = binary_search(list,51)
if result != -1:
    print("position is{0},value is {1}".format(str(result),list[result]))