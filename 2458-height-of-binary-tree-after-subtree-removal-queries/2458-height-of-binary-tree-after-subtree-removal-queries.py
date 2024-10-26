class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = dict()
        heights = dict()
        levels = defaultdict(list)
        maxHeights = defaultdict(list)
        def traverse(curr, depth):
            if curr == None:
                return 0
            height = 1 + max(traverse(curr.right, depth + 1), traverse(curr.left, depth + 1))
            levels[depth].append(curr.val)
            heights[curr.val] = height
            depths[curr.val] = depth
            if depth in maxHeights:
                if len(maxHeights[depth]) == 1:
                    maxHeights[depth].append([height, curr.val])
                else:
                    first, second = maxHeights[depth]
                    if height > first[0] and height <= second[0]:
                        maxHeights[depth] = [[height, curr.val], second]
                    elif height > second[0] and height <= first[0]:
                        maxHeights[depth] = [first, [height, curr.val]]
                    elif height > second[0] and height > first[0]:
                        if second[0] > first[0]:
                            maxHeights[depth] = [[height, curr.val], second]
                        else:
                            maxHeights[depth] = [first, [height, curr.val]]
            else:
                maxHeights[depth].append([height, curr.val])
            return height
        # @functools.cache
        def calculate(currRoot):
            MaxHeight = 0
            depthForCurrRoot = depths[currRoot]
            currMaxHeights = maxHeights[depthForCurrRoot]
            for i in currMaxHeights:
                if i[1] != currRoot:
                    MaxHeight = max(MaxHeight, i[0])
            return depthForCurrRoot + MaxHeight - 1
        traverse(root, 0)
        res = []
        for i in queries:
            res.append(calculate(i))
        return res        