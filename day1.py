#some basic patterns in Python
'''
1.

* * *
* * *

rows=int(input())
columns=int(input())
for row in range(rows):
    print("* "*columns)

2.

*
* *
* * *
* * * *

rows=int(input())
for i in range(1,rows+1):
    print("* "*i)


3.

      *
    * *
  * * * 
* * * *

rows=int(input())
for i in range(1,rows+1):
    spaces="  "*(rows-i)
    stars="* "*i 
    print(spaces+stars)


4.

* * * *
  * * *
    * *
      *

rows=int(input())
for i in range(rows):
    spaces="  "*i
    stars="* "*(rows-i)
    print(spaces+stars)

5.

* * * *
* * *
* *
*

rows=int(input())
for i in range(rows):
    spaces="  "*i
    stars="* "*(rows-i)
    print(stars+spaces)

6.

    *
   ***
  *****
 *******
*********

input=int(input())
for i in range(1,input+1):
    spaces=" "*(input-i) 
    stars="*"* (2*i-1) 
    print(spaces+stars) 

7.

*********
 *******
  *****
   ***
    *

input=int(input())
for i in range(input,0,-1):#5,4,3,2,1
    spaces="  "*(input-i)
    stars="* "*(2*i-1)
    print(spaces+stars)


8.

    *
   * *
  * * *
 * * * *
* * * * *
 

input=int(input())
for i in range(1,input+1):
   spaces=" "*(input-i)
   stars="* "*i 
   print(spaces+stars)

   
9.

* * * * *
 * * * *
  * * *
   * *
    *

input=int(input())
for i in range(input,0,-1):
    spaces=" "*(input-i)
    stars="* "*i 
    print(spaces+stars)

    
10.

    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
  
n=int(input())#3
#uuper part of diamond
for i in range(1,n+1):#1,2,3
    spaces=" "*(n-i)
    stars="* "*i 
    print(spaces+stars)
#lower part of diamond
for j in range(n-1,0,-1):
    spaces=" "*(n-j)
    stars="* "*j 
    print(spaces+stars) 

11.

  *
 ***
*****
 ***
  *

n=int(input())
for i in range(1,n+1):
    spaces="  "*(n-i)
    stars="* "*(2*i-1)
    print(spaces+stars)
for j in range(n-1,0,-1):#2,1
    spaces="  "*(n-j)
    stars="* "*(2*j-1)
    print(spaces+stars)

12.
   *
  **
 ***
****
 ***
  **
   *   

n=int(input())
for i in range(1,n+1):
    spaces="  "*(n-i)
    stars="* "*(i)
    print(spaces+stars)
for j in range(n-1,0,-1):
    spaces="  "*(n-j)
    stars="* "*(j)
    print(spaces+stars)


13.

*
**
***
****
***
**
*

n=int(input())
for i in range(1,n+1):
    print("* "*i)
for j in range(n-1,0,-1):
    print("* "*j)

    
14.

*             *
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *


n=int(input())#4 
#upper butterfly
for i in range(1,n+1):
    spaces="  "*(2*(n-i))
    stars="* "*i 
    print(stars+spaces+stars)
#bottom butterfly 
for j in range(n-1,0,-1):
    spaces="  "*(2*(n-j))
    stars="* "*j 
    print(stars+spaces+stars)

'''