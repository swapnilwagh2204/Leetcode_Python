
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        not_in_nums=[]
        n=len(nums)
        for i in range(1,n+1):
            if i not in nums:
                not_in_nums.append(i)
        return not_in_nums

    
#     optimised_approach:

    nums1={i for i in range(1,len(nums)+1)}
    op=nums1-set(nums)
    return op
        
