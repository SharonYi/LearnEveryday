#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeetCode 70. 爬楼梯 (Climbing Stairs)
Python 实现

题目描述：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？

示例：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶：
1. 1 步 + 1 步
2. 2 步

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶：
1. 1 步 + 1 步 + 1 步
2. 1 步 + 2 步
3. 2 步 + 1 步

约束条件：
1 <= n <= 45
"""


class Solution:
    """
    爬楼梯问题的解决方案
    """

    def climbStairs_recursive(self, n: int) -> int:
        """
        方法一：递归（最直观但效率最低）
        
        思路：
        根据递推关系式 f(n) = f(n-1) + f(n-2) 直接递归
        
        时间复杂度：O(2^n) - 指数级，存在大量重复计算
        空间复杂度：O(n) - 递归栈深度
        
        缺点：当 n 较大时（如 n=40），会严重超时
        
        Args:
            n: 楼梯阶数
            
        Returns:
            不同的爬楼方法数
        """
        # 递归终止条件
        if n <= 2:
            return n
        
        # 递推关系：f(n) = f(n-1) + f(n-2)
        return self.climbStairs_recursive(n - 1) + self.climbStairs_recursive(n - 2)

    def climbStairs_memoization(self, n: int) -> int:
        """
        方法二：记忆化递归（自顶向下 DP）
        
        思路：
        使用递归思路，但用一个数组保存中间结果，避免重复计算
        
        时间复杂度：O(n) - 每个值只计算一次
        空间复杂度：O(n) - 记忆化数组 + 递归栈
        
        思想：递归 + 记忆化 = 动态规划的雏形
        
        Args:
            n: 楼梯阶数
            
        Returns:
            不同的爬楼方法数
        """
        # 记忆化数组，用于存储已计算的结果
        memo = [0] * (n + 1)
        
        def dfs(k: int) -> int:
            """深度优先搜索（递归）"""
            # 递归终止条件
            if k <= 2:
                return k
            
            # 如果已经计算过，直接返回
            if memo[k] != 0:
                return memo[k]
            
            # 计算并存储结果
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]
        
        return dfs(n)

    def climbStairs_dp(self, n: int) -> int:
        """
        方法三：动态规划（自底向上）【推荐学习】
        
        思路：
        从底向上计算，用数组存储中间结果
        
        状态定义：
        dp[i]：表示到达第 i 阶台阶的不同走法数量
        
        状态转移方程：
        dp[i] = dp[i-1] + dp[i-2]  (i >= 3)
        
        初始化：
        dp[1] = 1：到 1 阶只有一种方法（1 步）
        dp[2] = 2：到 2 阶有两种方法（1+1 或 2）
        
        时间复杂度：O(n) - 需要计算到第 n 项
        空间复杂度：O(n) - 需要存储整个 dp 数组
        
        Args:
            n: 楼梯阶数
            
        Returns:
            不同的爬楼方法数
        """
        # 基础情况处理
        if n <= 2:
            return n
        
        # 创建 dp 数组，dp[i] 表示到达第 i 阶的方法数
        dp = [0] * (n + 1)
        
        # 初始化边界条件
        dp[1] = 1  # 到第 1 阶只有 1 种方法
        dp[2] = 2  # 到第 2 阶有 2 种方法
        
        # 从第 3 阶开始递推
        for i in range(3, n + 1):
            # 状态转移方程：到达第 i 阶的方法数 = 到达 i-1 阶的方法数 + 到达 i-2 阶的方法数
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

    def climbStairs(self, n: int) -> int:
        """
        方法四：空间优化的动态规划（滚动数组）【最推荐】
        
        思路：
        观察递推公式 dp[i] = dp[i-1] + dp[i-2]，发现计算 dp[i] 只需要前两项的值。
        因此可以用两个变量滚动更新，而不需要整个数组。
        
        时间复杂度：O(n) - 需要循环 n-2 次
        空间复杂度：O(1) - 只使用常数个变量
        
        优点：高效简洁，面试中展示空间优化能力会加分
        
        Args:
            n: 楼梯阶数
            
        Returns:
            不同的爬楼方法数
        """
        # 基础情况处理
        if n <= 2:
            return n
        
        # prev 表示 dp[i-2]，curr 表示 dp[i-1]
        # 初始状态：dp[1] = 1, dp[2] = 2
        prev, curr = 1, 2
        
        # 从第 3 阶开始迭代
        for _ in range(3, n + 1):
            # 计算 dp[i] = dp[i-1] + dp[i-2]
            next_val = prev + curr
            
            # 滚动更新：prev 变为 curr，curr 变为 next_val
            prev, curr = curr, next_val
        
        return curr

    def climbStairs_math(self, n: int) -> int:
        """
        方法五：数学公式（闭式解法）【进阶】
        
        思路：
        斐波那契数列有通项公式：
        F(n) = (1/√5) × [((1+√5)/2)^(n+1) - ((1-√5)/2)^(n+1)]
        
        时间复杂度：O(1) - 直接计算
        空间复杂度：O(1) - 只使用常数个变量
        
        缺点：浮点数运算存在微小误差，但在 n ≤ 45 时完全安全
        
        Args:
            n: 楼梯阶数
            
        Returns:
            不同的爬楼方法数
        """
        import math
        
        sqrt5 = math.sqrt(5)
        # 斐波那契数列通项公式
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        
        # 四舍五入取整
        return int(round(fibn / sqrt5))


def test_solution():
    """
    测试用例
    """
    solution = Solution()
    
    # 测试用例列表
    test_cases = [
        (1, 1),   # 边界情况：n=1
        (2, 2),   # 边界情况：n=2
        (3, 3),   # 常规情况：n=3
        (4, 5),   # 常规情况：n=4
        (5, 8),   # 常规情况：n=5
        (10, 89), # 中等情况：n=10
        (20, 10946), # 较大情况：n=20
        (45, 1836311903), # 最大约束：n=45
    ]
    
    print("=" * 60)
    print("开始测试爬楼梯问题的所有解法")
    print("=" * 60)
    
    # 测试方法四：空间优化的动态规划（最推荐）
    print("\n【方法四：空间优化的动态规划（推荐）】")
    for n, expected in test_cases:
        result = solution.climbStairs(n)
        status = "✅ 通过" if result == expected else "❌ 失败"
        print(f"  n={n:2d}: 期望={expected:12d}, 实际={result:12d} {status}")
    
    # 测试方法三：动态规划数组
    print("\n【方法三：动态规划数组】")
    for n, expected in test_cases:
        result = solution.climbStairs_dp(n)
        status = "✅ 通过" if result == expected else "❌ 失败"
        print(f"  n={n:2d}: 期望={expected:12d}, 实际={result:12d} {status}")
    
    # 测试方法二：记忆化递归
    print("\n【方法二：记忆化递归】")
    for n, expected in test_cases[:-2]:  # 测试前6个用例，避免太大
        result = solution.climbStairs_memoization(n)
        status = "✅ 通过" if result == expected else "❌ 失败"
        print(f"  n={n:2d}: 期望={expected:12d}, 实际={result:12d} {status}")
    
    # 测试方法一：递归（只测试小 n）
    print("\n【方法一：递归（仅小 n 测试）】")
    for n, expected in test_cases[:5]:  # 只测试前5个用例
        result = solution.climbStairs_recursive(n)
        status = "✅ 通过" if result == expected else "❌ 失败"
        print(f"  n={n:2d}: 期望={expected:12d}, 实际={result:12d} {status}")
    
    # 测试方法五：数学公式
    print("\n【方法五：数学公式】")
    for n, expected in test_cases:
        result = solution.climbStairs_math(n)
        status = "✅ 通过" if result == expected else "❌ 失败"
        print(f"  n={n:2d}: 期望={expected:12d}, 实际={result:12d} {status}")
    
    print("\n" + "=" * 60)
    print("所有测试用例测试完成！")
    print("=" * 60)


def demonstrate_dp_process(n: int = 5):
    """
    演示动态规划的计算过程
    
    Args:
        n: 楼梯阶数
    """
    print(f"\n{'='*60}")
    print(f"动态规划过程演示（n = {n}）")
    print(f"{'='*60}")
    
    if n <= 2:
        print(f"\nn = {n} 时，直接返回 {n}")
        return
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    print(f"\n初始状态：")
    print(f"  dp[1] = {dp[1]} (到第 1 阶：1 步)")
    print(f"  dp[2] = {dp[2]} (到第 2 阶：1+1 或 2)")
    
    print(f"\n递推过程：")
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        print(f"  dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    
    print(f"\n最终结果：")
    print(f"  到第 {n} 阶共有 {dp[n]} 种方法")
    
    # 可视化展示所有方法（n <= 5 时）
    if n <= 5:
        print(f"\n所有可能的爬法：")
        all_methods = generate_all_methods(n)
        for i, method in enumerate(all_methods, 1):
            print(f"  方法 {i}: {' + '.join(map(str, method))}")


def generate_all_methods(n: int) -> list:
    """
    生成所有可能的爬楼方法（用于演示）
    
    Args:
        n: 楼梯阶数
        
    Returns:
        所有爬法的列表，每种爬法是一个步数列表
    """
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1], [2]]
    
    methods = []
    # 最后一步走 1 阶
    for method in generate_all_methods(n - 1):
        methods.append(method + [1])
    # 最后一步走 2 阶
    for method in generate_all_methods(n - 2):
        methods.append(method + [2])
    
    return methods


def compare_methods(n: int = 30):
    """
    对比不同方法的性能
    
    Args:
        n: 测试的楼梯阶数
    """
    import time
    
    print(f"\n{'='*60}")
    print(f"不同解法性能对比（n = {n}）")
    print(f"{'='*60}")
    
    solution = Solution()
    
    methods = [
        ("方法一：递归", solution.climbStairs_recursive, True),  # 只在 n 较小时测试
        ("方法二：记忆化递归", solution.climbStairs_memoization, False),
        ("方法三：动态规划数组", solution.climbStairs_dp, False),
        ("方法四：空间优化", solution.climbStairs, False),
        ("方法五：数学公式", solution.climbStairs_math, False),
    ]
    
    print(f"\n{'方法名称':<25} {'结果':<15} {'耗时(μs)':<10}")
    print("-" * 50)
    
    for name, func, skip_large in methods:
        if skip_large and n > 30:
            print(f"{name:<25} {'(跳过，n太大)':<15} {'-':<10}")
            continue
        
        # 多次运行取平均
        iterations = 1000 if name != "方法一：递归" else 10
        
        start_time = time.perf_counter()
        for _ in range(iterations):
            result = func(n)
        end_time = time.perf_counter()
        
        avg_time_us = ((end_time - start_time) / iterations) * 1_000_000
        print(f"{name:<25} {result:<15} {avg_time_us:.2f}")


if __name__ == "__main__":
    # 运行测试用例
    test_solution()
    
    # 演示动态规划过程
    demonstrate_dp_process(n=5)
    
    # 性能对比
    compare_methods(n=30)
