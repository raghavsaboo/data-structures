from stacks.stack import Stack
from array import array

"""
Problem Statement
-----------------
Implement the following functions to implement two stacks using a
single array such that for storing elements both stacks should use
the same array. An illustration is also provided for your
understanding. Also, for this problem, use Python arrays and not
lists!

# Function Prototypes

def push1(value): # pushes value in stack 1
def push2(value): # pushes value in stack 2
def pop1(): # pops an element from stack 1
def pop2():# pops an element from stack 2

# Input/Output
>> push1(value)
>> Input: an integer
>> Output: inserts the given value in the first stack, i.e., stack1

>> push2(value)
>> Input: an integer
>> Output: inserts the given value in the second stack i.e stack2

>> pop1()
>> Output: returns and removes the top value of stack1

>> pop2()
>> Output: returns and removes the top value of stack2
"""


class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        """
        O(1) time complexity - indexing array
        Method to push an element x to stack1
        """

        if self.top1 < self.top2 - 1:
            # There is at least one empty space for new element
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow!")
            exit(1)

    def push2(self, x):
        """
        O(1) time complexity - indexing array
        Method to push an element x to stack2
        """

        if self.top1 < self.top2 - 1:
            # There is at least one empty space for new element
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow!")
            exit(1)

    def pop1(self):
        """
        O(1) time complexity - indexing array
        Method to pop an element from the end of stack1
        """
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow!")
            exit(1)

    def pop2(self):
        """
        O(1) time complexity - indexing array
        Method to pop an element from the end of stack2
        """
        if self.top2 <= self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow!")
            exit(1)


stack = TwoStacks(10)
stack.push1(20)
stack.push2(10)

print(stack.pop1())
stack.push1(100)



"""
Problem Statement 
-----------------

Implement a function called evaluate_postfix(exp) that will compute a postfix 
expression given to it as a string.

# Output
A result of the given postfix expression.

# Sample Input
>> exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4

# Sample Output
>> 3
"""

def evaluate_postfix(expression):
    """
    O(n) time complexity
    O(n) space complexity
    """
    s = Stack()
    
    try:
        for val in expression:
            if val.isdigit():
                s.push(val)
            else:
                b = s.pop()
                a = s.pop()
                result = str(eval(str(a) + str(val) + str(b)))
                s.push(result)
                
        return int(s.pop())
    except TypeError:
        return "Invalid Sequence"

print("Result: " + str(evaluate_postfix("921*-8-4+")))
print("Result: " + str(evaluate_postfix("921*-8--4+")))
