def evaluate(expression):
    """Evaluate a mathematical expression"""
    try:
        return eval(expression.replace(' ', ''))
    except:
        return None

def generate_expressions(digits, operators, expression=''):
    """Recursively generate all possible expressions"""
    if not digits:
        result = evaluate(expression)
        if result == 200:
            print(expression, '=', result)
        return

    for op in operators:
        generate_expressions(digits[1:], operators, expression + digits[0] + op)
        generate_expressions(digits[1:], operators, expression + digits[0])

# Generate all possible combinations of the given operators
operators = ['', '+', '-']
digits = '9876543210'
generate_expressions(digits, operators)
