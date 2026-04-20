# LeetCode Top 100 算法题学习

本仓库用于记录LeetCode Hot 100算法题的学习和解题过程。

## 进度统计

| 总题数 | 已完成 | 进行中 | 待开始 |
| :----: | :----: | :----: | :----: |
| 100 | 1 | 0 | 99 |

---

## 算法图示

### 第1题：两数之和

#### 方法一：暴力枚举

**思路：** 遍历数组中的每一对元素，检查它们的和是否等于目标值。

```
示例：nums = [2, 7, 11, 15], target = 9

第1轮：i=0 (值=2)
  j=1 (值=7): 2+7=9 ✓ 找到！
  返回 [0, 1]

过程图示：
索引:     0    1     2     3
数值:     2    7    11    15
         ↑    ↑
         i    j (i=0, j=1)
         2 + 7 = 9 = target ✓
```

**时间复杂度：** O(n²) - 需要检查所有可能的元素对
**空间复杂度：** O(1) - 只使用常量级别的额外空间

---

#### 方法二：哈希表（推荐）

**思路：** 使用哈希表存储已遍历元素及其下标，每次检查 `target - 当前值` 是否在哈希表中。

```
示例：nums = [2, 7, 11, 15], target = 9

初始状态：哈希表 = {}

第1轮：i=0, 值=2
  complement = 9 - 2 = 7
  7 不在哈希表中
  存入哈希表: {2: 0}
  哈希表: {2: 0}

第2轮：i=1, 值=7
  complement = 9 - 7 = 2
  2 在哈希表中！(哈希表[2] = 0)
  返回 [0, 1]

过程图示：
┌─────────────────────────────────────────┐
│  步骤1: i=0, 值=2, target=9             │
│  计算: complement = 9 - 2 = 7           │
│  检查: 7 是否在哈希表中？→ 否           │
│  存入: 哈希表[2] = 0                     │
│  哈希表: {2: 0}                          │
├─────────────────────────────────────────┤
│  步骤2: i=1, 值=7, target=9             │
│  计算: complement = 9 - 7 = 2           │
│  检查: 2 是否在哈希表中？→ 是！         │
│  哈希表[2] = 0                           │
│  返回: [0, 1] ✓                          │
└─────────────────────────────────────────┘
```

**时间复杂度：** O(n) - 只需遍历数组一次，哈希表查找为O(1)
**空间复杂度：** O(n) - 最坏情况下需要存储所有元素

---

#### 两种方法对比

| 特性 | 暴力枚举 | 哈希表法 |
| :--- | :------: | :------: |
| 时间复杂度 | O(n²) | O(n) |
| 空间复杂度 | O(1) | O(n) |
| 适用场景 | 小规模数据 | 大规模数据 |
| 推荐指数 | ⭐⭐ | ⭐⭐⭐⭐⭐ |

**核心思想：** 哈希表法是典型的**空间换时间**策略，通过牺牲一些空间来大幅降低时间复杂度。

---

## 题目列表

