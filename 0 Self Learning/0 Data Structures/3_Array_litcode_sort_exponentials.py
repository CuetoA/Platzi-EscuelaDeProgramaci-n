nums = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

def sort_exponentials(nums):

    for i in range(0, len(nums) ):
        nums[i] = nums[i]**2
    
    nums.sort()
    return nums

if __name__=="__main__":
    print(sort_exponentials(nums))
    print(sort_exponentials(nums2))