'''
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
'''


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        str_n = str(n)
        high = str_n[0]
        pow_ = 10 ** (len(str_n) - 1)
        last = n - int(high) * pow_

        if high == '1':
            # 例如当前数字为1234
            # 第一位是1，返回0-999的1数量 + 234的1数量 + 1000-1234的最高位1的数量
            return self.countDigitOne(pow_ - 1) + self.countDigitOne(last) + last + 1
        else:
            # 例如当前数字 87654
            # 第一位不是1，则返回0-9999的1数量 * 8 + 10000-19999的开头1数量 + 7654的1数量
            return self.countDigitOne(pow_ - 1) * int(high) + pow_ +self.countDigitOne(last)


solution = Solution()
n = 1234
print(solution.countDigitOne(n))