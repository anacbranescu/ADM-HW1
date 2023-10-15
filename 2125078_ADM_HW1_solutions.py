#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Problem 1


# In[ ]:


#Say "Hello, World!" With Python
print("Hello, World!")


# In[ ]:


#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b) 
    print (a-b) 
    print(a*b) 


# In[ ]:


#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a//b)
    print (a/b)


# In[ ]:


#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n) :
        print (i*i)


# In[ ]:


#Write a function
def is_leap(year):
    leap=False
    if year%4 ==0:
        if year %100== 0:
            if year %400== 0 :
                leap = True
            else: leap = False
        else:leap =True
    else: leap =False  
    return leap


# In[ ]:


#Print Function
if __name__ == '__main__':
    n =int(input())
    for i in range (n): 
        print(i+1, end ="")


# In[ ]:


#Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n= int(input())
    
if n% 2 !=0:
    print("Weird")
elif n>=2 and n<=5:
    print ("Not Weird")
elif n>=6 and n<= 20:
    print("Weird")
elif n>20 :
    print("Not Weird")


# In[ ]:


#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
Lista= [[i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if i+j+k != n]

print(Lista)


# In[ ]:


#Find the Runner-Up Score!
if __name__ == '__main__':
    n= int(input())
    arr=map(int, input().split())
    nlist = list(arr)
    nlist.sort()
    test_list= list(set(nlist))
    x= max (test_list)
    y= test_list.index(x)
    print(test_list[y-1])


# In[ ]:


#Nested Lists
if __name__ == '__main__':
    lista =[]
    for _ in range(int(input( ))):
        name = input()
        score = float(input())
        lista.append([name,score])
    second= sorted(set(score for name, score in lista))[1]
    second_name= sorted(name for name,score in lista if score== second)
    print(*second_name, sep = "\n")


# In[ ]:


#Finding the percentage
if __name__ == '__main__':
    n= int(input())
    marks ={}
    for _ in range(n):
        name, *line = input().split()
        scores= list(map(float, line))
        marks[name]= scores
    query_name = input()
 
    avg = sum(marks[query_name]) / len(marks[query_name])
    avg_2= "{:.2f}".format(avg)
    print(avg_2)


# In[ ]:


#Lists
if __name__ == '__main__':
    n = int(input())
    my_list =[]

    for _ in range(n) :
        command =input().split()
        command = [int(x) if x.isdigit() else x for x in command]

        if command and command[0] == "insert":
            my_list.insert(int(command[1]), command[2])
    

        elif command and command[0] == "print":
            print(my_list)

        elif command and command[0] == "remove":
            my_list.remove(command[1])
    

        elif command and command[0] == "append":
            my_list.append(command[1])
    

        elif command and command[0] == "sort":
            my_list.sort()
    

        elif command and command[0] == "pop":
            my_list.pop()
    

        elif command and command[0] == "reverse":
            my_list.reverse()


# In[ ]:


#Tuples
if __name__ == '__main__':
    n= int(input())
    mapn= map(int,input().split())
    t=tuple(mapn)
    print(hash(t))


# In[ ]:


#sWAP cASE
def swap_case(s):
    return s.swapcase()


# In[ ]:


#String Split and Join
def split_and_join(line):
    # write your code here
    line= line.split(" ")
    line= "-".join(line)
    return line


# In[ ]:


#What's Your Name?   
def print_full_name(first, last):
    mesaj = "Hello {} {}! You just delved into python."
    print (mesaj.format(first,last))


# In[ ]:


#Mutations
def mutate_string(string, position, character):
    string = string[0:position] + character + string[position+1:]
    return string


# In[ ]:


#Find a string
def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if (string.count(sub_string, i,i+len(sub_string))) >0:
            count+= 1
    return count


# In[ ]:


#String Validators
if __name__ == '__main__':
    s = input()
    x=0
    for i in s:
        if i.isalnum():
            x+=1
    if x!=0 :
        print("True")
    else:
        print ("False")
        
    x1=0
    for i in s:
        if i.isalpha():
            x1+=1
    if x1!=0 :
        print("True")
    else:
        print ("False")    
    
    x2=0
    for i in s:
        if i.isdigit():
            x2+=1
    if x2!=0 :
        print("True")
    else:
        print ("False")    
  
    x3=0
    for i in s:
        if i.islower():
            x3+=1
    if x3!=0 :
        print("True")
    else:
        print ("False")    
  
    x4=0
    for i in s:
        if i.isupper():
            x4+=1
    if x4!=0 :
        print("True")
    else:
        print ("False")  


# In[ ]:


#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


#Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)


# In[ ]:


#Designer Door Mat
x= input().split()
n= int(x[0])
m= int(x[1])

mess= "WELCOME"
patt= ".|."
midd= int(n/2)

for l in range(n):
    if l< midd:
        print(str(patt * ((l * 2) + 1)).center(m, "-"))
        
    if l==midd:
        print(mess.center(m,"-"))
    
    if l> midd:
        print(str(patt*((n-l )* 2 - 1)).center(m, "-"))


# In[ ]:


#String Formatting
def print_formatted(number):
    for i in range(1, number + 1):
        nr = len(bin(number)) -2
        print("{0:>{nr}d} {0:>{nr}o} {0:>{nr}X} {0:>{nr}b}".format(i, nr=nr))


# In[ ]:


#Alphabet Rangoli 
#ispired from discussions
def print_rangoli(size):
    lett = "abcdefghijklmnopqrstuvwxyz"[:size] 
    center = "-".join([c for c in lett[::-1]] + [c for c in lett[1:]])
    design = []
    for i in range(1, size+1):
        letters = [c for c in lett[-i:]]
        if len(letters) == 1:
            design.append("-".join(letters).center(len(center), "-"))
        else:
            design.append("-".join(letters[::-1] + letters[1:]).center(len(center), "-"))

    print("\n".join(design + design[::-1][1:]))


# In[ ]:


#Capitalize!
def solve(s):
    name= []
    for i in s.split(" "):
        if i.isalpha():
            name.append(i.capitalize() )
        else:
            name.append(i)
    return " ".join(name )


# In[ ]:


#Introduction to Sets
def average(array):
    new=set(array)
    return round(sum(new)/len(new),3)


# In[ ]:


#Symmetric Difference
m = int(input())
m1 = set(map(int, input().split()))

n = int(input())
n1 = set(map(int, input().split()))

f1 = m1.difference(n1)
f2 = n1.difference(m1)
final = sorted(f1.union(f2))

for i in final:
    print(i)


# In[ ]:


#Calendar Module
#Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y = input().split()
day = calendar.weekday(int(y), int(m), int(d))

dayname = calendar.day_name
print(dayname[day].upper())


# In[ ]:


#Shape and Reshape
import numpy
n=9
a= numpy.array(list(map(int, input().split())))
a.shape = (3,3)
print (a)


# In[ ]:


#Transpose and Flatten
from numpy import array, transpose
n, m = map(int, input().split())
val = []

for i in range(n):
    val.append(list(map(int, input().split())))

print(transpose(array(val)))
print(array(val).flatten())


# In[ ]:


#Polynomials
import numpy
coef= input()
x= float(input())
lista_coef= list(map(float, coef.split()))

print (numpy.polyval(lista_coef,x))


# In[ ]:


#Linear Algebra
import numpy
N= int(input())
A= [list(map(float, input().split())) for _ in range (N)]

det = numpy.linalg.det(A)
print(round(det, 2))


# In[ ]:


#Default Arguments
def print_from_stream(n, stream=None):
    if stream is None :
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


# In[ ]:


Problem 2


# In[ ]:


#Birthday Cake Candles
import math
import os
import random
import re
import sys
def birthdayCakeCandles(candles):
    max=0
    n=0
    for candle in candles:
        if candle>max :
            max =candle
    for candle in candles:
        if candle==max:
            n+=1
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys
def kangaroo(x1, v1, x2, v2):
    
    if v1 == v2 and x2>= x1:
        return "NO"
        
    meet = (x2 - x1) / (v1 - v2)
    if meet < 0 or meet % 1 != 0:
        return "NO"
    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


#Viral Advertising
import math
import os
import random
import re
import sys
def viralAdvertising(n):
    see = 2
    like= 2
    for _ in range(n-1):
        see= (see*3)//2
        like += see
    return like

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#Recursive Digit Sum
import math
import os
import random
import re
import sys
def superDigit(n, k):
    
    n =k* sum([int(n[l]) for l in range(len(n))]) 
    if n > 9:
        return superDigit(str(n), 1)
    else:
        return n
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


#Insertion Sort - Part 1
#Inspired from discussions
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    x = arr[-1]
    sort = sorted(arr)
    for i in arr[-2::-1]  :
        if arr== sort:
            break
        elif  i> x:
            arr[arr.index(i) +1]=i
        else:
            arr[arr.index(i) +1] =x
            
        print (*arr)
        
    else:
        if  arr!= sort: 
            arr[0] = x
            
            print(*arr)
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# In[ ]:


#Insertion Sort - Part 2
import math
import os
import random
import re
import sys
def insertionSort2(n, arr):
    for i in range (1, n) :
        element= arr[ i]
        l= i- 1
        
        while l>= 0 and element < arr[l]:
            arr[l+1] = arr[l]
            l-= 1
        arr[l +1] =element
        sort=map(str, arr)
        
        print(" ".join(sort))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

