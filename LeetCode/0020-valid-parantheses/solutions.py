class Solution:

    @classmethod
    def isValid(cls, s: str) -> bool:
        stack = []
        mapping = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in '([{':  # 当前是左括号则入栈
                stack.append(char)
            elif stack and stack[-1] == mapping[char]:  # 当前为匹配的右括号则出栈
                stack.pop()
            else:  # 不是匹配的右括号或没有左括号与之匹配，则返回 False
                return False

        return stack == []


if __name__ == '__main__':
    assert Solution.isValid('()') is True
    assert Solution.isValid('()[]{}') is True
    assert Solution.isValid('(]') is False
    assert Solution.isValid('([)]') is False
    assert Solution.isValid('{[]}') is True
