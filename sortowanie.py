import sys
sys.setrecursionlimit(100000)
from random import *
from time import perf_counter_ns

def Heapify(arr, n, i):
    najwieksza = i
    lewo = 2 * i + 1
    prawo = 2 * i + 2
    if lewo < n and arr[i] < arr[lewo]:
        najwieksza = lewo
    if prawo < n and arr[najwieksza] < arr[prawo]:
        najwieksza = prawo
    if najwieksza != i:
        arr[i], arr[najwieksza] = arr[najwieksza], arr[i]
        Heapify(arr, n, najwieksza)
def Build_Heap(arr, n):
    lewowsza = n // 2 - 1;
    for i in range(lewowsza, -1, -1):
        Heapify(arr, n, i);
def Heap_Sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)




minrun = 32                 # po ile dzielimy na czesc, najszczęściej wybiera się 32/64
def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    lewo = arr[start:mid + 1]
    prawo = arr[mid + 1:end + 1]
    dlugosc1 = mid - start + 1
    dlugosc2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < dlugosc1 and ind2 < dlugosc2:
        if lewo[ind1] < prawo[ind2]:
            arr[ind] = lewo[ind1]
            ind1 += 1
        else:
            arr[ind] = prawo[ind2]
            ind2 += 1
        ind += 1

    while ind1 < dlugosc1:
        arr[ind] = lewo[ind1]
        ind1 += 1
        ind += 1

    while ind2 < dlugosc2:
        arr[ind] = prawo[ind2]
        ind2 += 1
        ind += 1

    return arr


def TimSort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr




def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1


def QuickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)


arr1=[]
for i in range(50000):
    x=randint(0,1000)       #następuje zwolnienie komory losującej
    arr1.append(x)
arr2=arr1









t_start = perf_counter_ns()
QuickSort(arr1,0,len(arr1) - 1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior losowy, QuickSort:",
                                        t_stop-t_start)
""" don't open, death inside.
t_start = perf_counter_ns()
QuickSort(arr1,0,len(arr1) - 1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany, QuickSort:",
                                         t_stop-t_start)

arr1.reverse()
t_start = perf_counter_ns()
QuickSort(arr1,0,len(arr1) - 1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany odwrotnie, Qs :",
                                         t_stop-t_start, "\n")
"""




arr1=arr2
t_start = perf_counter_ns()
TimSort(arr1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior losowy, TimSort",
                                         t_stop-t_start)
t_start = perf_counter_ns()
TimSort(arr1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany, Tim:",
                                         t_stop-t_start)
arr1.reverse()
t_start = perf_counter_ns()
TimSort(arr1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany odwrotnie, Tim:",
                                         t_stop-t_start,"\n")



arr1=arr2
t_start = perf_counter_ns()
Heap_Sort(arr1)
Build_Heap(arr1, 3)
t_stop = perf_counter_ns()
print("czas sortowania, zbior losowy, Heapsort:",
                                         t_stop-t_start)
t_start = perf_counter_ns()
Heap_Sort(arr1)
Build_Heap(arr1, 3)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posegregowany, Heapsort:",
                                         t_stop-t_start)
t_start = perf_counter_ns()
Heap_Sort(arr1)
Build_Heap(arr1, 3)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posegregowany odwrotnie, Heapsort:",
                                         t_stop-t_start,"\n")






