
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_ele=min(strs,key=len)
        subst=""
        for i in range(len(min_ele)):
            for j in range(len(strs)):
                if min_ele[i]!=strs[j][i]:
                    return subst
            subst+=min_ele[i]
        return subst

        
