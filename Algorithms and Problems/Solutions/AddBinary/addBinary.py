class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        https://leetcode.com/problems/add-binary/

        Given two binary strings a and b, return their sum as a binary string.

        """
        result = []
        #A|B|Carry => (Sum,Carry)
        res_dict = {"111" : ("1","1"),
                    "110" : ("0","1"),
                    "101" : ("0","1"),
                    "100" : ("1","0"),
                    "011" : ("0","1"),
                    "001" : ("1","0"),
                    "010" : ("1","0"),
                    "000" : ("0","0"),
                    }
        length_of_A = len(a)
        length_of_B = len(b)
        carry = "0"
        # As long as both the strings have values
        while length_of_A > 0 and length_of_B > 0 :
            res = a[length_of_A-1]+b[length_of_B-1] + carry
            sum,carry = res_dict[res]
            print(f"Sum {sum} , Carry {carry} ")
            result += sum
            print(f"Result After {result}")
            length_of_A -= 1
            length_of_B -= 1

        print(f"length of A {length_of_A} length of B {length_of_B}")

        # When uneven lengths are given
        while length_of_A > 0:
            res = a[length_of_A-1] + "0" + carry
            sum,carry = res_dict[res]
            result += sum
            print(f"Result A After {result}")
            length_of_A -= 1

        while length_of_B > 0 :
            res = b[length_of_B-1] + "0" + carry
            sum,carry = res_dict[res]
            result += sum
            print(f"Result B After {result}")
            length_of_B -= 1


        if carry == "1" and (sum == "0" or sum == "1"):
            result += "1"
        return "".join(reversed(result))

pbm = Solution()
a = "1"
b = "111"
op = pbm.addBinary(a,b)
print(op)
