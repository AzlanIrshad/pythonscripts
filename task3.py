n = int(input())
result = ''.join(str(n)for n in range(n+1))
print(result)

n = int(input())
for i in range(n+1):
    if i != 0:
        print(i, end='')