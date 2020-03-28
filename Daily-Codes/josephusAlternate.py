import math
def josephusAlternate(n):
    if n==1:
        return 1
    if n&1:
        return 2 * josephusAlternate(math.floor(n/2)) + 1
    return  2 * josephusAlternate(math.floor(n/2)) - 1


n=13
print(josephusAlternate(n))