class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        Solution:
        1. First element
        2. check if the next element is equal to first_element
        3. skip that - set index_to_be_replaced = index_of_first_similar
        4. get_next_different_element , store it somewhere
        5. swap diff_elemenent = index_to_be_replaced
        6. increase counter  index_to_be_replaced+=1
        7. repeat this process.

        """

        if len(nums) <= 1:
            return len(nums)

        element = nums[0]
        index_to_be_replaced = -1

        for i in range(len(nums)):
            if i == len(nums) - 1:
                break

            if nums[i + 1] == element:
                if index_to_be_replaced == -1:
                    index_to_be_replaced = i + 1
                continue
            else:
                if index_to_be_replaced == -1:
                    element = nums[i + 1]
                else:
                    nums[index_to_be_replaced] = nums[i + 1]
                    index_to_be_replaced += 1
                    element = nums[i + 1]

        if index_to_be_replaced != -1:
            nums = nums[:index_to_be_replaced]

        return len(nums)
