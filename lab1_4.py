def gen_pattern(chars):
    width = len(chars)*4 -3
    pattern=[]
    
    for i in range(len(chars)):
        front = chars[-1:-i-1:-1]
        end = chars[-i-1:]
        text = front+ end
        pattern.append( '.'.join(text).center(width,'.' ))
    pattern += pattern[-2::-1]
    return '\n'.join(pattern)
    raise NotImplementedError()

print(gen_pattern('WXYZ'))