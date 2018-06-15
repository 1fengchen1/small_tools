from datetime import datetime


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 7


def now_time():
    now = datetime.now().microsecond
    print(now)
    now = int(now)
    return now

def ord_search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            print('list[{0}]={1}'.format(i, element))
            return i
    else:
        print('not found')

def bin_search(list, element):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        if element == list[mid]:
            print('list[{0}]={1}'.format(mid, element))
            return mid
        elif element > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


start = now_time()
i = bin_search(list, element)
end = now_time()
print(end-start)
start = now_time()
j = ord_search(list, element)
end = now_time()
print(end-start)