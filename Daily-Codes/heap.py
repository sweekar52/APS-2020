
#max heap
def heapify(arr,n):
  for i in range(n//2,0,-1):
    k = i
    v = arr[k]
    heap = False
    while not heap and 2*k<n+1:
      j = 2*k
      if(j<n):
        if(arr[j]<arr[j+1]):
          j += 1
      
      if(arr[k]>arr[j]):
        heap = True
      
      else:
        arr[k] = arr[j]
        k = j
    arr[k] = v

def main():
  arr = [0,2,4,6,3,5,8,6,9]

  heapify(arr, 8)
  print(arr) 

if __name__ == "__main__":
    main()