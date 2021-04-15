class Solution:
    def romanToInt(self, s: str) -> int:
        """
        https://leetcode.com/problems/roman-to-integer/
        """
        symbol_inversion = False
        symbol_dict = {
                        "I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000
        }
        sum = symbol_dict[s[0]]
        for i in range(1,len(s)):

            current_value = symbol_dict[s[i]]
            previous_value = symbol_dict[s[i-1]]
            print(f"previous value {previous_value} current_value {current_value} previous sum {sum}")
            if current_value > previous_value:
                symbol_inversion = True
                current_value -= previous_value
                print(f"current_value {current_value}")
            sum = sum + current_value - (previous_value if symbol_inversion else 0)
            symbol_inversion = False
            print(f"sum {sum}")
        return sum

pbm = Solution()
s = "MCMXCIV"
op = pbm.romanToInt(s)
print(op)

