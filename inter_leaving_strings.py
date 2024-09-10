def match_string(m,n,i,j,k,s1,s2,s3,dp):
    
    if k==len(s3):
        return i==m and j==n
    # s1[k]=match_string(m,n,i+1,j,s3)
    # s2[k]=match_string(m,n)
    # dp=[False]*len(s3)
    # if dp!=False:
    #     return dp
    # for k in range(len(s3)):
    if dp[i][j]!=-1:
        return dp[i][j]
    if i<m and s3[k]==s1[i]:
        
        # if next character also matches with i of s1 then take priority of s1 and increment it.
        if match_string(m,n,i+1,j,k+1,s1,s2,s3,dp):
            dp[i][j]=1 
            return True
    if j<n and s3[k]==s2[j]:
        if match_string(m,n,i,j+1,k+1,s1,s2,s3,dp):
            dp[i][j]=1 
            return True
        
    dp[i][j]=0 
    return False
        # match_string(m,n,i+1,j+1,s3)
    # return dp[k]
def interleaving_strings(s1,s2,s3):
    # here we need to compare the both s1 and s2 simultaneously 
    # with the s3, i and j run of s1 and s2. while another comparison pointer on s3.
    # if any of character matches from s1 or s2 then, suppose s1 got matches with character on s3
    # then s1 pointer moves to forward and s2 remains at same. similarly for s2.
    # if continuously mathcing chars from same string means need to move that pointer only.
    # the one who mathced recently have high priority to move if both got matched at a same time.
    # once i==len(s1)-1 and j==len(s2)-1 and s3 string have not chars left then retun 1 or true.
    m=len(s1)
    n=len(s2)
    if m+n!=len(s3):
        return False
    dp=[[-1 for _ in range(n+1)]for _ in range(m+1)]
    return match_string(m,n,0,0,0,s1,s2,s3,dp)
    # lets do this with recursion 
    
    
s1='aabcc'
s2='dbbca'
s3='aadbbcbcac'
print(interleaving_strings(s1,s2,s3))
