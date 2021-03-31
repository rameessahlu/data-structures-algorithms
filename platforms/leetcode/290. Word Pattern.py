class Solution:
    def wordPattern(self, pattern, s):
        _str = s.split(' ')
        foundedPattern = {}
        usedPatternChar = []
        if len(_str) != len(pattern):
            return False
        else:
            for i in range(0, len(_str)):
                if _str[i] not in foundedPattern and pattern[i] not in usedPatternChar:
                    foundedPattern[_str[i]] = pattern[i]
                    usedPatternChar.append(pattern[i])
                elif _str[i] not in foundedPattern and pattern[i] in usedPatternChar:
                    return False
                else:
                    if pattern[i] != foundedPattern[_str[i]]:
                        return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern('aba', 'happy hacking happy'))