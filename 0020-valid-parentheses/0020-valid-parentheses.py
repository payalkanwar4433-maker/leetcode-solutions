class Solution(object):
    def isValid(self, s):
        self.s=s
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""
                


