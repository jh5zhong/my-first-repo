import random
def get_random_from_list_multi(lst, num):
    randomList = lst[:]
    random.shuffle(randomList)
    if len(lst) < int(num):
        return randomList
    else:
        return randomList[0:int(num)]
    

a = get_random_from_list_multi([1,2,3,4,5,6], 1)
print(a)