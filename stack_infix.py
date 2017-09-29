OPERATOR = '+-*/'
temp_stack =[]
number_stack = []

equ = str(input('Enter equation : '))

for char in equ:
    if char in OPERATOR:
        temp_char = number_stack.pop()
        number_stack.append(char)
        number_stack.append(temp_char)
    else:
        number_stack.append(char)

print(''.join(number_stack))