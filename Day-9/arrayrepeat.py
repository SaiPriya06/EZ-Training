n,k=map(int,input().split())
lst=[]
c=0
for i in range(n):
    lst.append(int(input()))
s=set(lst)
for i in s:
    if lst.count(i)>=k:
        c+=1
print(c)
    