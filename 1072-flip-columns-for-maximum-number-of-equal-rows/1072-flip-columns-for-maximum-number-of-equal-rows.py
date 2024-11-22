class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mp = {}

        for row in matrix:
            first = row[0]
            canonical = ""
            for i in row:
                canonical += '1' if i == first else '0'
            mp[canonical] = mp.get(canonical, 0) + 1

        return max(mp.values(), default=0)
