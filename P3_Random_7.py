# If you have access to a function that returns a random integer from one to five,
# write another function which returns a random integer from one to seven.
 
import random
 
 
class Solution():
 
    def rand5(self):
        return random.randint(1, 5)
 
    def rand7(self):
        return (((s.rand5()+s.rand5()+s.rand5())%7)+1)
        # One other solution
        # while True:
        #     r = 5 * (self.rand5() - 1) + self.rand5()
        #     if r <= 21:
        #         break
        # return r % 7 + 1
 
s = Solution()
print(s.rand7())