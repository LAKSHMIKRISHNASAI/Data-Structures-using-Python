
# need to find the longest matching word from the list of words with the given common string.
# def is_substring(word,s):
#     m=len(word)
#     n=len(s)
#     # here need to compare the given s string with word, if character of s matches with word
#     # then only move forward the word character pointer else if unmatched then move s string pointer.
#     i=0  #pointer of word
#     j=0 #pointer of s
#     while i<m and j<n:
#         if word[i]==s[j]:
#             i=i+1 
#         j=j+1 
#     return i==m # i need the matched characters of word not the string s.
# def find_largest_word(arr,s):
#     # approach is comparing to find matching of given universal string with the list of words in the dictionary.
#     # if not matching then skip the letters.
#     # here need to finalize the matched word with longest length so size of word also matters.
#     res=''
#     length=0
#     for word in arr:
#         if length<len(word) and is_substring(word,s):
#             res=word 
#             length=len(word)
#     return res
# arr=["ale", "apple", "monkey", "plea"]
# s='abpcplea'
# print(find_largest_word(arr,s))

# check whether the two strings are isomorphic or not.
# if both patterns are similar with same length then called as isomorphic.
# approach is start with len of s1 and s2, initiate an map to store the ord of one string and keep the s2 characters in that s1 ord positions.
# first mark as false and start map with -1. if character of s1 is not seen before but character already seen before in s2 that means false.
# and mark that s2 char as visited, if curr character of s1 is not first appearance then check if previous character is definitely mapped with s2.if not return false.
def is_isomorphic(s1,s2):
    m=len(s1)
    n=len(s2)

    chars=256 
    visited=[False]*chars
    map=[-1]*chars 
    if m!=n:
        return False
    for i in range(n): 
        if map[ord(s1[i])]==-1:
            # but s2 has already visited the character then return false.
            if visited[ord(s2[i])]==True:
                return False 
            
            visited[ord(s2[i])]=True 
            map[ord(s1[i])]=s2[i]
        elif map[ord(s1[i])]!=s2[i]:
            # if char of s1 is not first appearance for s2. 
            return False 
    return True
s1='aab'
s2='xxy'
print(is_isomorphic(s1,s2))

