'''
You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:


Input: nums = [4,6,15,35]
Output: 4
Example 2:


Input: nums = [20,50,9,63]
Output: 2
Example 3:


Input: nums = [2,3,6,7,4,12,21,39]
Output: 8
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 105
All the values of nums are unique.
'''
class UnionFind: 
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        m = max(A)
        uf = UnionFind(m+1)
        seen = set(A)
        
        # modified sieve of eratosthenes 
        sieve = [1]*(m+1)
        sieve[0] = sieve[1] = 0 
        for k in range(m//2+1): 
            if sieve[k]: 
                ref = k if k in seen else 0
                for x in range(2*k, m+1, k): 
                    sieve[x] = 0
                    if x in seen: 
                        if ref: uf.union(ref, x)
                        ref = x
        
        freq = Counter(uf.find(i) for i in range(m+1))
        return max(freq.values())