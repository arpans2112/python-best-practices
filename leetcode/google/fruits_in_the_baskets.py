class Solution:

    def totalFruit(self, fruits: List[int]) -> int:

        def getTotalOfLastType(fruit_list, fruit_type):
            global start_index
            count = -1
            total = 0
            while abs(count) <= len(fruit_list):
                if fruit_list[count] == fruit_type:
                    total += 1
                    count -= 1
                else:
                    break
            start_index = len(fruit_list) + count
            return (total, start_index)

        """
        1. min_number_of_fruits = 1
        2. truits type : 0 < truits.length 
        3. need to pick maxium fruits: 
        4. Best Case: when there are type less than 2, then max fruit is equal to = length of array 
        5. what if there is no different type found, and array is ending
        Examples
        1. [1] - one element
        2. [1,2] - two element - two type
        3. [1, 2, 3] - more than two elements - distinct type
        4. [1, 2, 2] - more than two elements - only two type of elements
        5. [1, 2, 1] - more than two elements - distinct type elements
        5. [1, 2 , 1, 2, 3] - more than two elements - only two type of elements
        6. [1, 1 , 2 , 2, 3, 3, 2] 
        7. [1, 1 , 2 , 2, 3, 3, 3, 3] 
        8. [1, 1 , 2 , 2, 3, 3, 3, 3, 4] 
        9  [1,0,1]


        Solution:
        1. first_type
        2. second_type
        3. calculate sum
        4. set maxium
        4. first_type = second_type
        5. second_type = new_type
        6. calcualte sum
        7. check if sum > maxium or not and set new maxium
        8. Continue this process till the end of array
        """

        fruit_types = set(fruits)

        if (len(fruit_types) <= 2):
            return len(fruits)

        different_types = list()

        for fruit in fruits:
            if fruit not in different_types:
                different_types.append(fruit)
                if (len(different_types) == 2):
                    break

        first_type = different_types[0]
        second_type = different_types[1]

        total_count = 0;
        first_type_count = 0
        seoncd_type_count = 0
        max_fruit_count = 0
        diff_type_index = 2
        last_type = None
        start_index = 0
        for i, fruit in enumerate(fruits):
            if fruit in [first_type, second_type]:
                total_count += 1
            else:

                if total_count > max_fruit_count:
                    max_fruit_count = total_count

                total, start_index = getTotalOfLastType(fruits[start_index:i], last_type)
                total_count = total + 1
                first_type = last_type
                second_type = fruit
            last_type = fruit

        if total_count > max_fruit_count:
            max_fruit_count = total_count

        return max_fruit_count




