class Solution:
    def balancedStringSplit(self, _str: str) -> int:
        _result = 0
        bal = 0
        for s in _str:
            if s == 'R':
               bal +=1 
            else:
                bal -=1
            if not bal:
                _result += 1
        return _result    