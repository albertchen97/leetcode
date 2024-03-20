class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 0:
            if n != 1 and n % 2 != 0:
                return False
            n //= 2
        return True

    def test(self, n: int):
        if self.isPowerOfTwo(n):
            print("True")
        else:
            print("False")

sol = Solution()
sol.test(1)
sol.test(16)
sol.test(3)
            
