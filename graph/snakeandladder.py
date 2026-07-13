import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        visited = set()

        board.reverse()
        def address(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if not r % 2 == 0:
                c = n - 1 - c

            return r, c

        q = collections.deque([(1, 0)])
        while q:
            number, move = q.popleft()

            if number == n*n:
                return move

            for i in range(1,7):

                nxt = number + i
                if nxt > n * n:
                    continue
                r, c = address(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, move +1])
        return -1



        
        

