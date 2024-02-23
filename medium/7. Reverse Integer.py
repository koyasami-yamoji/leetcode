
class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        if str(x)[0] == '-':
            res += '-' + str(int(str(x)[:0:-1]))
        else:
            res += str(int(str(x)[::-1]))
        if int(res) >= 2147483647:
            return 0
        else:
            return int(res)