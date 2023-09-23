#patterns with alphabets
'''
In Python, you can obtain the ASCII value (or ordinal value) of a 
character using the built-in ord() function.The ord() function takes a 
single character as its argument and returns 
the ASCII value of that character as an integer.

Conversely, if you want to convert an ASCII value back to its corresponding
character, you can use the chr() function

A=65 
Z=90 

a=97
z=122 


A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

    
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end=" ")
    print()

    
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y

n=int(input())#5 
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+count),end=" ")
        count=count+1
    print()

    
A
B B
C C C
D D D D

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()

    
A 
A B 
A B C 
A B C D 
A B C D E 

n=int(input())#5 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

    
A B C D E 
A B C D 
A B C 
A B 
A 
 
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

    
        A
      A B
    A B C
  A B C D    
A B C D E   

n=int(input())
for i in range(1,n+1):
    #spaces
    for j in range(n-i):
        print(" ",end=" ")
    #alphabets 
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

    
   A
  B C
 D E F
G H I J

n=int(input())
count=0
for i in range(1,n+1):
    #spaces 
    for j in range(n-i):
        print(" ",end="")
    #alpha 
    for k in range(1,i+1):
        print(chr(65+count),end=" ")
        count=count+1 
    print()

    
   A
  A B     
 A B C
A B C D

n=int(input())#4
for i in range(1,n+1):
    #spaces 
    for j in range(n-i):
        print(" ",end="")
    #alpha
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

    
    A 
   A B 
  A B C 
 A B C D 
A B C D E 
 A B C D 
  A B C 
   A B 
    A 


n=int(input())
#upper pyramid
for i in range(1,n+1):
    #spaces 
    for j in range(n-i):
        print(" ",end="")
    #alphs
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
#lower pyramid
for i in range(n-1,0,-1):
    #spaces 
    for j in range(n-i):
        print(" ",end="")
    #alphs
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

A
B B
C   C
D     D
E E E E E  

'''



n = int(input())
alpha = 65
for row in range(n):
    left_spaces = " " * (n - row - 1) 
    hollow_spaces = " " * (2 * row - 1)
    if row == 0:
        each_row = left_spaces + chr(alpha)
        alpha += 1
    else:
        each_row = left_spaces + chr(alpha) + hollow_spaces + chr(alpha)
        alpha += 1
    print(each_row)
    
alpha -= 2

for row in range(1, n):
    left_spaces = " " * row 
    hollow_spaces = " " * (2 * (n - row - 1) - 1)
    if row == n - 1:
        each_row = left_spaces + chr(alpha)
    else:
        each_row = left_spaces + chr(alpha) + hollow_spaces + chr(alpha)
        alpha -= 1 
    print(each_row)