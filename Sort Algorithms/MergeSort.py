class MergeSort:
    def __init__(self):
        self.CUTOFF = 12

    def __merge(self, a, aux, lo, mid, hi):
        if a[mid - 1] <= a[mid]:
            return
        
        aux = a[lo:hi]
        i = lo
        j = mid

        for k in range(lo, hi):
            if i == mid:
                a[k] = aux[j - lo]
                j += 1
            elif j == hi:
                a[k] = aux[i - lo]
                i += 1
            elif aux[j - lo] < aux[i - lo]:
                a[k] = aux[j - lo]
                j += 1
            else:
                a[k] = aux[i - lo]
                i += 1

    def __sort(self, a, lo, hi):
        if hi <= lo + self.CUTOFF - 1:
            a = InsertionSort.sort(a)
            return
        
        mid = lo + (hi - lo) // 2
        self.__sort(a, lo, mid)
        self.__sort(a, mid, hi)
        self.__merge(a, lo, mid, hi)

    def sort(self, a):
        if len(a) <= 1:
            return
        
        is_sorted = all(a[i] <= a[i + 1] for i in range(len(a) - 1))

        if is_sorted:
            return
        
        self.__sort(a, 0, len(a))

def main():
    merge_sort = MergeSort()

    n = int(input())
    a = list(map(int, input().split()[:n]))
    merge_sort.sort(a)
    print(' '.join(map(str, a)))


if __name__ == '__main__':
    import InsertionSort
    main()