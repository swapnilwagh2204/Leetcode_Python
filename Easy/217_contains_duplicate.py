
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dt={}
        for i in nums:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
        for i in dt:
            if dt[i]>=2:
                return True
        return False
        
