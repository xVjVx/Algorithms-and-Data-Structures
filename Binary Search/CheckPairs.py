class OPar:
    def __init__(self, size, first):
        self.a = []
        for i in range(size):
            self.a.append(first + i)
        self.a.sort()

    def checkPairs(self):
        count = 0
        N = len(self.a)
        for i in range(N):
            lo = 0
            hi = N - 1
            key = self.a[i] * - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if self.a[mid] < key:
                    lo = mid + 1
                elif self.a[mid] > key:
                    hi = mid- 1
                else:
                    count += 1 
                    break

        return count

if __name__ == "__main__":
    size = int(input())
    first = int(input())
    soma = OPar(size, first)
    print(soma.checkPairs())