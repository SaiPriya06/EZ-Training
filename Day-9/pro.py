s=input()
s=s.split(",")
d=s.index('4')
c=s.index('7')
m=''
k=0
for i in range(len(s)):
    if i>=d and i<=c:
        m=m+s[i]
    else:
        k=k+int(s[i])
print(int(m)+k)