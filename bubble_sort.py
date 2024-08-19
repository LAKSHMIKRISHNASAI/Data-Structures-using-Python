def bubble_sort(arr):
#     used to swap the adjacent elements by comparing with each other
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[12,2,14,7,16,27,3]
bubble_sort(arr)
            
        
