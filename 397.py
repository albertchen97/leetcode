class Solution:
    def __init__(self):
        self.memo = {1: 0}
    def integerReplacement(self, n: int) -> int:
        if n >= 1:
            if n in self.memo:
                return self.memo[n]
            else:
                if n % 2 == 0:
                    self.memo[n] = 1 + self.integerReplacement(n / 2)
                else:
                    self.memo[n] = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
            return self.memo[n]
s = Solution()
print(s.integerReplacement(8))
print(s.integerReplacement(7))
print(s.integerReplacement(4))
