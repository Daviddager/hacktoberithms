def main():
    f = open("input.txt", "r")
    for arg in f:
        print(has_valid_parenthesis(arg))
        #has_valid_parenthesis(arg)

def has_valid_parenthesis(expression):
    graph = {
            '{':'}',
            '(':')',
            '[':']'
    }
    stack = []
    for char in expression:
        if char in graph:
            stack.append(char)
        else:
            if len(stack) > 0 and char == graph[stack[len(stack) - 1]]:
                stack.pop()
    if len(stack) > 0:
        return False
    return True

main()
