class Solution:
    def isValid(self, s: str) -> bool:
        ss = []
        for q_bracket in s:
            if q_bracket == "}":
                if ss:
                    a_bracket = ss[len(ss)-1]
                    if a_bracket == "{":
                        ss.pop()
                    else:
                        ss.append(q_bracket)
                else:
                    return False
            elif q_bracket == "]":
                if ss:
                    a_bracket = ss[len(ss)-1]
                    if a_bracket == "[":
                        ss.pop()
                    else:
                        ss.append(q_bracket)
                else:
                    return False
            elif q_bracket == ")":
                if ss:
                    a_bracket = ss[len(ss)-1]
                    if a_bracket == "(":
                        ss.pop()
                    else:
                        ss.append(q_bracket)
                else:
                    return False
            else:
                ss.append(q_bracket)
        
        if ss:
            return False
        else : 
            return True

