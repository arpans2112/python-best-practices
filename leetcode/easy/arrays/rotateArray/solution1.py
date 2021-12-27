class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Question:
        What if k = 0
        What if k > len(nums)
        what if k < len(nums)

        Note: when k == length of the array, rotation turns into the same array.


        """
        # Case1:
        if k % len(nums) == 0:
            return nums

        # case 2:
        # when k > len(nums)
        # when k is equal to length, then rotation is euql to same error, and for rest of the left
        # numbers we need to do the rotation as we are doing for k < len(nums)
        # i.e k = k % len(nums)
        # When k < len(nums), then k = k

        k = k if k <= len(nums) else k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
