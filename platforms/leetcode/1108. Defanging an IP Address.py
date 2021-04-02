class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ''
        for c in address:
            if c is '.':
                result += '[.]'
            else:
                result += c
        return result