def find_max_consecutive_ones(nums):

    counter = 0
    max_count = 0
    
    for num in nums:
        print(num)
        if num == 1:
            counter += 1
            print(counter)
            if counter >= max_count:
                max_count = counter
                print(max_count)
        else:
            counter = 0
            
    return max_count


nums = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]

find_max_consecutive_ones(nums) #?
