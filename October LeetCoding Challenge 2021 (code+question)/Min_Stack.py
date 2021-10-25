'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''
class MinStack:

    def __init__(self):
        self._stack = []
        self._min = None

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append(val)
            self._min = val
        elif val>=self._min:
            self._stack.append(val)
        else:
            self._stack.append(2*val-self._min)
            self._min = val     

    def pop(self) -> None:
        el = self._stack.pop()
        if el<self._min:
            el, self._min = self._min, 2*self._min-el
        return el

    def top(self) -> int:
        return max(self._stack[-1], self._min)

    def getMin(self) -> int:
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()