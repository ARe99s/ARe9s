from typing import List


def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    k = 0  # 存最大的 不一样的数据的Index
    for i in range(1, n):  #从第二位开始看
        if nums[i] != nums[k]:  # 相等的话不用看。不相等把K+1
            k += 1
            nums[k] = nums[i] # 把当前不一样的数字存到k的位置
    return k + 1

if __name__ == '__main__':
    nums = [2,2,3,6,6,6,7]
    removeDuplicates(nums)