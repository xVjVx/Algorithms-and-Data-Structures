class HeapSortTrace:
    def sort(self, a):
        self.N = len(a)
        for k in range(int(self.N / 2), 0, -1):
            self.sink(a, k, self.N)
        while self.N > 1:
            self.exch(a, 1, self.N)
            self.N -= 1
            self.__trace(a)
            self.sink(a , 1, self.N)

    def exch(self, a, i, j):
        a[i - 1], a[j - 1] = a[j - 1], a[i - 1]

    def sink(self, a, k, n):
        while 2 * k <= n:
            j = 2 * k
            if j < n and a[j - 1] < a[j]: j += 1
            if not a[k - 1] < a[j - 1]: break
            self.exch(a, k, j)
            k = j

    def __trace(self, a):
        for letter in a:
            print(letter, end=' ')
        print()

if __name__ == '__main__':
    hpt = HeapSortTrace()
    word = str(input()).split()
    hpt.sort(word)