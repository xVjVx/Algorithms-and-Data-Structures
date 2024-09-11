class ShellsortUnderMicroscope:
    def sort(self, arr):
        changes = []
        N = len(arr)
        h = 1

        while h < N // 3:
            h = 3 * h + 1

        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h and arr[j] < arr[j - h]:
                    arr[j], arr[j - h] = arr[j - h], arr[j]
                    changes.append(" ".join(arr))
                    j -= h

            h //= 3
            
        return changes
    
def main():
    word = input()
    arr = word.split()
    sort = ShellsortUnderMicroscope()
    word_sorted = sort.sort(arr)

    for change in word_sorted:
        print(change)


if __name__ == '__main__':
    main()