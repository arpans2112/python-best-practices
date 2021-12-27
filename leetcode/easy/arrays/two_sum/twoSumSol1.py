class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Questions to be asked:
        1. is the elements are sorted
        2. can the given array be empty
        3. do we have positive and negative values in the array or the only positive.
        4. what's the format of output you want - want to return bool for found or not found, or index of the array ?
        5. 2 <= nums.length <= 104
        6. -109 <= nums[i] <= 109
        7. -109 <= target <= 109

        Solution 1: bruit force approach (n*n)
           1. get all the pairs
           2. if targe = sum(pair)
           3. Return the index of those two pairs.

        Solution 2: (nlogn)
           1. current_number = x
           2. second_number = target - x
           3. check the second_number in rest of the array, if found return the index
           4. if not found, change your current_number = next number
           5. Repeat the process.

        Solution 3 : O(n)

            1. additional space we will use to store the compliment of the element and it's index
            2. current_element = x
            3. second_element = target - x
            4. check if the second_element in the map if not store in the map
            5. if the element found in the map, stop finding
            6. and get the index from the map and the index of the current element.

        """

        comp_dict = dict()

        for index, value in enumerate(nums):
            if value in comp_dict:
                return [comp_dict.get(value), index]
            else:
                comp_dict[target - value] = index
