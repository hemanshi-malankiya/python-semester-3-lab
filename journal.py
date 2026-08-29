#1. Write a program to input 2 nos and print their difference
s1=int(input("Enter a no 1:"))
s2=int(input("Enter a no 2:"))
s3=s1-s2
print("The diffference is:",s3)

#2. Write a program to input a no and print whether its an even no or odd no.
n1=int(input("Enter a no:"))
if n1%2==0:
    print("given number is even:")
else:
    print("the given number is odd.")

#3. Write a program to input 3 nos and print the large of the 3 numbers
n1=int(input("Enter a no 1:"))
n2=int(input("Enter a no 2:"))
n3=int(input("Enter a no 3:"))
if n1>=n2 and n1>=n3:
    print("the largest num is :",n1)
elif n2>=n3 and n2>=n1:
    print("The largest number is:",n2)
else:
    print("The largest number is:",n3)

#4. Write a program to input a string and print it n times.
s1=input("Enter a string:")
n=int(input("Enter how many times to print (n): "))

times=s1*n
print(f"{times}",end=" ")

#5. Write a program to input 2 strings and print whether they are equal

s1=input("Enter a string 1:")
s2=input("Enter a string 2:")
if s1==s2:
    print("The string are same")
else:
    print("THe string are not same")
    

#6. Write a program to input a month no and print it as a string
 
month_no = int(input("Enter month number (1-12): "))


months_dict = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

for key, value in months_dict.items():
    if key == month_no:
        print(f"The month is: {value}")

#7. Write a program to input the name and 5 subject marks out of 100
 #for a student Calculate the mark average. Print the grade    
#( >=85 A, >=70  and < 85 B, >=55 and < 70 C, >=35 and < 55 D, < 35 Fail)
marks=(input("ENter a student name:"))
total=0
for i  in range(1,6):
    s=int(input(f"Enter marks for subject {i}: "))
    print(f"Subject {i} marks: {s}")
    total+=s
print(f"{marks}: {total}")

avg=total/5
print(avg)

if avg>=85:
    print("A")
elif avg>=70 and avg<85:
    print("B")
elif avg>=55 and avg<70:
    print("C")
elif avg>=35 and avg<55:
    print("D")
elif avg<35:
    print("fail")
else:
    print("Inavalid")
    
#8. Print all the nos from 1-10 using a for loop
for i in range(1,11)
print(i)

 #9. Input 20 nos and print the no of a unit no,
#tens no, 100s no, or a 1000s no 10.   
for i in range(1,21):
    no=int(input("Enter a no:"))
    if no in range(1,10):
        print("unit")
    elif no in range(10,100):
        print("ten")
    elif no in range(100,1000):
        print("100s")
    elif no in range(1000,10000):
        print("1000s number")

         
#11. Print the fibonacci series for numbers lesser than 100
 a=0
 b=1
for i in range(1,101):
    i=a+b
    if i >= 100:
        break
    
    print(i)
    a=b
    b=i
    
#12. Write a program to print all the Armstrong nos between 11 – 999.
    for num in range(11, 1000):

    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + (digit * digit * digit)
        temp = temp // 10

    if sum == num:
        print(num)
#13. Write a script to input a no and print whether it’s a palindrome or not
 num = int(input("Enter a number: "))

temp = num
rev = 0

while temp > 0:

    digit = temp % 10

    rev = rev * 10 + digit

    temp = temp // 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")       
        


    
#14. Write a script to input strings from the user till the user enters 'end'.
#Print the length of all the strings entered and print the no of strings whose
#length is greater than 5 and the no of strings whose length is
#lesser than 5
greater=0
smaller=0

while True:
  s=(input("Enter a string:"))

  if s=="end":
    break

  length=len(s)
  print("length",length)

  if length > 5:
        greater += 1
  elif length < 5:
        smaller += 1

print("\nNumber of strings with length greater than 5:", greater)
print("Number of strings with length less than 5:", smaller)

#15. Write a script to input strings and print whether its a
#palindrome or not ( do not use built in functions use
#the while loop and + operator )

s=input("Emter a string:")
rev=""
length=len(s)

i=len(s)-1
while i>=0:
    rev=rev+s[i]
    i=i-1

if s==rev:
   print("String is palindrome.")
else:
    print("not palindrome.")
    
#16. Input a number and print its binary value
'''num = int(input("Enter a number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2

print("Binary =", binary)'''

#17.
#18. Print all the numbers from 1 to 10 using a while loop.
i = 1

while i <= 10:
    print(i)
    i = i + 1

#19. Print all the even numbers using a for loop.
for i in range(1, 11):
    if i % 2 == 0:
    print(i)

