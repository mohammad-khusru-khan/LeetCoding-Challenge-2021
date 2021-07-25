/*
Given a positive integer n, return the number of the integers in the range [0, n] 
whose binary representations do not contain consecutive ones.

Example 1:
Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 

Example 2:
Input: n = 1
Output: 2

Example 3:
Input: n = 2
Output: 3
 
Constraints:
1 <= n <= 109
*/

class Solution
{
public:
    int findIntegers(int n)
    {
        string t = "";
        while (n > 0)
        {
            t += (n & 1) == 1 ? "1" : "0";
            n = n >> 1;
        }

        vector<int> zero(t.length(), 0), one(t.length(), 0);
        zero[0] = one[0] = 1;
        for (int i = 1; i < t.length(); i++)
        {
            zero[i] = zero[i - 1] + one[i - 1];
            one[i] = zero[i - 1];
        }

        int res = zero[t.length() - 1] + one[t.length() - 1];
        for (int i = t.length() - 2; i >= 0; i--)
        {
            if (t[i] == '1' && t[i + 1] == '1')
                break;
            if (t[i] == '0' && t[i + 1] == '0')
                res -= one[i];
        }
        return res;
    }
};