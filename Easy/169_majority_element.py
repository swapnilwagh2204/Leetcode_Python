
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=int(len(nums)/2)
        dt={}
        for i in nums:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
        for i in dt:
            if dt[i]>n:
                return i
                
        
