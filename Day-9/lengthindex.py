name=[['Abhishek','43848'],['Mayur', '3749'],['Friend','3949'],['Yeah','7878']]
s=''
m=[]
n=[]
o=[]
op=''
for i in name:
    m.append(i[0])
for i in name:
    n.append(i[1])
for i in range(len(m)):
    q=[]
    for p in m[i]:
        q.append(p)
        for j in range(len(n)):
            l=0
            for k in n[j]:
                k=int(k)
                if k<=len(m[i]) and k>l :
                    l=k
            if l==0:
                o.append('x')
                
    o.append(q[l-1])
print(''.join(map(str, o)))      