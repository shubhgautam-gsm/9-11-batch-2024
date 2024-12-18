# First, print the descending part
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(1,6-i):
        print(j, end=' ')
       
    print('\n')

# Then, print the ascending part
