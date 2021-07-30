/*
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 
Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");// return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap"); // return 5 (apple + app = 3 + 2 = 5)
 

Constraints:
1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
*/

class MapSum
{

    /** Initialize your data structure here. */
public
    class Trie
    {
    public
        Trie[] nxt;
    public
        int cnt;
        Trie()
        {
            this.nxt = new Trie[26];
            this.cnt = 0;
        }
    } public Trie root;
public
    Map<String, Integer> mp;
public
    MapSum()
    {
        this.root = new Trie();
        this.mp = new HashMap<>();
    }

public
    void insert(String key, int val)
    {

        int pre = 0;
        if (this.mp.containsKey(key))
        {
            pre = this.mp.get(key);
        }
        this.mp.put(key, val);
        Trie p = this.root;
        for (int i = 0; i < key.length(); i++)
        {
            int idx = key.charAt(i) - 'a';
            if (p.nxt[idx] == null)
            {
                p.nxt[idx] = new Trie();
            }
            p = p.nxt[idx];
            p.cnt += val - pre;
        }
    }

public
    int sum(String prefix)
    {

        Trie p = this.root;
        for (int i = 0; i < prefix.length(); i++)
        {
            int idx = prefix.charAt(i) - 'a';
            if (p.nxt[idx] == null)
            {
                return 0;
            }
            p = p.nxt[idx];
        }
        return p.cnt;
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */