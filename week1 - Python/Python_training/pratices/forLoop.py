"""For loop praticles"""

for i in reversed(range(1,11)):
    print(i)
print('reversed')
for i in range(1,11,2):
    print(i)
print("range")
for i in range(1,20):
    if i==12:
        continue
    else:
        print(i)
print('continue')
for i in range(1,20):
    if i==12:
        break
    else:
        print(i)

print('break')
for i in range(5):
    for j in range(10):
        print('*',end='')
    print()