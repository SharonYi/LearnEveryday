#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeetCode 第1题：两数之和
题目链接：https://leetcode.cn/problems/two-sum/
难度：简单
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        方法一：暴力枚举
        时间复杂度：O(n²)，其中 n 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
        空间复杂度：O(1)。
        
        思路：
        遍历数组中的每个元素 x，然后查找数组中是否存在另一个元素 target - x。
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        """
        方法二：哈希表（推荐）
        时间复杂度：O(n)，其中 n 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
        空间复杂度：O(n)，其中 n 是数组中的元素数量。主要为哈希表的开销。
        
        思路：
        使用哈希表来存储已经遍历过的元素及其下标，这样可以在 O(1) 的时间复杂度内查找目标元素。
        
        步骤：
        1. 创建一个哈希表，用于存储元素值到下标的映射
        2. 遍历数组，对于每个元素 nums[i]：
           - 计算需要查找的目标值 complement = target - nums[i]
           - 检查哈希表中是否存在 complement
           - 如果存在，直接返回 [哈希表[complement], i]
           - 如果不存在，将 nums[i] 和其下标 i 存入哈希表
        3. 遍历结束后如果没有找到，返回空数组
        """
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []


def test_two_sum():
    """测试两数之和的各种情况"""
    
    solution = Solution()
    
    # 测试用例1：普通情况
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    result1_hash = solution.twoSum_hash(nums1, target1)
    print(f"测试用例1：nums={nums1}, target={target1}")
    print(f"  暴力解法结果：{result1}")
    print(f"  哈希表解法结果：{result1_hash}")
    print(f"  预期结果：[0, 1]")
    print()
    
    # 测试用例2：相同元素
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    result2_hash = solution.twoSum_hash(nums2, target2)
    print(f"测试用例2：nums={nums2}, target={target2}")
    print(f"  暴力解法结果：{result2}")
    print(f"  哈希表解法结果：{result2_hash}")
    print(f"  预期结果：[1, 2]")
    print()
    
    # 测试用例3：重复元素
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    result3_hash = solution.twoSum_hash(nums3, target3)
    print(f"测试用例3：nums={nums3}, target={target3}")
    print(f"  暴力解法结果：{result3}")
    print(f"  哈希表解法结果：{result3_hash}")
    print(f"  预期结果：[0, 1]")
    print()
    
    # 测试用例4：负数
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = solution.twoSum(nums4, target4)
    result4_hash = solution.twoSum_hash(nums4, target4)
    print(f"测试用例4：nums={nums4}, target={target4}")
    print(f"  暴力解法结果：{result4}")
    print(f"  哈希表解法结果：{result4_hash}")
    print(f"  预期结果：[2, 4]")
    print()
    
    # 测试用例5：混合正负
    nums5 = [1, -2, 3, -4, 5, -6, 7, -8]
    target5 = -1
    result5 = solution.twoSum(nums5, target5)
    result5_hash = solution.twoSum_hash(nums5, target5)
    print(f"测试用例5：nums={nums5}, target={target5}")
    print(f"  暴力解法结果：{result5}")
    print(f"  哈希表解法结果：{result5_hash}")
    print(f"  预期结果：[0, 1] 或 [2, 3] 等")
    print()


if __name__ == "__main__":
    test_two_sum()
