
def main():
    _ = int(input())
    valley = input()

    currentSign = 1
    valleyCount = 0

    currentLevel = 0

    for l in valley:
        if l == 'U':
            currentLevel += 1
            # print("/", end="")
        else:
            currentLevel -= 1
            # print("\\", end="")

        prevSign = currentSign
        if currentLevel < 0:
            currentSign = -1
        else:
            currentSign = +1

        if prevSign!=currentSign and currentSign == -1:
            valleyCount+=1
    print(valleyCount)

if __name__ == "__main__":
    main()