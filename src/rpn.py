from collections import deque

def eval_rpn(tokens):
    """
    Evaluates an expression in Reverse Polish Notation (RPN).

    Args:
        tokens: A list of strings representing the RPN expression.
                Numbers are represented as strings, and operators are
                represented as '+', '-', '*', or '/'.

    Returns:
        The integer result of the evaluation.
    """
    stack = deque()

    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            # If the token is a number (including negative numbers),
            # push it onto the stack.
            stack.append(int(token))
        else:
            # If the token is an operator, pop the top two operands,
            # perform the operation, and push the result back onto the stack.
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
               
                stack.append(int(operand1 / operand2))

    return stack.pop()