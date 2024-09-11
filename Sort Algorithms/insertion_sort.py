class InsertionSort:
    
    def sort(self, arr):
        N = len(arr)
        for i in range(N):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else: break
        return arr

def main():
    items = []
    for line in sys.stdin:
        items.extend(line.split())
    print('     items: ', items)
    print('sort items: ', InsertionSort().sort(items))

if __name__ == "__main__":
    import sys
    main()
    
