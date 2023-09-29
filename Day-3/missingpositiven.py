def findNum(arr, n):
    if n==0:
        return 1
    i = 0
    while i < n:
        if arr[i]>= 1 and arr[i] <= n and arr[i]!=arr[arr[i] - 1] :
            temp = arr[i] - 1
            temp_2 = arr[i]
            arr[i] = arr[temp]
            arr[temp] =temp_2
        else:
            i +=1
    for i in range(n):
        if arr[i]!= i + 1 :
            return i + 1
    return n+1
arr=[10,4,-4,1]
n=len(arr)
print(findNum(arr,n))

