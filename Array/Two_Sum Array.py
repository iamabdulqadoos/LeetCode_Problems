class Solution:
    def twoSum(self, number, target):
        seen = {}

        for i, number in enumerate(number):
            complement = target - number 

            if complement in seen:
                return[seen[complement], i]

            seen[number] = i