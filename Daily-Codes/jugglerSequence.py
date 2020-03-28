import math
def juggler(a):
    print(a)
    while(a != 1):
        if a&1:
            b=math.floor(math.sqrt(a)*math.sqrt(a)*math.sqrt(a))
        else:
            b=math.floor(math.sqrt(a))
        print(b)
        a=b

a=3
juggler(a)