def merge(arr,start,mid,end):
    # merge sort is need to divide the array into parts.
    # mid=len(arr)//2
    left=arr[start:mid+1]
    right=arr[mid+1:end+1]
    i=0
    j=0
    # here need to divide the array into parts and merge them.
    k=start
    # res=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1 
        else:
            arr[k]=right[j]
            j=j+1 
        k=k+1 
    # if arr is pending 
    while i<len(left):
        arr[k]=left[i]
        i=i+1 
        k=k+1
    while j<len(right):
        arr[k]=right[j]
        j=j+1 
        k=k+1 
def merge_sort(arr,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,start,mid,end)

arr=[12,3,21,15,6,17,5,1]
merge_sort(arr,0,len(arr)-1)
print(arr)

# # used to select the pivot element from the array and divide the array left and right side of pivot element.
def partition(arr,start,end):
    pivot=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    # approach is need to start two pointers, second pointer is used to swap the element 
    # first it checks while loop if element lower than pivot element found then swap that greater element pointed by i. 
    arr[i+1],arr[pivot]=arr[pivot],arr[i+1]
    return i+1
    # here one pointer points at greater element pointer by if any element found lesser than pivot element then swap greater element with that lesser element.
    # and move pointer, else swap pivot element with the greater element.

def partition(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<pivot]
    right=[x for x in arr[1:] if x>=pivot]
    return partition(left)+[pivot] +partition(right)
# def quicksort(arr,start,end):
#     if start<end:
#         pi=partition(arr,start,end)
#         quicksort(arr,start,pi-1)
#         quicksort(arr,pi+1,end)

arr=[12,3,21,15,6,17,5,1]
res=partition(arr)
print(res)

# # find the length of the longest substring without repeating the characters.


def find_longest_substring(s):
    # first creates the method to store the all substrings and find longest length.
    # another method to verify and return the substrings having unique characters.
    res=0
    for i in range(len(s)):
        visited=[0]*256
        for j in range(i,len(s)):
            if visited[ord(s[j])]==True:
                # if already visited
                # return False 
                break
            else:
                res=max(res,j-i+1)
                # and if it is not visited yet then mark it true
                visited[ord(s[j])]=True
        # and remove the prevous window  
        visited[ord(s[i])]=False 
    return res 
s='geeksforgeeks'
print(find_longest_substring(s))
def is_distinct(s,i,j):
    visited=[0]*256
    for x in range(i,j+1):
        if visited[ord(s[x])]==True:
            return False 
        # if not visited yet then mark as true.
        visited[ord(s[x])]=True 
    return True 
def find_substring(s):
    res=0 
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            if is_distinct(s,i,j):
                res=max(res,j-i+1)
    return res
s='geeksforgeeks'
print(find_substring(s))


# # check if a string is substring of another
def check_substring(s1,s2):
    m=len(s1)
    n=len(s2)
    # j=0
    # for i in range(n):
    #     for j in range(m):
    #         if s2[i]==s1[j]:
    #             return i   
    # return -1
    for i in range(n-m+1):
        for j in range(m):
            if s1[j]==s2[i+j] and j+1==m:
                return i 
    return -1


s1='for'
s2='geeksforgeeks'
print(check_substring(s1,s2))
            

