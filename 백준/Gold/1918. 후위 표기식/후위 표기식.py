infix = input()
postfix=''
stack = []
stack_out = {'(':3, '*':2,'/':2, '+':1, '-':1}
stack_in = {'(':0, '*':2,'/':2, '+':1, '-':1}

for token in infix:
    if token not in '+-*/()':
        postfix += token
    elif token ==')':
        while stack and stack[-1] !='(':
            ad = stack.pop()
            postfix += ad
        stack.pop()
    else:
        while stack and stack_in[stack[-1]] >= stack_out[token]:
            a = stack.pop()
            postfix += a
        stack.append(token)
while stack:
    postfix += stack.pop()    

print(postfix)
        

