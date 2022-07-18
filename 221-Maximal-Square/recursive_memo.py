class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        
        
        def helper(r, c, maximum):
            if r >= ROWS or c >= COLS:
                return (maximum, 0)
            
            if (r, c) not in cache:
                down = helper(r + 1, c, maximum)
                right = helper(r, c + 1, maximum)
                diag = helper(r + 1, c + 1, maximum)
                
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down[1], right[1], diag[1])
                maximum = max(maximum, down[0], right[0], diag[0], cache[(r, c)])
                    
            return maximum, cache[(r, c)]
        
        mx = helper(0,0,0)[0]
        return mx**2
