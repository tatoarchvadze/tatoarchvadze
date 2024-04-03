i = 0
while i < 10:
    print(i, end='\n' + ('-' * 10) + '\n')
    for j in range(10):
        print(j)
    i +=1


steps = 0 
for i in range(1920):
    for j in range(1000):
        print(f'{i} - {j}')
        steps += 1



print(steps)