class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        1. Time Limit Exceed or this solution: Not a good solution


        Do not return anything, modify nums in-place instead.
        # can we use another data structure to solve this or it's in place - No other datastructure
        # assumption: There is minimum length = 1 : return as it's
        # number can be positive or negative.
        # Maintain relative order
        # return nothing as doing in place replacement


        Solution 1: start from begining,- O(N^2)
        # get index of the zero from the last
        # swap the elements until you reach at the end or you find the next zero
        # Continue this process until all elements are not processed
        # [0,1,0,3,12]

        Solution 2: - Insert and Remove - Dosn't seem to be inplace solution
                    - If list used shift will cause the issue
         case 1: [0,0,0,1] worse case
         case 2: [1,1,3,4,5,0,0]
         1. get count of zero in the list
         2. start from the last, get index of zero, remove that element and insert 0 in the begining
         3. until count reduce to zero.

         Solution 3: minium swapping - Best: O(N^2) - with minimum swaping
         1. Start from the left
         2. find index of the first zero,
         3. Swap with the next non-zero
         4. continue this process until you don't find any non-zero value next.

         Solution 4: Creat a new array : start from the begining - O(N) - with extra memory
         put all non zero value from the begining and zeros from the end in new array and start filling
         the new array, space will increase will be done in o(N) complexity.

        Test Case:
        [-1,5,0,0,0,3,12,4]
        [ 0,0,0,3,12,4 ]
        [ 3, 15, 0]
        [5]
        [5, 4, 3, 5]
        [2,0,0,0,0,0,0,4,5,6,7] -
        """

        #         Time Limit Exceed : Not optimized
        zero_index = -1
        non_zero_index = 0

        while (non_zero_index < len(nums)):
            if nums[non_zero_index] != 0:
                if zero_index != -1:
                    nums[zero_index], nums[non_zero_index] = nums[non_zero_index], nums[zero_index]
                    zero_index = -1
                    non_zero_index = zero_index + 1
            else:
                if zero_index == -1:
                    zero_index = non_zero_index
            non_zero_index += 1






