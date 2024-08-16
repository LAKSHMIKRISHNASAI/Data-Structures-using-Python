# approach for quicksort algorithm is finding/selecting the pivot element first.
# make the two pointers left and right of array. one pointer if value greater pivot and another pointer which is found lesser than pivot then 
# both the pointers swap each other. left pointer increments and right pointer decrements. while left < right.
# when left > right reaches then need to swap the pivot element with that right pointer and return that pointer.
def partition(arr,low,high):
    pivot=arr[high]

    #assigning the pointer initially starts at the -1 index
    i=low-1 
    
    for j in range(low,high):
        if arr[j]<=pivot:
                #if any element with pointer j then swap it with the greatest element pointed by i.
            i=i+1 
            arr[i],arr[j]=arr[j],arr[i]
    #when the low > high then need to swap pivot element with low pointer
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
arr=[12,3,1,15,7,18,21,17]
quicksort(arr,0,len(arr)-1)
for i in arr:
    print(i,end=' ')
