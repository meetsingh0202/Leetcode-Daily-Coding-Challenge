class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        def dfs(i, remain, shelf_height):
            nonlocal n
            if remain < 0:
                return float('inf') 

            if i >= n:
                return shelf_height

            if (i, remain, shelf_height) in memo:
                return memo[(i, remain, shelf_height)]

            width, height = books[i]

            same_shelf = float('inf')
            if width <= remain:
                new_height = max(shelf_height, height)
                new_remain = remain - width
                same_shelf = dfs(i + 1, new_remain, new_height)

            new_remain = shelfWidth - width
            change_shelf = shelf_height + dfs(i + 1, new_remain, height)

            memo[(i, remain, shelf_height)] = min(same_shelf, change_shelf)

            return memo[(i, remain, shelf_height)]

        n = len(books)

        memo = dict()

        return dfs(0, shelfWidth, 0)
