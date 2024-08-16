def reverse(arr,n,k):
    # need to reverse at every k groups of elements.
    # if elements remained in array less than k value then they need to be swap.
    # if k=3, then need to take 3 elements and swap them repeatedly.if elements left less than k means swap them, and if k is greater than len(arr) swap entire array.
    i=0 
    while i<n:
        left=i 
        right=min(i+k-1,n-1)
        #left starts at first index.
        #right index placed at last value so i+k-1 
        #here taking minimum value from (i+k-1,n-1)
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left=left+1 
            right=right-1 
        i=i+k 
    if k>=len(arr):
        return arr[::-1]
    size=n
    for i in range(size):
        if size<k:
            return arr[i:]
        for j in range(i,i+k):
            arr[i],arr[j]=arr[j],arr[i]
            # if size<k:
                # arr[i],arr[j]=arr[j],arr[i]
        i=i+k 
        size=size-k
        # now need to check if remaining elements left less than k. Then they need to swap.
        # k=3, n=2 
arr=[1, 2, 3, 4, 5, 6,
                   7, 8]
k=3
n=len(arr)
print(reverse(arr,n,k))
print(arr)


# remove k length duplicates. 
def k_len_duplicates(s,k):
    dic=set()
    res=[]
    for i in range(len(s)-k+1):
        substr=s[i:i+k]
            # res=res+s[j]
        if substr not in dic:
            dic.add(substr)
            res.append(substr)
        # if substr in dic:
        #     break
    res=''.join(res[i] for i in range(0,len(res),k))
    return  res 
s='geeksforfreeksfo'
k=3
print(k_len_duplicates(s,k))
     

