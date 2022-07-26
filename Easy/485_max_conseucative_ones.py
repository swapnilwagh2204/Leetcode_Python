
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls=[]
        count=0
        op=0
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            op=max(count,op)
        return op
      
      
      
