str1=input("Enter the first string\t")
str2=input("Enter the second string\t")

s1=list(str1)
s2=list(str2)




sub=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            sub[i][j]=sub[i-1][j-1] + 1
        else:
            sub[i][j] = 0

len1=0

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if sub[i][j] > len1:
            len1=sub[i][j]
print(len1)