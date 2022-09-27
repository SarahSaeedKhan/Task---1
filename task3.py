def balanced(brackets):
    stack_list = []
    open_brackets = ['(', '{', '[']
    for char in brackets:
        if char in open_brackets:
            stack_list.append(char)
        else:
            if stack_list is None:
                return False
            current_char = stack_list.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False

    if stack_list:
        return False
    else:
        return True


brackets = input('enter a string/expression of brackets')
print('Input is:', brackets)
balanced(brackets)
if balanced(brackets) is False:
    print('Output:unbalanced')
else:
    print('Output:balanced')
