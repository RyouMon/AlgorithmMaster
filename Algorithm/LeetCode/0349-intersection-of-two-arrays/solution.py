from typing import List


class Solution01:
    """
    使用两个set
    """

    def set_intersection(self, set1: set, set2: set) -> List:
        return [n for n in set1 if n in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) > len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


class Solution02:
    """
    使用内置方法
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
