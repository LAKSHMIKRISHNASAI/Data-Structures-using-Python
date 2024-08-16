# practic problem of anagrams 
# contains list of words need to print the list of words are anagrams for each other.
# first need to sort the characters in the each word and then sort the words according to words range.
def word_anagrams(arr):
    original_arr=arr.copy()
    # word_arr=[]
    # for i in range(len(arr)):
    #     arr[i]=(arr.index(arr[i]),arr[i])
    #     word_arr.append(arr[i])
        # print(arr_index,word)
    # print(word_arr)
    # tac,1 cat,2 
    for i in range(len(arr)):
        arr[i]=(''.join(sorted(arr[i])),i)
    arr=sorted(arr)
    print(arr)
    for i in range(len(arr)):
        print(original_arr[arr[i][1]],end=' ')
    # for i in arr:
    #     print(original_arr,end=' ')
arr=['cat','dog','tac','god','act']
word_anagrams(arr)


# from collections import defaultdict
def create_dup_arr(arr,size):
    dup_arr=[]
    for i in range(size):
        dup_arr.append((arr[i],i))
    return dup_arr 
def word_anagrams(arr,size):
    duparr=create_dup_arr(arr,size)

    # now only approach is sort each word in the words array
    # and then merge them. then sort the entire array and later from the index position of duparr print the words from original arr.
    for word in range(size):
        duparr[word]=(sorted(duparr[word][0]),duparr[word][1])
    duparr.sort()
    print(duparr)
    for i in range(len(arr)):
        print(arr[duparr[i][1]],end=' ')
    # duparr=sorted(duparr,key=lamb)
    # groupedlist=defaultdict(list)

    # for word in arr:
    #     groupedlist[''.join(sorted(word))].append(word)
    
    # for value in groupedlist.values():
    #     print(' '.join(value))
words=['cat','dog','tac','god','act']
size=len(words)
word_anagrams(words,size)

#####################################################################
# RABINKARP ALGORITHM
def find_pattern(word,pattern):
    m=len(pattern)
    n=len(word)
    for i in range(n-m+1):
        j=0
        while j<m and pattern[j]==word[i+j]:
            j=j+1 
        if j==m:
            print('text found at index:',i)
word='GEEKS FORGEEKS'
pattern='GEEKS'
find_pattern(word,pattern)

# equal 0s,1s and 2s 
# approach is iterating through strings finding substrings having equal 0,1 and 2.
 
def count_strings(s):
    arr=[]
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            s1=''
            for k in range(i,j+1):
                s1=s1+s[k]
            arr.append(s1)
    count=0
    for i in range(len(arr)):
        zcount=0
        ocount=0
        tcount=0
        curs=arr[i]
        for j in range(len(curs)):
            if curs[j]=='0':
                zcount+=1 
            if curs[j]=='1':
                ocount+=1 
            if curs[j]=='2':
                tcount+=1 
        if zcount==ocount and ocount==tcount:
            count+=1
    return count

    # print(arr)
s='102100211'
print(count_strings(s))


# find largest word in dictionary 

# approach is used to find the largest word comparing with the list of dictionaries.
# string is given need to go through string in which finding the longest common word appear in the dictionary.
# abpcplea - apple 

