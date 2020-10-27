from typing import List


class Solution01:
    """
    哈希法
    """

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        # 用来存储A[x]+B[x]的和出现的次数
        hashtable = dict()

        for a in A:
            for b in B:
                try:
                    hashtable[a+b] += 1
                except KeyError:
                    hashtable[a+b] = 1

        # 用来记录满足条件的元组出现的次数
        count = 0

        for c in C:
            for d in D:
                if hashtable.get(-(c+d)):
                    count += hashtable[-(c+d)]

        return count
