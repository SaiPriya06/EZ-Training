nums = [6, 8, 9, 5, 4, 3, 26, 2]
target_sum = 13
subsets = []
for i in range(2 ** len(nums)):
    subset = []
    for j in range(len(nums)):
        if (i >> j) & 1:
            
            subset.append(nums[j])

    if sum(subset) == target_sum:
        subsets.append(subset)

if subsets:
    for subset in subsets:
        print(subset)
else:
    print("No subsets found that sum up to the target.")