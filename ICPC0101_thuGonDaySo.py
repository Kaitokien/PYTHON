n = int(input())
a = [int(x) for x in input().split()]
stack = []
stack.append(a[0])
for i in range(1, len(a)):
    if len(stack) > 0 and (a[i] + stack[len(stack) - 1]) % 2 == 0:
        stack.pop()
    else: stack.append(a[i])
print(len(stack))