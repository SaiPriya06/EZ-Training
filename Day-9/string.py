s=input()
s=list(s)
m=[]
n=[]
for i in range(len(s)):
    if(s[i].isalnum()):
        m.append(s[i])
    else:
        c=i     
m.reverse()
m.insert(c,s[c])
r = ''.join(map(str, m))
print(r)