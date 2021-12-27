class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        """
        Solution 1:
        check the lenth of set and the len of nums are equal or Note
        Faster: 11% only

        Solution2:
        Store element in the dict and use the get method to check if element already exist or note.

        """

        count_dict = dict()

        for i in nums:
            return_value = count_dict.get(i, "NA")
            if str(return_value) != "NA":
                return True
            else:
                count_dict[i] = 1
        return False