h=[0]*50
size=-1

def parent(i):
#     the parent in the heap in (i-1)//2
    return ((i-1)//2)
    
def left(i):
    return (2*i+1)
def right(i):
    return (2*i+2)    
def insert(val):
    global size
    size=size+1
    h[size]=val
   
#     to correct the heap property need to check the inserted value with shift up heap property
    shift_up(size)
    return val
def shift_up(i):
    curr_index=i
    while curr_index>0 and (h[curr_index]>h[parent(curr_index)]):
        
        h[curr_index],h[parent(curr_index)]=h[parent(curr_index)],h[curr_index]
        current_index=parent(curr_index)   
    
def shift_down(i):
    largest=i
    l=left(i)
    if l<len(h) and h[l]>h[largest]:
        largest=l
    r=right(i)
    if r<len(h) and h[r]>h[largest]:
        laregst=r
    if largest!=i:
        h[largest],h[i]=h[i],h[largest]
        shift_down(largest)
    
def extract_max():
    global size
    res=h[0]
#     need to store removing root node in some where
#     h[0] #it is the root node of tree
#     h[-1]#leaf node of tree
    h[0]=h[size]
    size=size-1
#     now leaf node occupies the root node position now need to correct the max heap property within the tree
    shift_down(0)
    return res
def change_priority(i,p):
#     (old index,new index priority)
    oldp=h[i]
    h[i]=h[p]
#     now need to correct the heap structure
    if (p>oldp):
        shift_up(i)
    else:
        shift_down(i)
        
def remove(i):
#     depends on priority need to remove priority value first
    h[i]=h[0]+1
    shift_up(i)
    extract_max()
def get_max():
    return h[0]


insert(40)
insert(12)
insert(30)
insert(27)
insert(10)
insert(7)
insert(8)
insert(19)
insert(7)

i=0
while i<=size:
    print(h[i],end=' ')
    i=i+1
print()
extract_max()
j=0
while (j<=size):
    print(h[j],end=' ')
    j=j+1
print()
get_max()
# change_priority(2,49)
# change_priority(3,21)

# j=0
# while (j<=size):
#     print(h[j],end=' ')
#     j=j+1
# print()
# change_priority(4,13)
# k=0
# while (k<=size):
#     print(h[k],end=' ')
#     k=k+1
# print()
# remove(3)
# l=0
# while l<=size:
#     print(h[l],end=' ')
#     l=l+1
# print()
