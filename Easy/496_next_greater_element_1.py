
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op=[]
        for i in nums1:
            if i in nums2:
                ind=nums2.index(i)
                ls=nums2[ind+1:]
                if len(ls)>0:
                    mx=max(ls)
                    if mx>i:
                        op.append(nums2[ind+1])
                    else:
                        op.append(-1)
                else:
                    op.append(-1)
            else:
                op.append(-1)

        return op