### 哈希表
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 1 | [两数之和](https://leetcode.cn/problems/two-sum/) | 简单 | [题解](./solutions/001-two-sum.md) | ✅ 已完成 |
| 49 | [字母异位词分组](https://leetcode.cn/problems/group-anagrams/) | 中等 |  | ⏳ 待开始 |
| 128 | [最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/) | 中等 |  | ⏳ 待开始 |

### 双指针
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 283 | [移动零](https://leetcode.cn/problems/move-zeroes/) | 简单 |  | ⏳ 待开始 |
| 11 | [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) | 中等 |  | ⏳ 待开始 |
| 15 | [三数之和](https://leetcode.cn/problems/3sum/) | 中等 |  | ⏳ 待开始 |
| 42 | [接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 困难 |  | ⏳ 待开始 |

### 滑动窗口
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 3 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 中等 |  | ⏳ 待开始 |
| 438 | [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | 中等 |  | ⏳ 待开始 |
| 76 | [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) | 困难 |  | ⏳ 待开始 |

### 子串
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 560 | [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) | 中等 |  | ⏳ 待开始 |
| 239 | [滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/) | 困难 |  | ⏳ 待开始 |
| 76 | [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) | 困难 |  | ⏳ 待开始 |

### 数组
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 53 | [最大子数组和](https://leetcode.cn/problems/maximum-subarray/) | 中等 |  | ⏳ 待开始 |
| 56 | [合并区间](https://leetcode.cn/problems/merge-intervals/) | 中等 |  | ⏳ 待开始 |
| 189 | [轮转数组](https://leetcode.cn/problems/rotate-array/) | 中等 |  | ⏳ 待开始 |
| 238 | [除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/) | 中等 |  | ⏳ 待开始 |
| 41 | [缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/) | 困难 |  | ⏳ 待开始 |

### 矩阵
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 73 | [矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/) | 中等 |  | ⏳ 待开始 |
| 54 | [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) | 中等 |  | ⏳ 待开始 |
| 48 | [旋转图像](https://leetcode.cn/problems/rotate-image/) | 中等 |  | ⏳ 待开始 |
| 240 | [搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/) | 中等 |  | ⏳ 待开始 |

### 链表
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 160 | [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/) | 简单 |  | ⏳ 待开始 |
| 206 | [反转链表](https://leetcode.cn/problems/reverse-linked-list/) | 简单 |  | ⏳ 待开始 |
| 234 | [回文链表](https://leetcode.cn/problems/palindrome-linked-list/) | 简单 |  | ⏳ 待开始 |
| 141 | [环形链表](https://leetcode.cn/problems/linked-list-cycle/) | 简单 |  | ⏳ 待开始 |
| 21 | [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) | 简单 |  | ⏳ 待开始 |
| 2 | [两数相加](https://leetcode.cn/problems/add-two-numbers/) | 中等 |  | ⏳ 待开始 |
| 19 | [删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) | 中等 |  | ⏳ 待开始 |
| 24 | [两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) | 中等 |  | ⏳ 待开始 |
| 142 | [环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/) | 中等 |  | ⏳ 待开始 |
| 148 | [排序链表](https://leetcode.cn/problems/sort-list/) | 中等 |  | ⏳ 待开始 |
| 25 | [K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/) | 困难 |  | ⏳ 待开始 |

### 哈希表
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 128 | [最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/) | 中等 |  | ⏳ 待开始 |

### 栈
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 20 | [有效的括号](https://leetcode.cn/problems/valid-parentheses/) | 简单 |  | ⏳ 待开始 |
| 155 | [最小栈](https://leetcode.cn/problems/min-stack/) | 中等 |  | ⏳ 待开始 |
| 394 | [字符串解码](https://leetcode.cn/problems/decode-string/) | 中等 |  | ⏳ 待开始 |
| 739 | [每日温度](https://leetcode.cn/problems/daily-temperatures/) | 中等 |  | ⏳ 待开始 |
| 84 | [柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/) | 困难 |  | ⏳ 待开始 |

### 队列
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 239 | [滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/) | 困难 |  | ⏳ 待开始 |

### 二叉树
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 94 | [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | 简单 |  | ⏳ 待开始 |
| 101 | [对称二叉树](https://leetcode.cn/problems/symmetric-tree/) | 简单 |  | ⏳ 待开始 |
| 104 | [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | 简单 |  | ⏳ 待开始 |
| 226 | [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) | 简单 |  | ⏳ 待开始 |
| 543 | [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/) | 简单 |  | ⏳ 待开始 |
| 108 | [将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) | 简单 |  | ⏳ 待开始 |
| 98 | [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/) | 中等 |  | ⏳ 待开始 |
| 102 | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 中等 |  | ⏳ 待开始 |
| 114 | [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) | 中等 |  | ⏳ 待开始 |
| 105 | [从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 中等 |  | ⏳ 待开始 |
| 230 | [二叉搜索树中第K小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) | 中等 |  | ⏳ 待开始 |
| 199 | [二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/) | 中等 |  | ⏳ 待开始 |
| 110 | [平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/) | 简单 |  | ⏳ 待开始 |
| 222 | [完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/) | 中等 |  | ⏳ 待开始 |
| 236 | [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | 中等 |  | ⏳ 待开始 |
| 124 | [二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) | 困难 |  | ⏳ 待开始 |

### 二叉树遍历
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 144 | [二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/) | 简单 |  | ⏳ 待开始 |
| 145 | [二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/) | 简单 |  | ⏳ 待开始 |

### 图论
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 200 | [岛屿数量](https://leetcode.cn/problems/number-of-islands/) | 中等 |  | ⏳ 待开始 |
| 994 | [腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/) | 中等 |  | ⏳ 待开始 |
| 207 | [课程表](https://leetcode.cn/problems/course-schedule/) | 中等 |  | ⏳ 待开始 |
| 210 | [课程表 II](https://leetcode.cn/problems/course-schedule-ii/) | 中等 |  | ⏳ 待开始 |
| 695 | [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 中等 |  | ⏳ 待开始 |
| 130 | [被围绕的区域](https://leetcode.cn/problems/surrounded-regions/) | 中等 |  | ⏳ 待开始 |
| 133 | [克隆图](https://leetcode.cn/problems/clone-graph/) | 中等 |  | ⏳ 待开始 |
| 417 | [太平洋大西洋水流问题](https://leetcode.cn/problems/pacific-atlantic-water-flow/) | 中等 |  | ⏳ 待开始 |
| 797 | [所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/) | 中等 |  | ⏳ 待开始 |

### 回溯
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 46 | [全排列](https://leetcode.cn/problems/permutations/) | 中等 |  | ⏳ 待开始 |
| 78 | [子集](https://leetcode.cn/problems/subsets/) | 中等 |  | ⏳ 待开始 |
| 17 | [电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) | 中等 |  | ⏳ 待开始 |
| 39 | [组合总和](https://leetcode.cn/problems/combination-sum/) | 中等 |  | ⏳ 待开始 |
| 22 | [括号生成](https://leetcode.cn/problems/generate-parentheses/) | 中等 |  | ⏳ 待开始 |
| 79 | [单词搜索](https://leetcode.cn/problems/word-search/) | 中等 |  | ⏳ 待开始 |
| 51 | [N 皇后](https://leetcode.cn/problems/n-queens/) | 困难 |  | ⏳ 待开始 |

### 贪心
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 121 | [买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | 简单 |  | ⏳ 待开始 |
| 55 | [跳跃游戏](https://leetcode.cn/problems/jump-game/) | 中等 |  | ⏳ 待开始 |
| 45 | [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/) | 中等 |  | ⏳ 待开始 |
| 763 | [划分字母区间](https://leetcode.cn/problems/partition-labels/) | 中等 |  | ⏳ 待开始 |

### 动态规划
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 70 | [爬楼梯](https://leetcode.cn/problems/climbing-stairs/) | 简单 |  | ⏳ 待开始 |
| 118 | [杨辉三角](https://leetcode.cn/problems/pascals-triangle/) | 简单 |  | ⏳ 待开始 |
| 198 | [打家劫舍](https://leetcode.cn/problems/house-robber/) | 中等 |  | ⏳ 待开始 |
| 279 | [完全平方数](https://leetcode.cn/problems/perfect-squares/) | 中等 |  | ⏳ 待开始 |
| 322 | [零钱兑换](https://leetcode.cn/problems/coin-change/) | 中等 |  | ⏳ 待开始 |
| 139 | [单词拆分](https://leetcode.cn/problems/word-break/) | 中等 |  | ⏳ 待开始 |
| 300 | [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) | 中等 |  | ⏳ 待开始 |
| 152 | [乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/) | 中等 |  | ⏳ 待开始 |
| 416 | [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/) | 中等 |  | ⏳ 待开始 |
| 122 | [买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) | 中等 |  | ⏳ 待开始 |
| 55 | [跳跃游戏](https://leetcode.cn/problems/jump-game/) | 中等 |  | ⏳ 待开始 |
| 62 | [不同路径](https://leetcode.cn/problems/unique-paths/) | 中等 |  | ⏳ 待开始 |
| 64 | [最小路径和](https://leetcode.cn/problems/minimum-path-sum/) | 中等 |  | ⏳ 待开始 |
| 5 | [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/) | 中等 |  | ⏳ 待开始 |
| 1143 | [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) | 中等 |  | ⏳ 待开始 |
| 72 | [编辑距离](https://leetcode.cn/problems/edit-distance/) | 困难 |  | ⏳ 待开始 |
| 32 | [最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/) | 困难 |  | ⏳ 待开始 |
| 42 | [接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 困难 |  | ⏳ 待开始 |
| 85 | [最大矩形](https://leetcode.cn/problems/maximal-rectangle/) | 困难 |  | ⏳ 待开始 |
| 879 | [盈利计划](https://leetcode.cn/problems/profitable-schemes/) | 困难 |  | ⏳ 待开始 |
| 123 | [买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) | 困难 |  | ⏳ 待开始 |
| 188 | [买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) | 困难 |  | ⏳ 待开始 |
| 309 | [最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 中等 |  | ⏳ 待开始 |
| 714 | [买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | 中等 |  | ⏳ 待开始 |
| 10 | [正则表达式匹配](https://leetcode.cn/problems/regular-expression-matching/) | 困难 |  | ⏳ 待开始 |
| 44 | [通配符匹配](https://leetcode.cn/problems/wildcard-matching/) | 困难 |  | ⏳ 待开始 |

### 多维动态规划
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 62 | [不同路径](https://leetcode.cn/problems/unique-paths/) | 中等 |  | ⏳ 待开始 |
| 64 | [最小路径和](https://leetcode.cn/problems/minimum-path-sum/) | 中等 |  | ⏳ 待开始 |
| 5 | [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/) | 中等 |  | ⏳ 待开始 |
| 1143 | [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) | 中等 |  | ⏳ 待开始 |
| 72 | [编辑距离](https://leetcode.cn/problems/edit-distance/) | 困难 |  | ⏳ 待开始 |
| 32 | [最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/) | 困难 |  | ⏳ 待开始 |
| 42 | [接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 困难 |  | ⏳ 待开始 |
| 85 | [最大矩形](https://leetcode.cn/problems/maximal-rectangle/) | 困难 |  | ⏳ 待开始 |
| 879 | [盈利计划](https://leetcode.cn/problems/profitable-schemes/) | 困难 |  | ⏳ 待开始 |

### 技巧
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 136 | [只出现一次的数字](https://leetcode.cn/problems/single-number/) | 简单 |  | ⏳ 待开始 |
| 169 | [多数元素](https://leetcode.cn/problems/majority-element/) | 简单 |  | ⏳ 待开始 |
| 75 | [颜色分类](https://leetcode.cn/problems/sort-colors/) | 中等 |  | ⏳ 待开始 |
| 31 | [下一个排列](https://leetcode.cn/problems/next-permutation/) | 中等 |  | ⏳ 待开始 |
| 287 | [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/) | 中等 |  | ⏳ 待开始 |

### 排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 912 | [排序数组](https://leetcode.cn/problems/sort-an-array/) | 中等 |  | ⏳ 待开始 |

### 分治
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 108 | [将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) | 简单 |  | ⏳ 待开始 |
| 53 | [最大子数组和](https://leetcode.cn/problems/maximum-subarray/) | 中等 |  | ⏳ 待开始 |

### 字典树
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 208 | [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/) | 中等 |  | ⏳ 待开始 |

### 并查集
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 200 | [岛屿数量](https://leetcode.cn/problems/number-of-islands/) | 中等 |  | ⏳ 待开始 |
| 695 | [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 中等 |  | ⏳ 待开始 |
| 547 | [省份数量](https://leetcode.cn/problems/number-of-provinces/) | 中等 |  | ⏳ 待开始 |
| 130 | [被围绕的区域](https://leetcode.cn/problems/surrounded-regions/) | 中等 |  | ⏳ 待开始 |

### 前缀树
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 208 | [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/) | 中等 |  | ⏳ 待开始 |

### 线段树
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 307 | [区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable/) | 中等 |  | ⏳ 待开始 |

### 二分查找
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 35 | [搜索插入位置](https://leetcode.cn/problems/search-insert-position/) | 简单 |  | ⏳ 待开始 |
| 74 | [搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/) | 中等 |  | ⏳ 待开始 |
| 34 | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) | 中等 |  | ⏳ 待开始 |
| 33 | [搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/) | 中等 |  | ⏳ 待开始 |
| 153 | [寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) | 中等 |  | ⏳ 待开始 |
| 4 | [寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/) | 困难 |  | ⏳ 待开始 |

### 位运算
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 136 | [只出现一次的数字](https://leetcode.cn/problems/single-number/) | 简单 |  | ⏳ 待开始 |
| 191 | [位1的个数](https://leetcode.cn/problems/number-of-1-bits/) | 简单 |  | ⏳ 待开始 |
| 190 | [颠倒二进制位](https://leetcode.cn/problems/reverse-bits/) | 简单 |  | ⏳ 待开始 |
| 137 | [只出现一次的数字 II](https://leetcode.cn/problems/single-number-ii/) | 中等 |  | ⏳ 待开始 |
| 260 | [只出现一次的数字 III](https://leetcode.cn/problems/single-number-iii/) | 中等 |  | ⏳ 待开始 |
| 201 | [数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/) | 中等 |  | ⏳ 待开始 |

### 数学
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 9 | [回文数](https://leetcode.cn/problems/palindrome-number/) | 简单 |  | ⏳ 待开始 |
| 69 | [x 的平方根](https://leetcode.cn/problems/sqrtx/) | 简单 |  | ⏳ 待开始 |
| 202 | [快乐数](https://leetcode.cn/problems/happy-number/) | 简单 |  | ⏳ 待开始 |
| 172 | [阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/) | 中等 |  | ⏳ 待开始 |
| 50 | [Pow(x, n)](https://leetcode.cn/problems/powx-n/) | 中等 |  | ⏳ 待开始 |
| 67 | [二进制求和](https://leetcode.cn/problems/add-binary/) | 简单 |  | ⏳ 待开始 |
| 415 | [字符串相加](https://leetcode.cn/problems/add-strings/) | 简单 |  | ⏳ 待开始 |
| 43 | [字符串相乘](https://leetcode.cn/problems/multiply-strings/) | 中等 |  | ⏳ 待开始 |

### 字符串
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 125 | [验证回文串](https://leetcode.cn/problems/valid-palindrome/) | 简单 |  | ⏳ 待开始 |
| 5 | [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/) | 中等 |  | ⏳ 待开始 |
| 647 | [回文子串](https://leetcode.cn/problems/palindromic-substrings/) | 中等 |  | ⏳ 待开始 |
| 415 | [字符串相加](https://leetcode.cn/problems/add-strings/) | 简单 |  | ⏳ 待开始 |
| 3 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 中等 |  | ⏳ 待开始 |
| 438 | [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | 中等 |  | ⏳ 待开始 |
| 76 | [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) | 困难 |  | ⏳ 待开始 |
| 560 | [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) | 中等 |  | ⏳ 待开始 |
| 239 | [滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/) | 困难 |  | ⏳ 待开始 |
| 49 | [字母异位词分组](https://leetcode.cn/problems/group-anagrams/) | 中等 |  | ⏳ 待开始 |
| 30 | [串联所有单词的子串](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/) | 困难 |  | ⏳ 待开始 |
| 76 | [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) | 困难 |  | ⏳ 待开始 |

### 模拟
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 415 | [字符串相加](https://leetcode.cn/problems/add-strings/) | 简单 |  | ⏳ 待开始 |
| 43 | [字符串相乘](https://leetcode.cn/problems/multiply-strings/) | 中等 |  | ⏳ 待开始 |
| 54 | [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) | 中等 |  | ⏳ 待开始 |
| 48 | [旋转图像](https://leetcode.cn/problems/rotate-image/) | 中等 |  | ⏳ 待开始 |
| 240 | [搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/) | 中等 |  | ⏳ 待开始 |
| 498 | [对角线遍历](https://leetcode.cn/problems/diagonal-traverse/) | 中等 |  | ⏳ 待开始 |
| 6 | [Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/) | 中等 |  | ⏳ 待开始 |

### 设计
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 146 | [LRU 缓存](https://leetcode.cn/problems/lru-cache/) | 中等 |  | ⏳ 待开始 |
| 155 | [最小栈](https://leetcode.cn/problems/min-stack/) | 中等 |  | ⏳ 待开始 |
| 208 | [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/) | 中等 |  | ⏳ 待开始 |
| 232 | [用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/) | 简单 |  | ⏳ 待开始 |
| 225 | [用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/) | 简单 |  | ⏳ 待开始 |
| 295 | [数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/) | 困难 |  | ⏳ 待开始 |
| 173 | [二叉搜索树迭代器](https://leetcode.cn/problems/binary-search-tree-iterator/) | 中等 |  | ⏳ 待开始 |
| 341 | [扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/) | 中等 |  | ⏳ 待开始 |
| 380 | [O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/) | 中等 |  | ⏳ 待开始 |
| 705 | [设计哈希集合](https://leetcode.cn/problems/design-hashset/) | 简单 |  | ⏳ 待开始 |
| 706 | [设计哈希映射](https://leetcode.cn/problems/design-hashmap/) | 简单 |  | ⏳ 待开始 |

### 快速选择
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 215 | [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | 中等 |  | ⏳ 待开始 |

### 桶排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 347 | [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) | 中等 |  | ⏳ 待开始 |

### 计数排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 912 | [排序数组](https://leetcode.cn/problems/sort-an-array/) | 中等 |  | ⏳ 待开始 |

### 基数排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 164 | [最大间距](https://leetcode.cn/problems/maximum-gap/) | 困难 |  | ⏳ 待开始 |

### 归并排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 148 | [排序链表](https://leetcode.cn/problems/sort-list/) | 中等 |  | ⏳ 待开始 |

### 快速排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 912 | [排序数组](https://leetcode.cn/problems/sort-an-array/) | 中等 |  | ⏳ 待开始 |

### 堆
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 215 | [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | 中等 |  | ⏳ 待开始 |
| 347 | [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) | 中等 |  | ⏳ 待开始 |
| 295 | [数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/) | 困难 |  | ⏳ 待开始 |

### 单调栈
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 739 | [每日温度](https://leetcode.cn/problems/daily-temperatures/) | 中等 |  | ⏳ 待开始 |
| 496 | [下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/) | 简单 |  | ⏳ 待开始 |
| 503 | [下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/) | 中等 |  | ⏳ 待开始 |
| 84 | [柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/) | 困难 |  | ⏳ 待开始 |
| 42 | [接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 困难 |  | ⏳ 待开始 |
| 85 | [最大矩形](https://leetcode.cn/problems/maximal-rectangle/) | 困难 |  | ⏳ 待开始 |
| 32 | [最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/) | 困难 |  | ⏳ 待开始 |
| 907 | [子数组的最小值之和](https://leetcode.cn/problems/sum-of-subarray-minimums/) | 中等 |  | ⏳ 待开始 |
| 2104 | [子数组范围和](https://leetcode.cn/problems/sum-of-subarray-ranges/) | 中等 |  | ⏳ 待开始 |

### 单调队列
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 239 | [滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/) | 困难 |  | ⏳ 待开始 |

### 区间
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 56 | [合并区间](https://leetcode.cn/problems/merge-intervals/) | 中等 |  | ⏳ 待开始 |
| 57 | [插入区间](https://leetcode.cn/problems/insert-interval/) | 中等 |  | ⏳ 待开始 |
| 435 | [无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/) | 中等 |  | ⏳ 待开始 |
| 452 | [用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) | 中等 |  | ⏳ 待开始 |
| 763 | [划分字母区间](https://leetcode.cn/problems/partition-labels/) | 中等 |  | ⏳ 待开始 |
| 649 | [Dota2 参议院](https://leetcode.cn/problems/dota2-senate/) | 中等 |  | ⏳ 待开始 |

### 状态压缩
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 464 | [我能赢吗](https://leetcode.cn/problems/can-i-win/) | 中等 |  | ⏳ 待开始 |
| 416 | [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/) | 中等 |  | ⏳ 待开始 |
| 698 | [划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/) | 中等 |  | ⏳ 待开始 |
| 2044 | [统计按位或能得到最大值的子集数目](https://leetcode.cn/problems/count-number-of-maximum-bitwise-or-subsets/) | 中等 |  | ⏳ 待开始 |
| 526 | [优美的排列](https://leetcode.cn/problems/beautiful-arrangement/) | 中等 |  | ⏳ 待开始 |
| 357 | [统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits/) | 中等 |  | ⏳ 待开始 |
| 935 | [骑士拨号器](https://leetcode.cn/problems/knight-dialer/) | 中等 |  | ⏳ 待开始 |
| 1349 | [参加考试的最大学生数](https://leetcode.cn/problems/maximum-students-taking-exam/) | 困难 |  | ⏳ 待开始 |

### 博弈
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 292 | [Nim 游戏](https://leetcode.cn/problems/nim-game/) | 简单 |  | ⏳ 待开始 |
| 1025 | [除数博弈](https://leetcode.cn/problems/divisor-game/) | 简单 |  | ⏳ 待开始 |
| 877 | [石子游戏](https://leetcode.cn/problems/stone-game/) | 中等 |  | ⏳ 待开始 |
| 486 | [预测赢家](https://leetcode.cn/problems/predict-the-winner/) | 中等 |  | ⏳ 待开始 |
| 464 | [我能赢吗](https://leetcode.cn/problems/can-i-win/) | 中等 |  | ⏳ 待开始 |
| 1025 | [除数博弈](https://leetcode.cn/problems/divisor-game/) | 简单 |  | ⏳ 待开始 |
| 292 | [Nim 游戏](https://leetcode.cn/problems/nim-game/) | 简单 |  | ⏳ 待开始 |

### 概率与统计
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 470 | [用 Rand7() 实现 Rand10()](https://leetcode.cn/problems/implement-rand10-using-rand7/) | 中等 |  | ⏳ 待开始 |
| 528 | [按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/) | 中等 |  | ⏳ 待开始 |
| 382 | [链表随机节点](https://leetcode.cn/problems/linked-list-random-node/) | 中等 |  | ⏳ 待开始 |
| 398 | [随机数索引](https://leetcode.cn/problems/random-pick-index/) | 中等 |  | ⏳ 待开始 |

### 采样
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 470 | [用 Rand7() 实现 Rand10()](https://leetcode.cn/problems/implement-rand10-using-rand7/) | 中等 |  | ⏳ 待开始 |
| 528 | [按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/) | 中等 |  | ⏳ 待开始 |
| 382 | [链表随机节点](https://leetcode.cn/problems/linked-list-random-node/) | 中等 |  | ⏳ 待开始 |
| 398 | [随机数索引](https://leetcode.cn/problems/random-pick-index/) | 中等 |  | ⏳ 待开始 |

### 扫描线
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 218 | [天际线问题](https://leetcode.cn/problems/the-skyline-problem/) | 困难 |  | ⏳ 待开始 |
| 850 | [矩形面积 II](https://leetcode.cn/problems/rectangle-area-ii/) | 困难 |  | ⏳ 待开始 |

### 欧拉路径/回路
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 332 | [重新安排行程](https://leetcode.cn/problems/reconstruct-itinerary/) | 困难 |  | ⏳ 待开始 |

### 拓扑排序
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 207 | [课程表](https://leetcode.cn/problems/course-schedule/) | 中等 |  | ⏳ 待开始 |
| 210 | [课程表 II](https://leetcode.cn/problems/course-schedule-ii/) | 中等 |  | ⏳ 待开始 |

### 多源BFS
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 542 | [01 矩阵](https://leetcode.cn/problems/01-matrix/) | 中等 |  | ⏳ 待开始 |
| 1162 | [地图分析](https://leetcode.cn/problems/as-far-from-land-as-possible/) | 中等 |  | ⏳ 待开始 |
| 286 | [墙与门](https://leetcode.cn/problems/walls-and-gates/) | 中等 |  | ⏳ 待开始 |
| 994 | [腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/) | 中等 |  | ⏳ 待开始 |
| 102 | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 中等 |  | ⏳ 待开始 |
| 103 | [二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) | 中等 |  | ⏳ 待开始 |
| 107 | [二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/) | 中等 |  | ⏳ 待开始 |
| 199 | [二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/) | 中等 |  | ⏳ 待开始 |
| 116 | [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/) | 中等 |  | ⏳ 待开始 |
| 117 | [填充每个节点的下一个右侧节点指针 II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) | 中等 |  | ⏳ 待开始 |
| 310 | [最小高度树](https://leetcode.cn/problems/minimum-height-trees/) | 中等 |  | ⏳ 待开始 |
| 200 | [岛屿数量](https://leetcode.cn/problems/number-of-islands/) | 中等 |  | ⏳ 待开始 |
| 695 | [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 中等 |  | ⏳ 待开始 |
| 547 | [省份数量](https://leetcode.cn/problems/number-of-provinces/) | 中等 |  | ⏳ 待开始 |
| 130 | [被围绕的区域](https://leetcode.cn/problems/surrounded-regions/) | 中等 |  | ⏳ 待开始 |
| 133 | [克隆图](https://leetcode.cn/problems/clone-graph/) | 中等 |  | ⏳ 待开始 |
| 417 | [太平洋大西洋水流问题](https://leetcode.cn/problems/pacific-atlantic-water-flow/) | 中等 |  | ⏳ 待开始 |
| 797 | [所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/) | 中等 |  | ⏳ 待开始 |
| 210 | [课程表 II](https://leetcode.cn/problems/course-schedule-ii/) | 中等 |  | ⏳ 待开始 |
| 207 | [课程表](https://leetcode.cn/problems/course-schedule/) | 中等 |  | ⏳ 待开始 |
| 399 | [除法求值](https://leetcode.cn/problems/evaluate-division/) | 中等 |  | ⏳ 待开始 |
| 990 | [等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/) | 中等 |  | ⏳ 待开始 |
| 1202 | [交换字符串中的元素](https://leetcode.cn/problems/smallest-string-with-swaps/) | 中等 |  | ⏳ 待开始 |
| 947 | [移除最多的同行或同列石头](https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/) | 中等 |  | ⏳ 待开始 |
| 839 | [相似字符串组](https://leetcode.cn/problems/similar-string-groups/) | 困难 |  | ⏳ 待开始 |
| 1631 | [最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/) | 中等 |  | ⏳ 待开始 |
| 778 | [水位上升的泳池中游泳](https://leetcode.cn/problems/swim-in-rising-water/) | 困难 |  | ⏳ 待开始 |
| 1584 | [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/) | 中等 |  | ⏳ 待开始 |
| 1135 | [最低成本联通所有城市](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/) | 中等 |  | ⏳ 待开始 |
| 743 | [网络延迟时间](https://leetcode.cn/problems/network-delay-time/) | 中等 |  | ⏳ 待开始 |
| 787 | [K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) | 中等 |  | ⏳ 待开始 |
| 787 | [K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) | 中等 |  | ⏳ 待开始 |
| 1631 | [最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/) | 中等 |  | ⏳ 待开始 |
| 778 | [水位上升的泳池中游泳](https://leetcode.cn/problems/swim-in-rising-water/) | 困难 |  | ⏳ 待开始 |
| 1584 | [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/) | 中等 |  | ⏳ 待开始 |
| 1135 | [最低成本联通所有城市](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/) | 中等 |  | ⏳ 待开始 |
| 743 | [网络延迟时间](https://leetcode.cn/problems/network-delay-time/) | 中等 |  | ⏳ 待开始 |
| 787 | [K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) | 中等 |  | ⏳ 待开始 |
| 1334 | [阈值距离内邻居最少的城市](https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 中等 |  | ⏳ 待开始 |
| 882 | [细分图中的可到达结点](https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/) | 困难 |  | ⏳ 待开始 |
| 1631 | [最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/) | 中等 |  | ⏳ 待开始 |
| 778 | [水位上升的泳池中游泳](https://leetcode.cn/problems/swim-in-rising-water/) | 困难 |  | ⏳ 待开始 |
| 1584 | [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/) | 中等 |  | ⏳ 待开始 |
| 1135 | [最低成本联通所有城市](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/) | 中等 |  | ⏳ 待开始 |
| 743 | [网络延迟时间](https://leetcode.cn/problems/network-delay-time/) | 中等 |  | ⏳ 待开始 |
| 787 | [K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) | 中等 |  | ⏳ 待开始 |
| 1334 | [阈值距离内邻居最少的城市](https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 中等 |  | ⏳ 待开始 |
| 882 | [细分图中的可到达结点](https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/) | 困难 |  | ⏳ 待开始 |

### 记忆化搜索
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 139 | [单词拆分](https://leetcode.cn/problems/word-break/) | 中等 |  | ⏳ 待开始 |
| 329 | [矩阵中的最长递增路径](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) | 困难 |  | ⏳ 待开始 |
| 472 | [连接词](https://leetcode.cn/problems/concatenated-words/) | 困难 |  | ⏳ 待开始 |
| 337 | [打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/) | 中等 |  | ⏳ 待开始 |
| 1143 | [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) | 中等 |  | ⏳ 待开始 |
| 516 | [最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/) | 中等 |  | ⏳ 待开始 |
| 1035 | [不相交的线](https://leetcode.cn/problems/uncrossed-lines/) | 中等 |  | ⏳ 待开始 |
| 712 | [两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/) | 中等 |  | ⏳ 待开始 |
| 300 | [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) | 中等 |  | ⏳ 待开始 |
| 673 | [最长递增子序列的个数](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/) | 中等 |  | ⏳ 待开始 |
| 646 | [最长数对链](https://leetcode.cn/problems/maximum-length-of-pair-chain/) | 中等 |  | ⏳ 待开始 |
| 1218 | [最长定差子序列](https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/) | 中等 |  | ⏳ 待开始 |
| 873 | [最长的斐波那契子序列的长度](https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/) | 中等 |  | ⏳ 待开始 |
| 1027 | [最长等差数列](https://leetcode.cn/problems/longest-arithmetic-subsequence/) | 中等 |  | ⏳ 待开始 |
| 446 | [等差数列划分 II - 子序列](https://leetcode.cn/problems/arithmetic-slices-ii-subsequence/) | 困难 |  | ⏳ 待开始 |
| 300 | [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) | 中等 |  | ⏳ 待开始 |
| 354 | [俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/) | 困难 |  | ⏳ 待开始 |
| 646 | [最长数对链](https://leetcode.cn/problems/maximum-length-of-pair-chain/) | 中等 |  | ⏳ 待开始 |
| 435 | [无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/) | 中等 |  | ⏳ 待开始 |
| 452 | [用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) | 中等 |  | ⏳ 待开始 |
| 1288 | [删除被覆盖区间](https://leetcode.cn/problems/remove-covered-intervals/) | 中等 |  | ⏳ 待开始 |
| 986 | [区间列表的交集](https://leetcode.cn/problems/interval-list-intersections/) | 中等 |  | ⏳ 待开始 |
| 763 | [划分字母区间](https://leetcode.cn/problems/partition-labels/) | 中等 |  | ⏳ 待开始 |
| 649 | [Dota2 参议院](https://leetcode.cn/problems/dota2-senate/) | 中等 |  | ⏳ 待开始 |

### 枚举
| 题号 | 题目 | 难度 | 题解 | 状态 |
| :--: | :--: | :--: | :--: | :--: |
| 93 | [复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/) | 中等 |  | ⏳ 待开始 |
| 78 | [子集](https://leetcode.cn/problems/subsets/) | 中等 |  | ⏳ 待开始 |
| 46 | [全排列](https://leetcode.cn/problems/permutations/) | 中等 |  | ⏳ 待开始 |
| 77 | [组合](https://leetcode.cn/problems/combinations/) | 中等 |  | ⏳ 待开始 |
| 39 | [组合总和](https://leetcode.cn/problems/combination-sum/) | 中等 |  | ⏳ 待开始 |
| 40 | [组合总和 II](https://leetcode.cn/problems/combination-sum-ii/) | 中等 |  | ⏳ 待开始 |
| 216 | [组合总和 III](https://leetcode.cn/problems/combination-sum-iii/) | 中等 |  | ⏳ 待开始 |
| 377 | [组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/) | 中等 |  | ⏳ 待开始 |
| 17 | [电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) | 中等 |  | ⏳ 待开始 |
| 22 | [括号生成](https://leetcode.cn/problems/generate-parentheses/) | 中等 |  | ⏳ 待开始 |
| 79 | [单词搜索](https://leetcode.cn/problems/word-search/) | 中等 |  | ⏳ 待开始 |
| 200 | [岛屿数量](https://leetcode.cn/problems/number-of-islands/) | 中等 |  | ⏳ 待开始 |
| 695 | [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 中等 |  | ⏳ 待开始 |
| 547 | [省份数量](https://leetcode.cn/problems/number-of-provinces/) | 中等 |  | ⏳ 待开始 |
| 130 | [被围绕的区域](https://leetcode.cn/problems/surrounded-regions/) | 中等 |  | ⏳ 待开始 |
| 133 | [克隆图](https://leetcode.cn/problems/clone-graph/) | 中等 |  | ⏳ 待开始 |
| 417 | [太平洋大西洋水流问题](https://leetcode.cn/problems/pacific-atlantic-water-flow/) | 中等 |  | ⏳ 待开始 |
| 797 | [所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/) | 中等 |  | ⏳ 待开始 |
| 210 | [课程表 II](https://leetcode.cn/problems/course-schedule-ii/) | 中等 |  | ⏳ 待开始 |
| 207 | [课程表](https://leetcode.cn/problems/course-schedule/) | 中等 |  | ⏳ 待开始 |
| 399 | [除法求值](https://leetcode.cn/problems/evaluate-division/) | 中等 |  | ⏳ 待开始 |
| 990 | [等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/) | 中等 |  | ⏳ 待开始 |
| 1202 | [交换字符串中的元素](https://leetcode.cn/problems/smallest-string-with-swaps/) | 中等 |  | ⏳ 待开始 |
| 947 | [移除最多的同行或同列石头](https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/) | 中等 |  | ⏳ 待开始 |
| 839 | [相似字符串组](https://leetcode.cn/problems/similar-string-groups/) | 困难 |  | ⏳ 待开始 |
| 1631 | [最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/) | 中等 |  | ⏳ 待开始 |
| 778 | [水位上升的泳池中游泳](https://leetcode.cn/problems/swim-in-rising-water/) | 困难 |  | ⏳ 待开始 |
| 1584 | [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/) | 中等 |  | ⏳ 待开始 |
| 1135 | [最低成本联通所有城市](https://leetcode.cn/problems/connecting-cities-with-minimum-cost/) | 中等 |  | ⏳ 待开始 |
| 743 | [网络延迟时间](https://leetcode.cn/problems/network-delay-time/) | 中等 |  | ⏳ 待开始 |
| 787 | [K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) | 中等 |  | ⏳ 待开始 |
| 1334 | [阈值距离内邻居最少的城市](https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 中等 |  | ⏳ 待开始 |
| 882 | [细分图中的可到达结点](https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/) | 困难 |  | ⏳ 待开始 |
| 1631 | [最小体力消耗路径](https://leet