stack=[]
def push(elmnt):
    stack.append(elmnt)
def pop():
    stack.pop()
    print(stack)
def match(ch1, ch2):
    match_dict={')': '(',']': '[','}': '{'}
    return match_dict[ch1] == ch2
def is_balanced(s):
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if len(stack)==0:
                return False
            if not match(ch,stack.pop()):
                return False
    return len(stack)==0
x=input()
y=is_balanced(x)
print(y)