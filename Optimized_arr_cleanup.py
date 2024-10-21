class Solution:
    def empty_stack(self,arr,subseq_ind):
        new_arr=[arr[i] for i in range(len(arr)) if i not in subseq_ind]
        
        # for i in range(len(subseq_arr)):
        #     if arr[subseq_ind[i]]==subseq_arr[i]:
        #         arr.remove(arr[subseq_ind[i]])
        return new_arr
    def find_subarr(self,arr):
        #if len(arr)==0:
         #   return [],[],count_subseq
        subseq_arr=[]
        subseq_ind=[]
        for i in range(len(arr)):
            if arr[i] not in subseq_arr:
                subseq_arr.append(arr[i])
                subseq_ind.append(i)
            #break
        return subseq_arr,subseq_ind
    def minMoves(self, n, arr):
        # code here
        #here geek can select unique subsequent that is in the selected
        #subsequent all elements should be unique.
        #such that once we consider one subsequent we can check for next elements
        #by jumping to the next starting part of elements from subsequencts.
        
        # here another base case is geek have to consider is,
        #for eg: curr_subseq=[1, 2]
        #[1,2,1,2,3]---[1,2,3]--[3]--such that 3 not present in [1,2] so now need to
        #remove that [1,2] and create another operation [3] and remove 3 from stack []
        #and also if geek creates new subsequent the previous one will also remain for future checkings
        # [1,2] [3]
        #[1,2,3]--[1,2,3,1,2]
        #count+=1,[1,2]--[0]--count+=1--count=2
        #[1]--[1,1,1]
        #count=1,[1]--[1,1]--count=2,[1]--[1]
        #count=3,[]
        #[1,2,3,3,4,5,6,1,2,7,8]
        #count=1,[1,2,3]--[3,4,5,6,1,2,4,6]
        #count=2,[3,4,5,6,1,2]--[4,6]
        #okk here we can subsequence from the array in any form of order either by skipping the elements
        #here the logic is need to take a subsequence in such a way of having unique elements.
        #count=1,sarr=[1,2,3,4,5,6,7,8]--[3,1,2]
        #count=2,[3,1,2]--[]
        #subseq_arr=[]
        
        # if len(arr)==0:
        #     return countsubseq
        
        count_subseq=0
        while arr:
            subseq_arr,subseq_ind=self.find_subarr(arr)
            count_subseq+=1
            arr=self.empty_stack(arr,subseq_ind)
        # if len(subseq_arr)==0 and len(subseq_ind)==0:
        #     subseq_arr,subseq_ind,count_subseq=self.find_subarr(n,arr,subseq_arr,subseq_ind,count_subseq)
        # if subseq_arr and subseq_ind:
        #     res=self.empty_stack(arr,subseq_arr,subseq_ind)
        #     subseq_arr,subseq_ind,count_subseq=self.find_subarr(n,res,subseq_arr,subseq_ind,count_subseq)
        #first it need to take current arr and then extract the new_arr 
        #[3,1,2]-- and count+1 and then again go through making small arr. if  
        #arr=[3,1,2]
        #[1,1,1]
        return count_subseq
