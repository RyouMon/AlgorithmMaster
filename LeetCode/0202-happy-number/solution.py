def getNext(n: int) -> int:
    result = 0

    while n:
        n, m = divmod(n, 10)
        result += pow(m, 2)

    return result


class Solution01:
    """
    使用集合探测循环
    """

    def isHappy(self, n: int) -> bool:

        record = set()

        while (n != 1) and (n not in record):

            n = getNext(n)

            record.add(n)

        return n == 1


class Solution02:
    """
    快慢指针
    """

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = getNext(n)

        while (fast != 1) and (slow != fast):

            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1
