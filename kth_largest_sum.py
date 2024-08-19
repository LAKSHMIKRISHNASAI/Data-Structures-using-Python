# kth largest sum contigous subarray
def kthlargestsum(arr,k):
    res=[]
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            res.append(sum)
    res.sort(reverse=True)
    print(res)
    return res[k-1]
    
k=3
arr=[20, -5, -1]
# arr=[10, -10, 20, -4
