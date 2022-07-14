
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dt={}
        for i in nums:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
        for i in dt:
            if dt[i]==1:
                return i
            
                
        
