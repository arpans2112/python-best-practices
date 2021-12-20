class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """

        solution:
        index_to_be_replaced = 1
        find_next_index not equal equal to element2, then idenfied index with index_to_be_replaced


        get_first_element
        check_next_element  that's distinct

        example:
        [1, 1] :
        [1, 2] :


        """

        index_to_be_replaced=1
        for i in range(len(nums)):
            if nums[index_to_be_replaced-1] != nums[i]:
                nums[index_to_be_replaced] = nums[i]
                index_to_be_replaced+=1

        nums[:] = nums[:index_to_be_replaced]
        return index_to_be_replaced