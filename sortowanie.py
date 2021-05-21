from time import perf_counter_ns

def qs(arr, p, r):
    if p < r:
        q = part(arr, p, r)
        qs(arr, p, q-1)
        qs(arr, q+1, r)

def part(arr, p, r):
    pivot = arr[r]
    smaller = p
    for j in range(p, r):
        if arr[j] <= pivot:
            arr[smaller], arr[j] = arr[j], arr[smaller]
            smaller = smaller + 1
    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller




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
    pierwszawsza = n // 2 - 1;
    for i in range(pierwszawsza, -1, -1):
        Heapify(arr, n, i);
def Heap_Sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)




minrun = 32
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
    pierwsza = arr[start:mid + 1]
    ostatnia = arr[mid + 1:end + 1]
    dlugosc1 = mid - start + 1
    dlugosc2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < dlugosc1 and ind2 < dlugosc2:
        if pierwsza[ind1] < ostatnia[ind2]:
            arr[ind] = pierwsza[ind1]
            ind1 += 1
        else:
            arr[ind] = ostatnia[ind2]
            ind2 += 1
        ind += 1

    while ind1 < dlugosc1:
        arr[ind] = pierwsza[ind1]
        ind1 += 1
        ind += 1

    while ind2 < dlugosc2:
        arr[ind] = ostatnia[ind2]
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



arr = [7,4,3,8,10,3,3,13,14,21,27]
t_start = perf_counter_ns()
TimSort(arr)
t_stop = perf_counter_ns()
print("czas sortowania, zbior losowy, Tim:",
                                         t_stop-t_start)


t_start = perf_counter_ns()
TimSort(arr)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany, Tim:",
                                         t_stop-t_start)



arr=[27,21,14,13,10,8,7,4,3,3,3]
t_start = perf_counter_ns()
TimSort(arr)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany odwrotnie, Tim:",
                                         t_stop-t_start)


arr = [7,4,3,8,10,3,3,13,14,21,27]
t_start = perf_counter_ns()
qs(arr,0,len(arr) - 1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior losowy, Qs:",
                                         t_stop-t_start)

t_start = perf_counter_ns()
qs(arr,0,len(arr) - 1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany, Qs:",
                                         t_stop-t_start)

arr=[27,21,14,13,10,8,7,4,3,3,3]
t_start = perf_counter_ns()
qs(arr,0,len(arr) - 1)
t_stop = perf_counter_ns()
print("czas sortowania, zbior posortowany odwrotnie, Qs:",
                                         t_stop-t_start)

arr = [7,4,3,8,10,3,3,13,14,21,27]
t_start = perf_counter_ns()
Heap_Sort(arr)
Build_Heap(arr, 3);
t_stop = perf_counter_ns()
print("czas sortowania, zbior losowy, Heapsort:",
                                         t_stop-t_start)

t_start = perf_counter_ns()
Heap_Sort(arr)
Build_Heap(arr, 3);
t_stop = perf_counter_ns()
print("czas sortowania, zbior posegregowany, Heapsort:",
                                         t_stop-t_start)

arr=[27,21,14,13,10,8,7,4,3,3,3]
t_start = perf_counter_ns()
Heap_Sort(arr)
Build_Heap(arr, 3);
t_stop = perf_counter_ns()
print("czas sortowania, zbior posegregowany odwrotnie, Heapsort:",
                                         t_stop-t_start)









