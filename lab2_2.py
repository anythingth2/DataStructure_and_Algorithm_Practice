# order = str(input('Enter : '))
order = "{}"

LEFT_BRACKET = ('[','{','(')
RIGHT_BRACKET = (']','}',')')
BRACKET = LEFT_BRACKET + RIGHT_BRACKET


left_bracket_stack = []
right_bracket_stack = []

def match(bracket,next_bracket):
    if bracket == '[':
        return next_bracket == ']'
    elif bracket == '(':
        return next_bracket == ')'
    elif bracket == '{':
        return next_bracket == '}'

err = False
for char in order:
    if char in BRACKET:
        if char in LEFT_BRACKET:
            left_bracket_stack.append(char)
        else:
            bracket = left_bracket_stack.pop()
            if match(bracket,char):
                pass
            else:
                err = True
                break

if len(left_bracket_stack) != 0:
    err = True

if err:
    print('MISMATCH')
else:
    print('MATCH')


def matcher2(expression):
    tmp = []
    pList =  ['(', '[', '{', ')', ']', "}"]
    pureP = ''.join([i for i in expression if i in pList])
    for c in pureP:
        if(pList.index(c) < 3):
            tmp.append(c)
        elif pList[pList.index(c)-3] == tmp[-1]:
            tmp.pop()
        else:
            return False
    return tmp == []

def matcher2List(expressionList):
    return [matcher2(expression) for expression in expressionList]