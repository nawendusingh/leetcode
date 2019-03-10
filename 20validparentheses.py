def vp(str):
    paren = {'[': ']', '(': ')', '{': '}'}
    stk = []
    for i in str:
        if i not in paren:
            if not stk or i != paren[stk[-1]]:
                return False
            else:
                stk.pop()
        else:
            stk.append(i)
    return stk == []


# imagine a stack,u find opening parenthese u push on stack
# u find closing parenthes u check if it matches top element on stack
# if it does you pop topmost element
# valid: when string is exhausted  and the stack is empty
# invalid: stack empty and closing parenthese is current i
# current i not matched topmost element on stack
# if stack not empty and str is exhausted

print(vp('{{[(]}}'))
