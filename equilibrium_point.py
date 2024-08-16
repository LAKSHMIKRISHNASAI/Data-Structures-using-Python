def find_equilibrium_point(arr):
    # leftsum=0
    # rightsum=0 
    l=0
    r=len(arr)
    while l<r:
        mid=(l+r)//2 
        leftsum=sum(arr[l:mid])
        rightsum=sum(arr[mid+1:r+1])
        if leftsum==rightsum:
            return arr[mid]
        if leftsum>rightsum:
            # then need to shift pointer towards left and move right arr towards left to balance sum
            while l>0:
                rightsum=rightsum+arr[mid]
                leftsum=leftsum-arr[mid-1]
                mid=mid-1
            if rightsum>leftsum:
                return -1 
            if leftsum==rightsum:
                return arr[mid]
        elif rightsum>leftsum:
            while r<=len(arr):
                leftsum=leftsum+arr[mid]
                rightsum=rightsum-arr[mid+1]
                mid=mid+1 
            if leftsum>rightsum:
                return -1 
            if leftsum==rightsum:
                return arr[mid]
# arr=[2, 3, 4, 1, 4, 5]
arr=[1,4,2,5,0]
print(find_equilibrium_point(arr))
#############################################################################################
def find_pair_with_sum(arr1,arr2):
    # approach is first find the sum of all elements in the both arrays
    # then find the difference between sum of two arrays 
    # based on the difference find the one element from arr1 and arr2 if sum of those two elements found difference
    # then swap them from one array position to another position.
    sumarr1=sum(arr1)
    sumarr2=sum(arr2)
    # if arr1 or arr2 is None:
    #     return None 
    # for i in range(len(arr1)):
    #     sumarr1=sumarr1+arr1[i] 
    # for i in range(len(arr2)):
    #     sumarr2+=arr2[i]
    
    # print(sumarr1)
    # print(sumarr2)
    # if sumarr1==sumarr2:
    #     print('no swapping is needed')
    diff=abs(sumarr1-sumarr2)
    # print(diff)
    # if diff==0:
    #     return
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j]==diff and abs(arr1[i]-arr2[j])==diff//2:
                print(arr1[i],arr2[j])
                return
               
arr1=[4, 1, 2, 1, 1, 2]
# arr1=[5, 7, 4, 6]
# arr2=[1, 2, 3, 8]
arr2=[3, 6, 3, 3]
find_pair_with_sum(arr1,arr2)
##########################################################################################
def find_first_repeating_letter(s):
    seen=set()
    for char in s:
        if char in seen:
            return char 
        seen.add(char)
    l=0
    r=l+1 
    while r<len(s):
        if s[l]==s[r]:
            return s[l]
        l=l+1
        r=r+1 
    str=''
    for i in range(len(s)-1,-1,-1):
        str=str+ s[i]
    return str
s='abccdeeghh'
print(find_first_repeating_letter(s))

def rain_water_trapping(heights):
    # approach is finding left max and right max.
    l=0
    r=len(heights)-1 
    leftmax=0
    rightmax=0
    res=0
    while l<r:
        if heights[l]>=heights[r]:
            if heights[l]>=leftmax:
                leftmax=heights[l]
            else:
                res=res+leftmax-heights[l]
            l=l+1
        else:
            if heights[r]>=rightmax:
                rightmax=heights[r]
            else:
                res=res+rightmax-heights[r]
            r=r-1 
    return res+1
# heights=[3,0,2,4,0,2]
heights=[0,1,0,2,1,0,1,3,2,1,2,]
print(rain_water_trapping(heights))
####################################################################


# convert roman number to integer 
def roman_to_int(arr):
    dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res=0
    prev=0
    n=len(arr)
    for i in range(n):
        if i<n-1 and dic[arr[i]]<dic[arr[i+1]]:
            res=res-dic[arr[i]]
        # if dic[arr[i]]>dic[arr[i-1]]:
        res=res+dic[arr[i]]
    # for i in range(n):
    #     if i<n-1 and dic[arr[i]]<dic[arr[i+1]]:

    return res
    # XXVII
# arr='XXVII' #--10+10+5+1+1
arr='XVII'
print(roman_to_int(arr))


# def roman_to_integer(arr):



