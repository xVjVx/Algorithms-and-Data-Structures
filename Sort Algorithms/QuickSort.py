class ParesLuvas:
    def binarySearch(self, a, key):
        lo = 0
        hi = len(a) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == key:
                return mid
            elif a[mid] < key:
                lo = mid + 1
            else: 
                hi = mid - 1

        return -1
    
    def __partition(self, a, lo, hi):
        pivot = a[hi]
        i = lo - 1

        for j in range(lo, hi):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[hi] = a[hi], a[i + 1]
        
        return i + 1
    
    def __sort(self, a, lo, hi):
        if lo < hi:
            pi = self.__partition(a, lo, hi)
            self.__sort(a, lo, pi - 1)
            self.__sort(a, pi + 1, hi)

    def sort(self, a):
        self.__sort(a, 0, len(a) - 1)

    def numberLostGloves(self, a, b):
        lost_count = 0

        for glove in a:
            if self.binarySearch(b, glove) == -1:
                lost_count += 1
        
        return lost_count
    
def main():
    pares_luvas = ParesLuvas()

    left_gloves_total = int(input())
    left_gloves = list(map(int, input().split()[:left_gloves_total]))

    right_gloves_total = int(input())
    right_gloves = list(map(int, input().split()[:right_gloves_total]))

    pares_luvas.sort(left_gloves)
    pares_luvas.sort(right_gloves)

    left_lost = pares_luvas.numberLostGloves(left_gloves, right_gloves)
    right_lost = pares_luvas.numberLostGloves(right_gloves, left_gloves)

    print(left_lost)
    print(right_lost)

if __name__ == '__main__':
    main()