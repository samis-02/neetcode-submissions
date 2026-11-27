class Solution:
    def isValid(self, s: str) -> bool:
        ss = []
        d = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for q_bracket in s:
            if q_bracket in d:
                if ss:
                    a_bracket = ss[-1]
                    if a_bracket == d[q_bracket]:
                        ss.pop()
                    else:
                        return False
                else:
                    ss.append(q_bracket)
            else:
                ss.append(q_bracket)
        
        return not ss
