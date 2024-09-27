class Solution:
    def isValid(self, s: str) -> bool:
        b_dict = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['s']
        for brac in s:
            if brac in b_dict:
                stack.append(brac)
            elif b_dict[stack.pop()] != brac:
                return False
        return len(stack) == 1

