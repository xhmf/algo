
def selectionSort(ls):
    for i in range(len(ls)):
        cur_min = ls[i]
        swap = i
        for j in range(i + 1, len(ls)):
            if ls[j] < cur_min:
                swap = j
                cur_min = ls[j]
        ls[swap] = ls[i]
        ls[i] = cur_min

def insertionSort(ls):
    for i in range(1, len(ls)):
        current = ls[i]
        insert = i
        while insert > 0 and ls[insert - 1] > current:
            ls[insert] = ls[insert - 1]
            insert -= 1
        ls[insert] = current

def mergeSort(ls):
    if len(ls) == 1:
        return ls
    middle = len(ls) // 2
    return merge(mergeSort(ls[:middle]), mergeSort(ls[middle:]))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:] if left_index < len(left) else right[right_index:]
    return result

def quickSort(ls):
    recQuick(ls, 0, len(ls) - 1)

def recQuick(ls, low, high):
    if high > low:
        pivot = partition(ls, low, high)
        recQuick(ls, low, pivot - 1)
        recQuick(ls, pivot + 1, high)


def partition(ls, low, high):
    pivot = ls[high]
    low_index = low
    for i in range(low, high):
        if ls[i] < pivot:
            ls[low_index], ls[i] = ls[i], ls[low_index]
            low_index += 1
    ls[low_index], ls[high] = ls[high], ls[low_index]
    return low_index



def verify(ls):
    for i in range(1, len(ls)):
        if ls[i] < ls[i - 1]:
            return False
    return True
