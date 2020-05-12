def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        n -= 1
        if bin(n).count("1") %2 == 0:
            print("Richard")
        else:
            print("Louise")

if __name__ == "__main__":
    main()