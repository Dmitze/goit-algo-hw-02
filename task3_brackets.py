def check_brackets(expression):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return "Несиметрично"
            
            last_bracket = stack.pop()
            if brackets_map[char] != last_bracket:
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

# Тестування
test_expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "{[()]}"
]

for expr in test_expressions:
    result = check_brackets(expr)
    print(f"'{expr[:20]}...' -> {result}")