import collections
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
       
        bank = set(bank)
        queue = collections.deque([(startGene, 0)])
        visited = set()

        genes = ['A', 'C', 'G', 'T']

        while queue:
            node, steps = queue.popleft()

            if node == endGene:
                return steps

            for i in range(len(node)):
                for g in genes:
                    new = node[:i] + g + node[i+1:]

                    if new in bank and new not in visited:
                        visited.add(new)
                        queue.append((new, steps + 1))

        return -1