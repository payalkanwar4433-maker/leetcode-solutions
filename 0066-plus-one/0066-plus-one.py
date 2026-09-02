class Solution(object):
    def plusOne(self, digits):
        count = ""
        for i in digits:
            count = count + str(i)
            total_count = int(count) + 1
            result = []
            for i in str(total_count):
                result.append(int(i))
        return result
            