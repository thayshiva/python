#from random import randint, randrange, choice
#import decimal

# question 2
# x = randint(1,50)
# y = randint(2,5)
# print(x)
# print(y)
# z = x**y
# print(z)

# question 3
# x = randint(1,10)
# print(x)
# for i in range(x):
#     print('suba')

# question 4
# x = decimal.Decimal(randrange(1,10))/100
# print(x)

#QUE 5

# for _ in range(5):
#     r = choice([(1,2),(1,3),(1,4),(1,5),(1,6)])
#     print(randint(*r))

# ques 6
# x = int(input("Enter the value x: "))
# y = int(input("Enter the value y: "))
# z = abs(x-y)/x+y
# print("Answer is : ", z)

#ques 7
# angle = int(input("Enter the angle: "))
# x = -90 % 360
# print("Angle is: ",x)

#ques 8
# seconds = int(input("Enter the number of seconds: "))
# min = seconds // 60
# min1 = seconds % 60
# print("%d minutes and %d seconds" % (min, min1))

#ques 9
#ModuleNotFoundError: No module named 'timedelta'

#ques 10
# user = int(input("Enter the number: "))
# s = pow(2,user)
# print(s)

#ques 11
# kg = int(input("Enter kg: "))
# pounds = kg/0.45359237
# print(round(pounds,1))

#ques 12
# n = int(input("Enter the number: "))
# fact = 1
#
# for i in range(1,n+1):
#     fact = fact * i
#
# print ("The factorial of 23 is : ",end="")
# print (fact)

#ques 13
# import math
# num = int(input("Enter the number: "))
# print(math.sin(num))
# print(math.cos(num))
# print(math.tan(num))

#ques 14
# import math
# degree = int(input("Enter the number: "))
# print(math.sin(degree))
# print(math.sin(math.radians(degree)))

#ques 15
# import math
# n = 0
# for i in range(0,345,15):
#     print(round(math.sin(math.radians(i)),4),end=" , ")
#     print(round(math.cos(math.radians(i)),4))

#ques 16


#ques 17
# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")

#ques 18
# dollar = 1.00
# nickels = 1.00 / .05
# pennies = 1.00 / .01
# dimes = 1.00 / .10
# quater = 1.00 / .25
# #print("nickels = {0}, pennies = {1}, dimes = {2}, quater = {3}", %(nickels, pennies, dimes, quater))
# print("nickels = " + str(nickels), "pennies = " + str(pennies), "dimes = " + str(dimes), "quater = " + str(quater))

#ques 19
# n = int(input("Enter the number of rows: "))
# m = int(input("Enter the number of columns: "))
# num = 0
# for row  in range(0, n):
#     for col in range(0, m):
#         print(end=' ')
#         num = num + 1
#     print()

# for i in range(1, 8 * 1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print(" ")

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
num = 0
for row  in range(0, n+2):
    for col in range(0, m):
        print(end=' ')
        num = num + 1
        if num > 10:
            print(num % 10, end=' ')

    print()
