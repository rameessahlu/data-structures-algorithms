class Solution:
    def fibHelper(self, n, d):
        if n not in d and n >= 1:
            d[n] = self.fibHelper(n-1, d) + self.fibHelper(n-2, d)
        return d[n]
    
    def fib(self, n: int) -> int:
        return self.fibHelper(n, {1: 1, 0 : 0})