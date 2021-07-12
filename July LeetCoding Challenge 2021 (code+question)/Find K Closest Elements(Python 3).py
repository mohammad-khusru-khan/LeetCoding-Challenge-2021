'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def CrossoverPoint(arr, low, high, x):
            if arr[high] <= x:
                return high
            if arr[low] > x:
                return low
            mid = (low + high) // 2
            if arr[mid] <= x < arr[mid + 1]:
                return mid
            if arr[mid] < x:
                return CrossoverPoint(arr, mid + 1, high, x)
            return CrossoverPoint(arr, low, mid - 1, x)


        def findClosestElements(arr, k, x):
            ans = []
            n = len(arr)
            l = CrossoverPoint(arr, 0, n - 1, x)
            r = l + 1
            count = 0
            while l >= 0 and r < n and count < k:
                if x - arr[l] <= arr[r] - x:
                    ans.append(arr[l])
                    l -= 1
                else:
                    ans.append(arr[r])
                    r += 1
                count += 1
            while count < k and l >= 0:
                ans.append(arr[l])
                l -= 1
                count += 1
            while count < k and r < n:
                ans.append(arr[r])
                r += 1
                count += 1
            return ans
        ans = findClosestElements(arr, k, x)
        ans.sort()
        return ans
