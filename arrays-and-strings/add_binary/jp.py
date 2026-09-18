"""
Key is to think of adding two binary numbers like adding 2 regular numbers

Big piece of this problem is the carry which happens when you add 2 numbers that can't be represented in 1 decimal place 
Ex: 9 + 1 = 10 which can't be represented in 1 position, so u have to carry the 1 to the left
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2) #Base 2
        b = int(b, 2)
        
        while b:
            #do an xor and ignore anything that needs to be carried over (1001 ^ 101 is 1100)
            without_carry = a ^ b
            #Doing a & b indicates places where a carry should happen. Since if you have 2 ones, that resolves to a 1.
            #Then you shift it 1 position to the left just like adding the carry to the left in normal addition.
            carry = (a & b) << 1

            #If you take a and b, a is basically now the numbers added together ignoring carry. b is the carry that needs to be added. 
            #So you add them together just like normal addition and keep going until there is no carry left
            a = without_carry
            b = carry
        return bin(a)[2:]


def test():
    sol = Solution()
    print(sol.addBinary("1001", "101"))

if __name__ == "__main__":
    test()