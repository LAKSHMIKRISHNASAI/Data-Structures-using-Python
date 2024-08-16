#creating the two arrays where left and right arrays.
#left arrays contains the elements lesser than pivot 
#placing all the elements greater than pivot in right array.
# def quicksort(arr):
#     if len(arr)<=1:
#         return arr 
#     else:
#         pivot=arr[0]
#         left=[i for i in arr[1:] if i<pivot]
#         right=[j for j in arr[1:] if j>pivot]
#         return quicksort(left)+[pivot]+quicksort(right)
    
# arr = [1, 7, 4, 1, 10, 9, -2]
# res=quicksort(arr)
# print(res)

# sort the stack using recursion
def insert_stack(arr,ele):
    if len(arr)==0 or ele>arr[-1]:
        arr.append(ele)
        return 
    temp=arr.pop()
    insert_stack(arr,ele)
    arr.append(temp)

def sort_stack(arr):
    if arr:
        temp=arr.pop()
        sort_stack(arr)
        insert_stack(arr,temp)
        # if ele<arr[-1]:
def printstack(arr):
    for i in arr:
        print(i,end=' ')
# arr=[12,1,14,5,9,13,3,4]
arr=[]
arr.append(20)
arr.append(1)
arr.append(12)
arr.append(7)
arr.append(10)
arr.append(5)
sort_stack(arr)
printstack(arr)
