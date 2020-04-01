s = input()
l = eval(input())
j = []
for i in l:
    if i.startswith(s):
        j.append(i)
print(j)
