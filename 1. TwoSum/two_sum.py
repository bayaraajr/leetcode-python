# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
   def twoSum(self, nums, target):
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 

def main():
    s = Solution()
    print("Solution:", s.twoSum([1,2,3], 5))

if __name__=="__main__":
    main()