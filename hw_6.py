
list_test = [223, 43, 1, 4, 6, 76, 23]

def bubble_sort(list1):
     for i in range(len(list1)):
         for j in range(len(list1) - i - 1):
             if list1[j] > list1[j+1]:
                 list1[j], list1[j+1] = list1[j+1], list1[j]
                 j += 1
     return list1
print(bubble_sort(list_test))

def binary_search(value, list1):
    n = len(list1)
    result_ok = False
    first = 0
    last = n - 1
    pos = None
    while True:
        if first < last:
            mid = (first + last) // 2
            if value == list1[mid]:
                first = mid
                last = first
                result_ok = True
                pos = mid
            else:
                if value > list1[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
        else:
            if result_ok:
                print("Элемент найден")
                print(pos)
            else:
                print("Элемент не найден")
            break

print(binary_search(4, list_test))