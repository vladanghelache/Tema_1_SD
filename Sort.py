from time import perf_counter

#bubblesort:
def bubblesort(sir):
    n = len(sir)
    for i in range(n):
        for j in range(n - i - 1):
            if sir[j] > sir[j + 1]:
                sir[j], sir[j + 1] = sir[j + 1], sir[j]

#countsort:
def countsort(sir,MAX):
    if MAX>100000000:
        return
    v = [0] * (MAX + 1)
    for x in sir:
        v[x] += 1
    index = 0
    for i in range(MAX + 1):
        while v[i] != 0:
            sir[index] = i
            v[i] -= 1
            index += 1
    end = perf_counter()

#mergesort:
def interclasare(sir, lst, ldr):
    k = 0
    i = 0
    j = 0
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            sir[k] = lst[i]
            i += 1
        else:
            sir[k] = ldr[j]
            j += 1
        k += 1
    while i < len(lst):
        sir[k] = lst[i]
        i += 1
        k += 1
    while j < len(ldr):
        sir[k] = ldr[j]
        j += 1
        k += 1


def mergesort(sir):
    if len(sir) > 1:
        m = len(sir) // 2
        lst = sir[:m]
        ldr = sir[m:]
        mergesort(lst)
        mergesort(ldr)
        interclasare(sir, lst, ldr)

#quicksort:
def pivot_mediana(sir):
    if len(sir)<=5:
        return sorted(sir)[len(sir)//2]
    subliste=[sorted(sir[i:i+5])for i in range (0,len(sir),5)]
    mediane=[sl[len(sl)//2]for sl in subliste]
    return pivot_mediana(mediane)


def partition(sir, start, end, pivot):
    i = (start - 1)

    for j in range(start, end):
        if sir[j]==pivot:
            sir[end], sir[j] = sir[j], sir[end]
        if sir[j] < pivot:
            i = i + 1
            sir[i], sir[j] = sir[j], sir[i]
    sir[i+1],sir[end]=sir[end],sir[i+1]
    return (i + 1)


def quicksort(sir, start, end):
    if start < end:
        pivot=pivot_mediana(sir[start:end+1])
        index_pivot = partition(sir, start, end, pivot)

        quicksort(sir, start, index_pivot - 1)
        quicksort(sir, index_pivot + 1, end)

#radixsort:
def sort_cif(sir, ord):
    n = len(sir)
    rez = [0]*n
    v = [0]*10
    for i in range(0, n):
        x = sir[i] // ord
        v[x % 10] += 1

    for i in range(1, 10):
        v[i] += v[i - 1]
    i = n - 1
    while i >= 0:
        x= sir[i] // ord
        rez[v[x % 10] - 1] =sir[i]
        v[x % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(sir)):
        sir[i] = rez[i]


def radixsort(sir,MAX):
    ord=1
    while MAX//ord>0:
        sort_cif(sir,ord)
        ord *= 10

#funcția care verifica ca algoritmul de sortare a sortat corect:
def test_sort(sir):
    for i in range(1,len(sir)):
        if sir[i]<sir[i-1]:
            return 'Sirul NU a fost sortat corect'
    return 'Sirul a fost sortat corect'

#generator de siruri:
def generator(n,MAX):
    import random
    l=[]
    for i in range(n):
        l+=[random.randint(0,MAX)]
    return l
#generator de sorari:
def sortari(nr_sortare,sir,n,MAX):
    if nr_sortare == 0:
        start = perf_counter()
        bubblesort(sir)
        end = perf_counter()
        return 'bubblesort:','timpul initial:',start,'timpul final:',end,'intervalul temporal:',end-start
    elif nr_sortare==1:
        if Max<100000000:
            start = perf_counter()
            countsort(sir,Max)
            end = perf_counter()
            return 'coutsort:','timpul initial:',start,'timpul final:',end,'intervalul temporal:',end-start
        else:
            return 'countsort: Sirul are numere prea mari pentru countsort'
    elif nr_sortare == 2:
        start = perf_counter()
        mergesort(sir)
        end = perf_counter()
        return 'mergesort:','timpul initial:',start,'timpul final:',end,'intervalul temporal:',end-start
    elif nr_sortare == 3:
        start = perf_counter()
        quicksort(sir,0,len(sir)-1)
        end = perf_counter()
        return 'quicksort:','timpul initial:',start,'timpul final:',end,'intervalul temporal:',end-start
    elif nr_sortare == 4:
        start = perf_counter()
        radixsort(sir,MAX)
        end = perf_counter()
        return  'radixsort:','timpul initial:',start,'timpul final:',end,'intervalul temporal:',end-start
    elif nr_sort == 5:
        start = perf_counter()
        sir.sort()
        end = perf_counter()
        return  'metoda predefinita <.sort()>','timpul initial:',start,'timpul final:',end,'intervalul temporal:',end-start
f=open('txt.in')
T=int(f.readline())
print(T)
for i in range(T):
    print(i,' :')
    n, Max = f.readline().split()
    n = int(n)
    Max = int(Max)
    sir_nesortat=generator(n,Max)
    for nr_sort in range(6):
        sir=sir_nesortat.copy()
        print(*sortari(nr_sort,sir,n,Max),test_sort(sir))
        print()
f.close()