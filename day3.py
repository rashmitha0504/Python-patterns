# patterns with numbers
'''
1
1 2
1 2 3
1 2 3 4

n=int(input("No of rows :"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()



1 2 3 4
1 2 3
1 2
1

n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


      1
    1 2
  1 2 3
1 2 3 4

n=int(input())#4
for i in range(n):#0,1,2,3
    #for spaces
    for j in range(n-i-1):#1
        print(" ",end=" ")
    #for nums
    for j in range(i+1):
        print(j+1,end=" ")
    print()

    
1 2 3 4
  1 2 3
    1 2
      1

n=int(input())#4 
for i in range(n,0,-1):#4 3 2 1
    #spaces
    for j in range(n-i):#0 1 2 3 
        print(" ",end="")
    #nums 
    for j in range(1,i+1):
        print(j,end="")
    print()


1
2 2
3 3 3
4 4 4 4 

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

    
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

n=int(input())#4
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(count,end=" ")
        count=count+1 
    print()


1 4 9 
16 25 36
49 64 81

n = int(input())
count=1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(count*count, end=" ")
        count+=1
    print()


1 
2 3 
4 5 6
7 8 9 10

n=int(input())
count=1
for i in range(1,n+1):
    for j in range(i):
        print(count,end=" ")
        count=count+1 
    print()

      1
    2 3
  4 5 6
7 8 9 10

n=int(input())#4
count=1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(count,end=" ")
        count+=1 
    print()

   1
  2 2   
 3 3 3
4 4 4 4

n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(i,end=" ")
    print()

    
   1
  2 3
 4 5 6   
7 8 9 10

n=int(input())
count=1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(count,end=" ")
        count=count+1 
    print()

   1
  2 3
 4 5 6   
7 8 9 10
 11 12 13
   14 15
     16

n=int(input())#4
#upper pyramid
count=1
for i in range(1,n+1):
    #spaces
    for j in range(n-i):
        print(" ",end="")
    #nums
    for k in range(i):
        print(count,end=" ")
        count=count+1 
    print()

#lower pyramid 
for i in range(n-1,0,-1):
    #spaces 
    for j in range(n-i):
        print(" ",end="")    
    # Print numbers in ascending order
    for k in range(i):
        print(count, end=" ")
        count=count+1
    
    # Move to the next line for the next row
    print()
'''


