# conversion of infix to postfix expression using stacks in python


def infix_to_postfix(infix_expression):
    def precedence(operator):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)
    def is_operator(char):
        operators = set(['+', '-', '*', '/', '^'])
        return char in operators
    stack = []
    postfix = []
    for char in infix_expression:
        if char.isalnum():
            # If the character is an operand, add it to the postfix expression
            postfix.append(char)
        elif char == '(':
            # If the character is an opening parenthesis, push it onto the stack
            stack.append(char)
        elif char == ')':
            # If the character is a closing parenthesis, pop operators from the stack and add to postfix until an opening parenthesis is encountered
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  
        elif is_operator(char):
            # If the character is an operator, pop operators from the stack and add to postfix until a lower precedence operator is encountered or the stack is empty
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())
    postfix_expression = ''.join(postfix)
    return postfix_expression

infix_expression = input("Enter an infix expression : ")
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
