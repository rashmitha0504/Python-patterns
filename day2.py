'''
1.

* * * * * *
*         *
*         *
* * * * * *

rows=int(input())
columns=int(input())
for i in range(1,rows+1):
    if i==1 or i==rows:
        print("* "*columns)
    else:
        print("* "+"  "*rows+"*")

2.

*
* *
*   *
*     *
* * * * *    

n=int(input())
for i in range(n):
    if i==0:
        print("* ")
    elif i==n-1:
        print("* "*n)
    else:
        right_spaces="  "*(n-i-1)
        hollow_spaces="  "*(i-1)
        print("* "+hollow_spaces+"* "+right_spaces)

3.

        *
      * *
    *   *
  *     *
* * * * *

n=int(input())
for i in range(0,n):
    if i==0:
        print("  "*(n-1)+"*")
    elif i==n-1:
        print("* "*n)
    else:
        left_spaces="  "*(n-i-1)
        hollow_spaces="  "*(i-1)
        print(left_spaces+"* "+hollow_spaces+"* ")

4.

* * * * *
  *     *
    *   *
      * *
        *

n=int(input())
for i in range(0,n):
    if i==0:
        print("* "*n)
    elif i==(n-1):
        print("  "*(n-1)+"* ")
    else:
        left_spaces="  "*i 
        hollow_spaces="  "*(n-i-2)
        print(left_spaces+"* "+hollow_spaces+"* ")
    
5.

* * * * *
*     *
*   *
* *
*

n=int(input())
for i in range(0,n):
    if i==0:
        print("* "*n)
    elif i==(n-1):
        print("* ")
    else:
        hollow_spaces="  "*(n-i-2)
        print("* "+hollow_spaces+"* ")

6.

    *
   * *
  *   *
 *     *
* * * * *

n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print(" "*(n-i)+"* "*i)
    else:
        hollow_spaces="  "*(i-2)
        left_spaces=" "*(n-i)
        print(left_spaces+"* "+hollow_spaces+"* ")

7.

* * * * *
 *     *
  *   *
   * *
    *

n=int(input())
for i in range(n,0,-1):#5,4,3,2,1
    if (i==1 or i==n):#1 or 5
        print(" "*(n-i)+"* "*i)
    else:
        left_spaces=" "*(n-i)
        hollow_spaces="  "*(i-2)
        print(left_spaces+"* "+hollow_spaces+"* ")


8.

* 
* *
*   *
*     *
*   *
* *
*

n=int(input())#4 
print("* ")
for i in range(1,n):
    hollow_spaces="  "*(i-1)
    print("* "+hollow_spaces+"* ")
for j in range(n-1,1,-1):
    spaces="  "*(j-2)
    print("* "+spaces+"* ")
print("* ")


9.
        *
      * *
    *   *
  *     *
*       *
  *     *
    *   *
      * *
        *

n=int(input())#5 
print("  "*(n-1)+"*")
for i in range(1,n):
    hollow_spaces="  "*(i-1)
    left_spaces="  "*(n-i-1)
    print(left_spaces+"* "+hollow_spaces+"* ")
for j in range(n-1,1,-1):
    left_spaces="  "*(n-j)
    hollow_spaces="  "*(j-2)
    print(left_spaces+"* "+hollow_spaces+"* ")
print("  "*(n-1)+"* ")



10.

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

n=int(input())#5 
print(" "*(n-1)+"* ")
for i in range(2,n+1):
    spaces=" "*(n-i)
    hollow="  "*(i-2)
    print(spaces+"* "+hollow+"* "+spaces)
for j in range(n-1,1,-1):
    spaces=" "*(n-j)
    hollow="  "*(j-2)
    print(spaces+"* "+hollow+"* ")
print(" "*(n-1)+"* ")

'''