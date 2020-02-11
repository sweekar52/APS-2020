#s1=['a','c','d','a']
#s2=['b','d','a','b','a','c']

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
            sub[i][j] = max(sub[i-1][j],sub[i][j-1])

print(sub[len(s1)][len(s2)])
