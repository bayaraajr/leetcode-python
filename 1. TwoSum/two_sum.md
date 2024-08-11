## Two sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Solution
While looping through the array, if the difference between the target and the current element are equal return the current element with the map key and current element's index;


## Complexity
Time complexity : `O(n)` Because it only loops through the elements once.
Space complexity: `O(n)` Worst case scenario, the first and last element of the array add up to the target. Then this algorithm will push every element to the map and makes it `O(n)` instead of `O(1)`