a = int(input())
lis = map(int, input().split())
A = set(lis)
b = int(input())
newlis = map(int, input().split())
B = set(newlis)
C = sorted(A ^ B)
for i in C:
    print(i)
