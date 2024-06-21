arr=list(map(int, input().split()))
t=int(input())
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if t==arr[i]+arr[j]:
            print(i+1,j+1)
            break