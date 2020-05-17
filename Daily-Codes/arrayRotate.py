def rotate(arr, n):
  return arr[-n:]+arr[:-n]

def main():
  n, k, q = map(int, input().split())
  k = k%n
  arr = list(map(int, input().split()))

  arr = rotate(arr, k)
  for _ in range(q):
    print(arr[int(input())])

if __name__ == "__main__":
    main()