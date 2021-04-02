class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        rulekey_to_rulevalue_map = {'type':0, 'color': 1, 'name': 2}
        for i in items:
            if i[rulekey_to_rulevalue_map[ruleKey]] == ruleValue:
                result +=1
        return result