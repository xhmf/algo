import Sort
from Sort import verify
import random


ls = [random.randint(0,100) for i in xrange(100)]
Sort.selectionSort(ls)
print verify(ls)

ls = [random.randint(0,100) for i in xrange(100)]
Sort.insertionSort(ls)
print verify(ls)

ls = [random.randint(0,100) for i in xrange(100)]
ls = Sort.mergeSort(ls)
print verify(ls)

ls = [random.randint(0,100) for i in xrange(100)]
Sort.quickSort(ls)
print verify(ls)
