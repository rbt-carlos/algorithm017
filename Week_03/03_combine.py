class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]  # 列出所有n个数
        res = []

        def backTrace(sub_nums, cur_res, j):
            # 递归终止条件：
            if len(cur_res) == k:
                res.append(cur_res[:])  # 浅拷贝（先记住）
                return
            # 当前层的处理程序：
            for i in range(j, n):
                cur_res.append(nums[i])
                # 下探到下一层：
                backTrace(sub_nums[j:], cur_res, i + 1)
                cur_res.pop()
        # 特殊情况判断：
        if n == 0 or k == 0:
            return res
        backTrace(nums, [], 0)
        return res
