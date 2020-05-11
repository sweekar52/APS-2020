char = input("Input the character whose case has to be toggled ")
asci = ord(char)
if asci < 97 :
    asci |= 32
else :
    asci &= 95
char = chr(asci)
print(char)