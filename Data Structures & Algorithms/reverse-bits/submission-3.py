class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            rightbit=n&1 #so 
            shifted_bit=(rightbit<<(31-i)) #moves rightbit to pos 31 and makes 0-30 0
            result= result|shifted_bit #or with result, so we dont care what result currenlty is we just want right bit, hence we OR rathern than AND
            n=n>>1
        return result 
