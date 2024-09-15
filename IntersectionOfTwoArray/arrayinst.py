class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        res=[]
        for i in range(0,len(nums2)):
            if nums2[i] in seen:
                res.append(nums2[i])
                seen.remove(nums2[i])

        return res





        
