'''
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5

rows = int(input())
for i in range(1,rows+1):
    for j in range(i):
        print(i, end=' ')
    print('')


1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5


rows = int(input())
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

    
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

n=int(input())
count=0
for i in range(n,0,-1):
    count+=1
    for j in range(1,i+1):
        print(count,end=" ")
    print()

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

n=int(input())#5 
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

1
2 3
4 5 6
7 8 9 10

n=int(input())
count=1 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count=count+1 
    print()

'''