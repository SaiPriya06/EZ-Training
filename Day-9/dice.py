l=list(map(int,input().split()))
m=list(map(int,input().split()))
c = [0] * 36
for i in range(0,len(l)):
    for j in range(0,len(m)):
        c[l[i]+m[j]+1]+=1
print(max(c))