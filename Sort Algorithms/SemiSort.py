class SemiSort:
    def less(self, a, b):
        return a < b

    def exch(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def sort(self, arr, p):
        N = math.ceil(len(arr) * p)
        for i in range(1, N):
            j = i
            while j > 0 and self.less(arr[j], arr[j -1]):
                self.exch(arr, j, j - 1)
                j -= 1


def main():
    semi_sort = SemiSort()
    arr = []

    size = int(input())
    proportion = float(input())

    for _ in range(size):
        val = int(input())
        arr.append(val)

    semi_sort.sort(arr, proportion)
    
    for i in arr:
        print(i)

if __name__ == '__main__':
    import math
    main()