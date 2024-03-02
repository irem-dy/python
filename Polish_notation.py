def polish_notation(expression: str) -> int:
    stack = []
    for token in reversed(expression.split()):
        if token.isdigit():
            stack.append(int(token))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(op1 / op2)
    return stack.pop()

expression = input("Lütfen bir aritmetik ifade girin: ")
result = polish_notation(expression)
print(f"Sonuç: {result}")
