def sum_target(nums_list, target_value):
    for i in range(len(nums_list)):
        for j in range(i+1, len(nums_list)):
            if target_value - nums_list[i] == nums_list[j]:
                return[i, j]
            return []


nums = [1, 5, 7, 3]
target = 6
print(sum_target(nums, target))

nums = [1, 3, 4]
target = 4
print(sum_target(nums, target))

