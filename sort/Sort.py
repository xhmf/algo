
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


def verify(ls):
    for i in range(1, len(ls)):
        if ls[i] < ls[i - 1]:
            return False
    return True
