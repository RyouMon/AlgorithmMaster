from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        offset = 0  # 偏移量
        num = 1  # 需要填充的数字
        loop = n // 2  # 一共需要画的轮数
        step = n - 1  # 画每条边需要的次数

        for _ in range(loop):

            for x in range(step):

                result[0+offset][x+offset] = num
                num += 1

            for y in range(step):

                result[y+offset][n-1-offset] = num
                num += 1

            for x in range(step, 0, -1):

                result[n-1-offset][x+offset] = num
                num += 1

            for y in range(step, 0, -1):

                result[y+offset][0+offset] = num
                num += 1

            offset += 1
            step -= 2

        # 如果 n 为奇数，需要单独给中心点赋值
        if (n % 2 == 1):
            mid = int((n - 1) / 2)
            result[mid][mid] = num

        return result