#20. Print all the odd numbers from 1 to 100 using a for loop

for i in range(1, 101):

    if i % 2 != 0:
        print(i)

#21. Print the sum of all odd numbers and even numbers from 1 to 100
even = 0
odd = 0

for i in range(1, 101):

    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print("Sum of even numbers =", even)
print("Sum of odd numbers =", odd)

#22.Input a string and print it character by character
s = input("Enter a string: ")

for i in s:
    print(i)

#23.Input a string and print the number of vowels and consonants
s = input("Enter a string: ")

vowel = 0
consonant = 0

for i in s:

    if i in "AEIOUaeiou":
        vowel = vowel + 1
    else:
        consonant = consonant + 1

print("Number of vowels =", vowel)
print("Number of consonants =", consonant)

 
'''#24. Write a python program to input two DNA string of same length and print a dot plot. 
  A T G C 
A 1 0 0 0 
T 0 1 0 0 
T 0 1 0 0 
C 0 0 0 1'''

s1=list(input("Enter a string 1:")
s2=list(input("Enter a string 2:")
print(s1)
print(s2)

if len(s1)==len(s2):
    print(" "," ".join(s2))

for i in s1:
    print(i, end=" ")
    for j in s2:
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()       


#25. Write a Python script that determines SNPs from a multiple
#sequence alignment
#and outputs each SNP and its position. For example if the input is

>s0
ACCCTGTATAAC
>s1
ACCGTGTACAAC
>s2
ACCCTGTAAAAC

then the output should be

"C/G" 	3
"A/C/T" 8
    

 s0 = input("Enter sequence 1: ")
s1 = input("Enter sequence 2: ")
s2 = input("Enter sequence 3: ")

if len(s0) == len(s1) == len(s2):

    for i in range(len(s0)):
        bases = []

        if s0[i] not in bases:
            bases.append(s0[i])

        if s1[i] not in bases:
            bases.append(s1[i])

        if s2[i] not in bases:
            bases.append(s2[i])

        if len(bases) > 1:
            print("/".join(bases), i)

else:
     print("Sequences must have the same length.")
'''    
26. Write a Python program to count the number of strings where the string
  length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

    print("All sequences must be of same length.")
List = ['abc', 'xyz', 'aba', '1221']

count = 0

for i in List:
    if len(i) >= 2:
        if i[0] == i[-1]:
            count = count + 1

print(count)

'''27. Write a Python program to get a list, sorted in increasing
order by the last element in each tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''

List = [(2,5), (1,2), (4,4), (2,3), (2,1)]
print(List)
for i in range(len(List)):
    for j in range(i+1, len(List)):
        if List[i][1] > List[j][1]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp

print("Result:",List)

#28.  Write a Python program to find
#the list of words that are longer than n from a given list of words.

l=input("Enter a word:").split()
print(l)

for i in l:
    print(i,len(i))

s=int(input("enter a n number:"))

for i in l:
      if len(i)>=s:
       print(i)

#29. Write a Python function that takes two lists
#and returns True if they have at least one common member

# 29. Write a Python function that takes two lists
# and returns True if they have at least one common member.

def common_member(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = input("Enter the elements of first list: ").split()
list2 = input("Enter the elements of second list: ").split()

result = common_member(list1, list2)
print(result)

#31. Write a Python program to generate all permutations of a list in Python. 
List = [10, 15, 20, 25, 30, 35, 40]

result = [i for i in List if i % 2 != 0]
print(result)

#32. Write a Python program to get the difference between the two lists. 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

result = []

for i in list1:
    if i not in list2:
        result.append(i)
print(result)

#33. Write a Python program access the index of a list
List = ["apple", "banana", "mango", "orange"]
for i in range(len(List)):
    print("Index =", i, "Value =", List[i])
    
#34. Write a Python program to convert a list of characters into a string. 
List = ['P', 'Y', 'T', 'H', 'O', 'N']

s = "".join(List)
print(s)

List = ['P', 'Y', 'T', 'H', 'O', 'N']

s = ""

for i in List:
    s = s + i

print(s)

#35. Write a Python program to find the index of an item in a specified list. 
List = ["apple", "banana", "mango", "orange"]
print(List)

item=input("Enter a item to find:")
for i in range(len(List)):
    if List[i]==item:
        print("Index",i)

#36. Write a Python program to append a list to the second list. 

l1=[1,2,3]
l2=[4,5,6,7]
l2.append(l1)
print(l2)

#37.#37. Write a Python program to select an item randomly from a list.
List = ["apple", "banana", "mango", "orange"]
print(List)
index = int(input("Enter index: "))

print("Selected item:", List[index])

import random

List = input("Enter list items separated by spaces: ").split()

item = random.choice(List)

print("Random item:", item)

#38. Write a Python program to find the second smallest and largest
 #number in a list
List = [10, 25, 8, 45, 15, 30]
print(List)

List.sort()
print(List)


print("Second Smallest =", List[1])
print("Second Largest =", List[-2])


#39. Write a Python program to get the frequency of the elements in a list.
List = [1, 2, 3, 2, 4, 1, 2, 5, 3, 1]
print(List)

for i in List:
    print(i, ":", List.count(i))

#40. Write a Python program to count the number of elements in a
    #list within a specified range.

List = [10, 25, 8, 45, 15, 30, 18, 22]

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

count = 0

for i in List:
    if i >= lower and i <= upper:
        count = count + 1
print("Count =", count)

'''47. Write a Python program to convert list to list of dictionaries. 
Sample lists: ["Black", "Red", "Maroon", "Yellow"],
 ["#000000", "#FF0000", "#800000", "#FFFF00"]'''

color=["Black", "Red", "Maroon", "Yellow"]
code=["#000000", "#FF0000", "#800000", "#FFFF00"]
r=[]

for i in range(len(color)):
    d={
       "color":color[i],
       "code":code[i]
        }
    r.append(d)

print(r)    


##48. Write a Python program to split a list every Nth element. 
##Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
##List size : 5
##Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
l= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n']
n=5
r=[]
for i in range(n):
    new=l[i::n]
    r.append(new)
print(r)    

'''49. Write a Python program to compute the difference between two lists. 
Sample data: ["red", "orange", "green", "blue", "white"],
["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']'''
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
set1 = set(color1)
set2 = set(color2)
diff1 = list(set1 - set2)


diff2 = list(set2 - set1)


print("Color1-Color2:", diff1)
print("Color2-Color1:", diff2)


'''50. Write a Python program to replace the last element in
a list with another list. 
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]'''

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
result = list1[:-1] + list2

print(result)


'''51. Write a Python program to insert a given string at the
beginning of all items in a list. 
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']'''

list=[1,2,3,4]
l="emp"
r=[]
for i in list:
    new=l+str(i)
    r.append(new)


print(r)
    


'''52. Write a Python program to move all zero digits to end of a given
list of numbers. 
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9,
10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9,
7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0,
      9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
result=[]
print(list)
for i in list:
    if i!=0:
        result.append(i)
        
zero_count=list.count(0)
result.extend([0]*zero_count)
print(result)

'''53. Write a Python program to find the list in a list
of lists whose sum of elements is the highest. 
Sample lists: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
Expected Output: [10, 11, 12]'''

l=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
highest=l[0]
max_sum=sum(highest)

for i in l:
    curr_sum=sum(i)

    if curr_sum >max_sum:
        max_sum=curr_sum
        highest=i
print(highest)

'''54. Write a Python program to find all the values in a
list are greater than a input number.'''
my_list = [5, 12, 18, 22, 30, 45]
print(my_list)

n = int(input("Enter a number: "))

r = []


for i in my_list:
    if i > n:
       r.append(i)

print("Values greater than the input number:")
print(r)

#55. Write a Python program to find the items starts with
   # specific character from a given list. 
Expected Output:
Original list: 
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
[‘a’,’d’,’w’]
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]

l = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

r = ['a', 'd', 'w']

print("Original list:")
print(l)

for x in r:
    result = []

    for i in range(len(l)):
        if l[i].startswith(x):
            result.append(l[i])

    print("Items start with", x, "from the said list:")
    print(result)

##56. Write a Python program to flatten a given nested list structure. 
##Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
##Flatten list:
##[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
l =[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print("Original list:",l)
flatten_list=[]
for i in l:
    if type(i)==list:
        for j in i:
            flatten_list.append(j)
    else:
        flatten_list.append(i)
print("flatten_list:",flatten_list)

##57. Write a Python program to remove consecutive duplicates of a given list. 
##Original list:
##[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
##After removing consecutive duplicates:
##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
##

list=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print("List",list)
l=[list[0]]
for i in range(1,len(list)):
    if list[i]!=list[i-1]:
        l.append(list[i])
        
print(l)

##58. Write a Python program to pack consecutive duplicates of a given list elements into sublists. 
##Original list:
##[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
##After packing consecutive duplicates of the said list elements into sublists:
##[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]


l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

result = []
temp = [l[0]]

for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        temp.append(l[i])
    else:
        result.append(temp)
        temp = [l[i]]

result.append(temp)

print("Original list:")
print(l)

print("After packing consecutive duplicates of the said list elements into sublists:")
print(result)
##59. Write a Python program to remove the K'th element from a given list, print the new list. 
##Original list:
##K=2
##[1, 1, 2, 3, 4, 4, 5, 1]
##After removing an element at the kth position of the said list:
##[1, 1, 3, 4, 4, 5, 1]
l=[1, 1, 2, 3, 4, 4, 5, 1]
print(l)
k=2
d=[]
for i in range(len(l)):
    if i != k - 1:
        d.append(l[i])
print(d)

##60. Write a Python program to insert an element at a specified position into a given list. 
##Original list:
##[1, 1, 2, 3, 4, 4, 5, 1]
##Value : 12
##Positon : 3
##After inserting an element at kth position in the said list:
##[1, 1, 12, 2, 3, 4, 4, 5, 1]

l=[1, 1, 2, 3, 4, 4, 5, 1]
print(l)

n=int(input("Enter a value to insert:"))
p=int(input("Enter a position:"))     
for i in range(len(l)) :
    if i==p-1:
      l.insert(p-1,n)
print(l)      
      
##61. Write a Python program to read a matrix from console and print the sum for each column.
## Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. 
##Input rows: 2
##Input columns: 2
##Input number of elements in a row (1, 2, 3,4):
##1 2
##3 4
##sum for each column:
##4 6
##sum for each row
##3 7
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

matrix = []

# Input matrix
for i in range(rows):
    row = []

    for j in range(columns):
        value = int(input("Enter element: "))
        row.append(value)

    matrix.append(row)

# Print matrix
print("Matrix:")

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()

# Sum of each column
print("Sum for each column:")

for j in range(columns):
    total = 0

    for i in range(rows):
        total = total + matrix[i][j]

    print(total, end=" ")

print()

# Sum of each row
print("Sum for each row:")

for i in range(rows):
    total = 0

    for j in range(columns):
        total = total + matrix[i][j]

    print(total, end=" ")

##62. Write a Python program to find the list with maximum and minimum length. 
##Original list:
##[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
##List with maximum length of lists:
##(3, [13, 15, 17])
##List with minimum length of lists:
##(1, [0])
##Original list:
##[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
##List with maximum length of lists:
##(3, [3, 5, 7])
##List with minimum length of lists:
##(1, [0])
    


l = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

print("Original list:", l)

max_list = l[0]
min_list = l[0]

for i in l:
    if len(i) > len(max_list):
        max_list = i

    if len(i) < len(min_list):
        min_list = i

print("List with maximum length of lists:", (len(max_list), max_list))
print("List with minimum length of lists:", (len(min_list), min_list))

##63. Write a Python program to count the number of sublists
##contain a particular element. 
##Original list:
##[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
##Count 1 in the said list:
##3
##Count 7 in the said list:
##2
##Original list:
##[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
##Count 'A' in the said list:
##3
##Count 'E' in the said list:
##1

l = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]

n = int(input("Enter element: "))

count = 0

for i in l:
    if n in i:
        count = count + 1

print("Count:", count)

##65. Write a Python program to extract common index
##elements from more than one given list. 
##Do it without using sets
##Original lists:
##[1, 1, 3, 4, 5, 6, 7]
##[0, 1, 2, 3, 4, 5, 7]
##[0, 1, 2, 3, 4, 5, 7]
##Common index elements of the said lists:
##[1, 7]
l1 = [1, 1, 3, 4, 5, 6, 7]
l2 = [0, 1, 2, 3, 4, 5, 7]
l3 = [0, 1, 2, 3, 4, 5, 7]
print(l1)
print(l2)
print(l3)

result = []

for i in range(len(l1)):
    if l1[i] == l2[i] and l2[i] == l3[i]:
        result.append(l1[i])

print("Common index elements:", result)

##66. Write a Python program to extract specified size of strings from a give list of string values. 
##Original list:
##['Python', 'list', 'exercises', 'practice', 'solution']
##length of the string to extract:
##8
##After extracting strings of specified length from the said list:
##['practice', 'solution']


l=['Python', 'list', 'exercises', 'practice', 'solution']
print(l)
L=[]

x=int(input("Enter  a length of the string to exract:"))
for i in range(len(l)):
    if len(l[i]) == x:
     L.append(l[i])

print(L)
print("After extracting:", L)
      


##67. Write a Python program to rotate a given list by specified number of items to the right or left direction. 
##original List:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##Rotate the said list in left direction by 4:
##[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
##Rotate the said list in left direction by 2:
##[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
##Rotate the said list in Right direction by 4:
##[8, 9, 10, 1, 2, 3, 4, 5, 6]
##Rotate the said list in Right direction by 2:
##[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", l)

l = l[4:] + l[:4]
print("Left rotation by 4:", l)

# Left rotation by 2
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = l[2:] + l[:2]
print("Left rotation by 2:", l)

# Right rotation by 4
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = l[-4:] + l[:-4]
print("Right rotation by 4:", l)

# Right rotation by 2
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = l[-2:] + l[:-2]
print("Right rotation by 2:", l)
l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

##68. Write a Python program to find the item with maximum occurrences in a given list. 
##Original list:
##[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
##Item with maximum occurrences of the said list:
##2

l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

max_count = 0
max_item = 0

for i in l:
    count = l.count(i)

    if count > max_count:
        max_count = count
        max_item = i

print("Item with maximum occurrences:", max_item)

##69. Write a Python program to access multiple elements of specified index from a given list. 
##Original list: use list comprehension
##[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
##Index list:
##[0, 3, 5, 7, 10]
##Items with specified index of the said list:
##[2, 4, 9, 2, 1]
l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print(l)

index = [0, 3, 5, 7, 10]

result = [l[i] for i in index]

print("Items with specified index:", result)

##70. Write a Python program to check whether a specified list is sorted or not. 
##Original list:
##[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
##Is the said list is sorted!
##True
##Original list:
##[1, 2, 4, 6, 8, 10, 12, 16, 14, 17]
##Is the said list is sorted!
##False
l = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print(l)
print("Is the said list is sorted!")
if l == sorted(l):
    print(True)
else:
    print(False)
    
##71. Write a Python program to extract the nth element from a given list of tuples. 
##Original list:
##[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
##Extract nth element ( n = 0 ) from the said list of tuples:
##['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
##Extract nth element ( n = 2 ) from the said list of tuples:
##[99, 96, 94, 98]
##

data = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

# Extract nth element
n = 0
result = [t[n] for t in data]
print(result)

n = 2
result = [t[n] for t in data]
print(result)

##72. Write a Python program to check if the elements of a given list are unique or not. 
##Original list:
##[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
##Is the said list contains all unique elements!
##False
##Original list:
##[2, 4, 6, 8, 10, 12, 14]
##Is the said list contains all unique elements!
##True
list1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
list2 = [2, 4, 6, 8, 10, 12, 14]

print("Original list:")
print(list1)

if len(list1) == len(set(list1)):
    print("Is the said list contains all unique elements!")
    print(True)
else:
    print("Is the said list contains all unique elements!")
    print(False)


print("\nOriginal list:")
print(list2)

if len(list2) == len(set(list2)):
    print("Is the said list contains all unique elements!")
    print(True)
else:
    print("Is the said list contains all unique elements!")
    print(False)
##
##73. Write a Python program to sort a list of lists by a
##given index of the inner list. 
##Original list:
##[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96),
## ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
##Sort the said list of lists by a given index ( Index = 0 ) of the inner list
##[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96),
## ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
##Sort the said list of lists by a given index ( Index = 2 ) of the inner list
##[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96),
## ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]

data = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

print("Original list:")
print(data)

print("\nSort by index 0:")
print(sorted(data, key=lambda x: x[0]))

print("\nSort by index 2:")
print(sorted(data, key=lambda x: x[2]))

##74. Write a Python program to remove all elements
##from a given list present in another list. 
##Original lists:
##list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##list2: [2, 4, 6, 8]
##Remove all elements from 'list1' present in 'list2:
##[1, 3, 5, 7, 9, 10]


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

print("Original list1:")
print(list1)

print("Original list2:")
print(list2)

for x in list2:
    if x in list1:
        list1.remove(x)

print("After removing elements:")
print(list1)

##75. Write a Python program to create a list taking
##alternate elements from a given list. 
##Original list: use list comprehension
##['red', 'black', 'white', 'green', 'orange']
##List with alternate elements from the said list:
##['red', 'white', 'orange']
##Original list:
##[2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
##List with alternate elements from the said list:
##[2, 3, 0, 8, 4]
# Original lists
list1 = ['red', 'black', 'white', 'green', 'orange']
list2 = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]

# Taking alternate elements using list comprehension
result1 = [list1[i] for i in range(0, len(list1), 2)]
result2 = [list2[i] for i in range(0, len(list2), 2)]

print("Original list:", list1)
print("List with alternate elements:", result1)

print("Original list:", list2)
print("List with alternate elements:", result2)

##76. Write a Python program to find the nested lists
##elements which are present in another list. 
##Original lists:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
##[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
##Intersection of said nested lists:
##[[12], [7, 11], [1, 5, 8]]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

list2 = [
    [12, 18, 23, 25, 45],
    [7, 11, 19, 24, 28],
    [1, 5, 8, 18, 15, 16]
]

result = []

for sublist in list2:
    temp = []
    
    for x in sublist:
        if x in list1:
            temp.append(x)
    
    result.append(temp)

print("Original lists:")
print(list1)
print(list2)

print("Intersection of said nested lists:")
print(result)

##77. Write a Python program to find common element(s) in a given nested lists. 
##Original lists:
##[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
##Common element(s) in nested lists:
##[18, 12]
lists = [
    [12, 18, 23, 25, 45],
    [7, 12, 18, 24, 28],
    [1, 5, 8, 12, 15, 16, 18]
]

print("Original lists:")
print(lists)

common = []

for element in lists[0]:
    found = True

    for sublist in lists[1:]:
        if element not in sublist:
            found = False
            break

    if found:
        common.append(element)

print("Common element(s) in nested lists:")
print(common)

##78. Write a Python program to reverse strings in a
##given list of string values. 
##Original lists:
##['Red', 'Green', 'Blue', 'White', 'Black']
##Reverse strings of the said given list:
##['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
list1 = ['Red', 'Green', 'Blue', 'White', 'Black']

print("Original list:")
print(list1)

result = []

for word in list1:
    reverse = word[::-1]
    result.append(reverse)

print("Reverse strings of the said given list:")
print(result)

##79. Write a Python program to find the maximum and minimum
##product from the pairs of tuple within a given list. 
##The original list, tuple :
##[(2, 7), (2, 6), (1, 8), (4, 9)]
##Maximum and minimum product from the pairs of the said tuple of list:
##(36, 8)
list1 = [(2, 7), (2, 6), (1, 8), (4, 9)]

print("The original list, tuple:")
print(list1)

products = []

for pair in list1:
    product = pair[0] * pair[1]
    products.append(product)

maximum = max(products)
minimum = min(products)

print("Maximum and minimum product from the pairs of the said tuple of list:")
print((maximum, minimum))

##80. Write a Python program to interleave multiple lists of the same length. 
##Original list:
##list1: [1, 2, 3, 4, 5, 6, 7]
##list2: [10, 20, 30, 40, 50, 60, 70]
##list3: [100, 200, 300, 400, 500, 600, 700]
##Interleave multiple lists:
##[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500,
## 6, 60, 600, 7, 70, 700]
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]

print("Original list:")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

result = []

for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])
    result.append(list3[i])

print("Interleave multiple lists:")
print(result)

##81. Write a Python program to remove words from a given
##list of strings containing a character or string. 
##Original list:
##list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
##Character list:
##['#', 'color', '@']
##New list:
##['Red', '', 'Green', 'Orange', 'White']
list1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
characters = ['#', 'color', '@']

result = []

for word in list1:
    new_word = word

    for char in characters:
        new_word = new_word.replace(char, '')

    result.append(new_word.strip())

print("Original list:")
print(list1)

print("Character list:")
print(characters)

print("New list:")
print(result)

##82. Write a Python program to calculate the sum of
##the numbers in a list between the indices of a specified range. 
##Original list:
##[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
##Range: 8 , 10
##Sum of the specified range:
##29
l = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]

start = 8
end = 10

total = 0

for i in range(start, end + 1):
    total = total + l[i]

print("Original list:")
print(l)

print("Sum of the specified range:")
print(total)

##83. Write a Python program to reverse each list in a given list of lists. 
##Original list of lists:
##[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
##Reverse each list in the said list of lists:
##[[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]
##


l = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

result = []

for x in l:
    result.append(x[::-1])

print("Original list of lists:")
print(l)

print("Reverse each list:")
print(result)


##84. Write a Python program to compute the sum of digits of
##each number of a given list. 
##Original tuple: 
##[10, 2, 56]
##Sum of digits of each number of the said list of integers:
##14
##Original tuple:
##[10, 20, 4, 5, 'b', 70, 'a']
##Sum of digits of each number of the said list of integers:
##19
##Original tuple:
##[10, 20, -4, 5, -70]
##Sum of digits of each number of the said list of integers:
##19
l = [10, 2, 56]

total = 0

for num in l:
    for digit in str(num):
        total = total + int(digit)

print("Original list:")
print(l)

print("Sum of digits:")
print(total)
##
##85. Write a Python program to remove specific words from a given list. 
##Original list:
##['red', 'green', 'blue', 'white', 'black', 'orange']
##Remove words:
##['white', 'orange']
##After removing the specified words from the said list:
##['red', 'green', 'blue', 'black']
# Original data
original_list = ["red", "green", "blue", "white", "black", "orange"]
words_to_remove = ["white", "orange"]

# Remove words using list comprehension
result_list = [word for word in original_list if word not in words_to_remove]

# Print outputs
print("Original list:")
print(original_list)

print("\nRemove words:")
print(words_to_remove)

print("\nAfter removing the specified words from the said list:")
print(result_list)

##86. Write a Python program to add two given lists of different lengths,
##start from left. 
##Original lists:
##[2, 4, 7, 0, 5, 8]
##[3, 3, -1, 7]
##Add said two lists from left:
##[5, 7, 6, 7, 5, 8]
##Original lists:
##[1, 2, 3, 4, 5, 6]
##[2, 4, -3]
##Add said two lists from left:
##[3, 6, 0, 4, 5, 6]
l1 = [2, 4, 7, 0, 5, 8]
l2 = [3, 3, -1, 7]

result = []

for i in range(len(l1)):
    if i < len(l2):
        result.append(l1[i] + l2[i])
    else:
        result.append(l1[i])

print("Original lists:")
print(l1)
print(l2)

print("Add said two lists from left:")
print(result)

##87. Write a Python program to find the last occurrence of a specified
##item in a given list. 
##Original list:
##['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
##Last occurrence of f in the said list:
##7
##Last occurrence of k in the said list:
##14
l = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f',
     'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

items = ['f', 'k']

for item in items:
    position = -1

    for i in range(len(l)):
        if l[i] == item:
            position = i

    print("Last occurrence of", item, "in the said list:")
    print(position)
##    
##88. Write a Python program to get the index of the first element
##which is greater than a specified element. 
##Original list:
##[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
##Index of the first element which is greater than 73 in the said list:
##4
##Index of the first element which is greater than 21 in the said list:
##1

l = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

number = 73

for i in range(len(l)):
    if l[i] > number:
        print("Index of the first element which is greater than", number, ":")
        print(i)
        break
    
##89. Write a Python program to split a given list into specified sized chunks. 
##Original list:
##[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
##Split the said list into equal size 3
##[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
##Split the said list into equal size 4
##[[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
##Split the said list into equal size 5
##[[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]
l = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

sizes = [3, 4, 5]

for size in sizes:
    result = []

    for i in range(0, len(l), size):
        result.append(l[i:i + size])

    print("Split into size", size, ":")
    print(result)

####90. Write a Python program to convert a given list of strings into
##    list of lists. Original list of strings:
####['Red', 'Maroon', 'Yellow', 'Olive']
####Convert the said list of strings into list of lists:
####[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
####    
l = ['Red', 'Maroon', 'Yellow', 'Olive']

result = []

for word in l:
    result.append(list(word))

print("Original list of strings:")
print(l)

print("Convert into list of lists:")
print(result)

##91. Write a Python program to convert a given list
##of strings and characters to a single list of characters. 
##Original list:
##['red', 'white', 'a', 'b', 'black', 'f']
##Convert the said list of strings and characters to a single list of characters:
##['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']
l = ['red', 'white', 'a', 'b', 'black', 'f']

result = []

for word in l:
    for char in word:
        result.append(char)

print("Original list:")
print(l)

print("Single list of characters:")
print(result)

##92. Write a Python program to insert an element in a given list after every nth position. 
##Original list:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
##Insert a in the said list after 2 nd element:
##[1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
##Insert b in the said list after 4 th element:
##[1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

n = 2
element = 'a'

result = []

for i in range(len(l)):
    result.append(l[i])

    if (i + 1) % n == 0:
        result.append(element)

print("Original list:")
print(l)

print("Insert a after every 2nd element:")
print(result)

##93. Write a Python program to remove the last N number
##of elements from a given list. 
##Original lists:
##[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
##Remove the last 3 elements from the said list:
##[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
##Remove the last 5 elements from the said list:
##[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
##Remove the last 1 element from the said list:
##[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
##
l = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]

numbers = [3, 5, 1]

print("Original list:")
print(l)

for n in numbers:
    result = l[:-n]

    print("Remove the last", n, "elements:")
    print(result)
    
##94. Write a Python program to find the minimum, maximum value
##for each tuple position in a given list of tuples. 
##Original list:
##[(2, 3), (2, 4), (0, 6), (7, 1)]
##Maximum value for each tuple position in the said list of tuples:
##[7, 6]
##Minimum value for each tuple position in the said list of tuples:
##[0, 1]
l = [(2, 3), (2, 4), (0, 6), (7, 1)]

max_result = []
min_result = []

for i in range(len(l[0])):
    values = []

    for tup in l:
        values.append(tup[i])

    max_result.append(max(values))
    min_result.append(min(values))

print("Original list:")
print(l)

print("Maximum value for each tuple position:")
print(max_result)

print("Minimum value for each tuple position:")
print(min_result)

##95. Write a Python program to get the unique values in a given list of lists. 
##Original list:
##[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
##Unique values of the said list of lists:
##[0, 1, 2, 3, 4, 5, 7]
##Original list:
##[['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
##Unique values of the said list of lists:
##['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']
##l = [[1, 2, 3, 5],
     [2, 3, 5, 4],
     [0, 5, 4, 1],
     [3, 7, 2, 1],
     [1, 2, 1, 2]]

result = []

for sublist in l:
    for value in sublist:
        if value not in result:
            result.append(value)

result.sort()

print("Original list:")
print(l)

print("Unique values:")
print(result)

##96. Given a list of marks, create a list containing "Pass" if marks are 40 or above, otherwise "Fail" .
##Python marks = [35, 80, 45, 20, 90, 40]
##Expected output: Python ['Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']



# Given list of marks
marks = [35, 80, 45, 20, 90, 40]

# List comprehension to map marks to "Pass" or "Fail"
status = ["Pass" if mark >= 40 else "Fail" for mark in marks]

# Print the resulting list
print(status)

##97. Given a list of numbers, create a list containing "Positive" , "Negative" , or "Zero" . Python numbers = [-3, 0, 5, -1, 8]
##Expected output: Python ['Negative', 'Zero', 'Positive', 'Negative', 'Positive']
##
numbers = [-3, 0, 5, "-1,", 8]


output = [
    "Positive" if float(str(n).replace(",", "")) > 0 
    else "Negative" if float(str(n).replace(",", "")) < 0 
    else "Zero" 
    for n in numbers
]

print(output)

##98. Given a list of words, create a list of words that start with a vowel. Python words = ["apple", "banana", "orange", "grape", "umbrella"]
##Expected output: Python ['apple', 'orange', 'umbrella']

words = ["apple", "banana", "orange", "grape", "umbrella"]

vowel_words = [word for word in words if word[0].lower() in "aeiou"]

print(vowel_words)

##99. Given a list of words, create a list of palindromic words.
##Python words = ["madam", "python", "level", "data", "radar"]
##Expected output: Python ['madam', 'level', 'radar']
words = ["madam", "python", "level", "data", "radar"]

palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)

##100. Given a list of numbers, create a list of squares only for even numbers.
##Python numbers = [1, 2, 3, 4, 5, 6]
##Expected output: Python [4, 16, 36]

numbers = [1, 2, 3, 4, 5, 6]

squares = []

for num in numbers:
    if num % 2 == 0:
        squares.append(num ** 2)

print(squares)

##101. Given a list of numbers, create a list of cubes only for odd numbers.
##Python numbers = [1, 2, 3, 4, 5]
##Expected output: Python [1, 27, 125]
numbers = [1, 2, 3, 4, 5]

cubes = []

for num in numbers:
    if num % 2 != 0:
        cubes.append(num ** 3)

print(cubes)


##102. Given a sentence, create a list of words with length greater than 3.
##Python sentence = "Python is easy and powerful"
##Expected output: Python ['Python', 'easy', 'powerful']

       
sentence = "Python is easy and powerful"

result = [word for word in sentence.split() if len(word) > 3]

print(result)

##103. Given a list of strings, create a list containing the first character of each string.
##Python words = ["DNA", "RNA", "Protein", "Gene"]
##Expected output: Python ['D', 'R', 'P', 'G']
words = ["DNA", "RNA", "Protein", "Gene"]

result = [word[0] for word in words]

print(result)

##104. Create a multiplication table list for number 5 from 1 to 10.
##Expected output: Python [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
number = 5

result = [number * i for i in range(1, 11)]

print(result)

##105. Create a list of pairs (i, j) where i ranges from 1 to 3 and j ranges from 1 to 3.
##Expected output: Python [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
##
result = [(i, j) for i in range(1, 4) for j in range(1, 4)]

print(result)

##106. Create a list of pairs (i, j) where the sum of i and j is even. Python i = 1 to 4 j = 1 to 4
##Expected output: Python [(1, 1), (1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (4, 2), (4, 4)]

result = [(i, j) for i in range(1, 5) for j in range(1, 5) if (i + j) % 2 == 0]

print(result)

##107. Flatten the following nested list.
##Python matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
##Expected output: Python [1, 2, 3, 4, 5, 6, 7, 8, 9]
##
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = [item for row in matrix for item in row]

print(result)



    

    











            


        

   

        
        

        
 

        

        

        




    
    
    
           

