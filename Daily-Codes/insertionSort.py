def insertionSort(arr,n):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        for i in arr:
            print(i, end=' ')
        print()
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    insertionSort(arr,n)
    # print(arr)

if __name__ == "__main__":
    main()