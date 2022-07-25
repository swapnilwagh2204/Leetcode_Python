
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
