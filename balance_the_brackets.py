# Check if the given set of brackets is balanced or not
# No user input required

# We should not use the count method because:
# suppose the given input was = )(
# The count logic would approve this, but in reality it makes no sense

inp = '[](){[]()(){}}'
stack = []
for i in inp:
    if len(stack) == 0:
        stack.append(i)
    else:
        if i == ')' and stack[-1] == '(':
            stack.pop()   
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(i)

if stack:
    print('Brackets are NOT balanced')
else:
    print('Brackets are balanced')  