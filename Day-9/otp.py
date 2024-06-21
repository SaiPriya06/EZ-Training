n=(input())
n=list(n)
m=[]
for i in range(0,len(n)):
    if i%2!=0:
        n[i]=(int(n[i])**2)
        m.append(n[i])
r = ''.join(map(str, m))
print(int(str(r)[:4]))
#2 method
n=input()
s=""
for i in range(1,len(n),2):
    s=s+str(int(n[i])**2)
print(s[:4])
#3 method
def demo(n):
    n=str(n)
    s=""
    for i in range(1,len(n),2):
        s=s+str(int(n[i])**2)
        s=s[:4]
    return s
if __name__=='__main__':
    print(demo(7564168))

    

        
    

        