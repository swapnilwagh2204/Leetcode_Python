
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct=nums.count(val)
        for i in range(ct):
            nums.remove(val)
        ln=len(nums)
        for i in range(ct):
            nums.append("_")
        return ln
