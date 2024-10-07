n = int(input().strip())
if n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird-2")
elif n % 2 == 0 and n > 20:
    print("Not Weird-2")
else:
    print("Weird-1")