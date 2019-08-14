
# coding: utf-8

# In[6]:


#Python program to input a number from the user and check if it is positive, negative or zero. 
num = float(input("Enter a number : "))
if num > 0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")


# In[8]:


#Python Program to Check if a Number is Odd or Even by taking user input.
#A number is even if division by 2 give a remainder of 0.
#If remainder is 1, it is odd number.
num =int(input("Enter a number: "))
if (num%2)==0:
    print("{0}is Even".format(num))
else:
    print("{0}is Odd".format(num))



# In[12]:


#Python Program to input a year with century and check ,
#if it is Leap Year or print invalid if it is not in the form of year with century.
year = int(input("Enter a year:"))
# To get year (integer input) from the code
#year = 2000

if (year%4)==0:
   if(year%100)==0:
    if(year%400)==0:
        print("{0}is a leap year".format(year))
    else:
        print("{0}is not a leap year".format(year))
   else:
    print("{0}is a leap year".format(year))
else:
    print("{0}is not a leap year".format(year))



# In[15]:


#Python Program to Find the Largest Among Three Numbers, using the least number of lines of code. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if(num1>=num2) and (num1>=num3):
    largest= num1
elif(num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3
print("the largest number between",num1,",",num2,"and",num3,"is",largest)


# In[18]:


#Python program to input a month name and print number of days in it
print("List of months: January, February, March, April, May, June, July, August, September, October, November,December")
month_name =input("Input the name of Month: ")

if month_name =="February":
    print("No.of days: 28/29 days")
elif month_name in("April,June,September,November"):
    print("No.of days: 30 days")
elif month_name in("January,March,May,July,August,October,December"):
    print("No.of days: 31 days")
else:
    print("wrong month name")


# In[27]:


#Python Program to Check if a number is Prime Number or not
num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
         if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
         else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# In[30]:


#Python program to display all the prime numbers within an interval
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[40]:


#Python Program to Find the Factorial of a Number

num=int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)


# In[41]:


#Python Program to Display the multiplication Table by taking the number as input
n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)


# In[46]:


#Python Program to Print the Fibonacci sequence. 

nterms = int(input("How many terms? "))

n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[52]:


#Python Program to Find the Sum of Natural Numbers
num = int(input("Enter a number: "))
if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is",sum)
    

