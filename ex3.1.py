import sys

def evaluate(tokens):
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            sub_expr = []
            while stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()
            sub_expr.reverse()
            result = compute(sub_expr)
            stack.append(result)
        else:
            if token.isdigit():
                stack.append(int(token))
            else:
                stack.append(token)
    return stack.pop()

def compute(expr):
    op = expr.pop(0)
    if op == '+':
        return sum([int(x) for x in expr])
    elif op == '-':
        return int(expr[0]) - sum([int(x) for x in expr[1:]])
    elif op == '*':
        result = 1
        for x in expr:
            result *= int(x)
        return result
    elif op == '/':
        result = int(expr[0])
        for x in expr[1:]:
            result /= int(x)
        return result
    else:
        raise Exception("Unknown operator: " + op)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ex3.1.py <expression>")
        sys.exit(1)
    expr = sys.argv[1]
    tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    result = evaluate(tokens)
    print("Result: ", result)
