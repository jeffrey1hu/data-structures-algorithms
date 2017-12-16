# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self.stack[-1]

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = Stack()
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.push(Bracket(next, i+1))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if opening_brackets_stack.is_empty():
                print(i+1)
                exit()
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                print(i+1)
                exit()
    if not opening_brackets_stack.is_empty():
        print(opening_brackets_stack.stack[0].position)
        exit()
    print("Success")

    # Printing answer, write your code here
