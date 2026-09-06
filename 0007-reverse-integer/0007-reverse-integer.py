class Solution(object):
    def reverse(self, x):
        reverse = 0

        if x > 0:
            while x > 0:
                digit = x % 10
                reverse = reverse * 10 + digit
                x = x // 10

        elif x < 0:
            x = -x

            while x > 0:
                digit = x % 10
                reverse = reverse * 10 + digit
                x = x // 10

            reverse = -reverse

        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return reverse