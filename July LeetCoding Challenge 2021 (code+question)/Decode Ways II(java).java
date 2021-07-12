/*
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*"
*/

class Solution
{
public
    static int numDecodings(String s)
    {
        long[] res = new long[2];
        res[0] = ways(s.charAt(0));
        if (s.length() < 2)
            return (int)res[0];

        res[1] = res[0] * ways(s.charAt(1)) + ways(s.charAt(0), s.charAt(1));
        for (int j = 2; j < s.length(); j++)
        {
            long temp = res[1];
            res[1] = (res[1] * ways(s.charAt(j)) + res[0] * ways(s.charAt(j - 1), s.charAt(j))) % 1000000007;
            res[0] = temp;
        }
        return (int)res[1];
    }

private
    static int ways(int ch)
    {
        if (ch == '*')
            return 9;
        if (ch == '0')
            return 0;
        return 1;
    }

private
    static int ways(char ch1, char ch2)
    {
        String str = "" + ch1 + "" + ch2;
        if (ch1 != '*' && ch2 != '*')
        {
            if (Integer.parseInt(str) >= 10 && Integer.parseInt(str) <= 26)
                return 1;
        }
        else if (ch1 == '*' && ch2 == '*')
        {
            return 15;
        }
        else if (ch1 == '*')
        {
            if (Integer.parseInt("" + ch2) >= 0 && Integer.parseInt("" + ch2) <= 6)
                return 2;
            else
                return 1;
        }
        else
        {
            if (Integer.parseInt("" + ch1) == 1)
            {
                return 9;
            }
            else if (Integer.parseInt("" + ch1) == 2)
            {
                return 6;
            }
        }
        return 0;
    }
}
