'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        marked = [False] * 256
        map = [-1] * 256
        for i in range(n):
            if map[ord(s[i])] == -1:
                if marked[ord(t[i])]:
                    return False
                marked[ord(t[i])] = True
                map[ord(s[i])] = t[i]
            elif map[ord(s[i])] != t[i]:
                return False

        return True
