#a=2+(5-2)/6
#b=4/5 + ( 10 - 3 )/6
#print(f'Answer with out round of a is :{a}')
#print(f'Answer with round of a is{round(a)}')
#print(f'Answer with out round of b is :{b}')
#print(f'Answer with out round of a is :{round(a)}')

#for i in range(0,50):
 #   if i%2==0:
 #     print("even number is ",i)
    
#number=0
#while number<=50:
#    print(number)
#    number=number+2

#for i in range(0,50):
#    if i%2!=0:
#        print("Prime number is",i)

#number=int(input("Enter Number to find it is prime or Not        :   "))
#if number%2!=0:
#    print("It is prime number") 
#else:
#    print("It is not Prime number")    


#for i in range(0,11):
#    mul_table=i*i
#    print(f'{i}*{i}={mul_table}')

#counter=0
#for i in range(0,100):
#    if i%2==0:
#        print(f"{i}", end=' ')
#    counter=counter+i
#print(f"Sum of all even number is {counter}")

#counter=0
#for i in range(0,100):
#    if i%2!=0:
#        print(f"{i}", end=' ')
#    counter=counter+i
#print(f"Sum of all odd number is {counter}")
    
# for i in range(1500,2700):
#     if i%7==0 :
#       print(f"numbers are divisible by 7  : {i}")
# for i in range(1500,2700):
#   if i%5==0:
#     print(f' number are multiple of 5 {i}')      
  
#import random
#random_number=random.randint(0,9)
#try_=0
#print("would You like to play guess game?")
#print("Yes for 1")
#rint("No for 0")

#option=int(input("Enter option above"))
#if option==1:
  #  print("lets play")
  #  guess=int(input("guess a number between 0 to 9  :  "))

  #  if guess > random_number:
  #      print("your guess is too high")
 #   if guess< random_number:
   #     print("your guess is low")
 #   if guess==random_number:
   #     print("you win")
 #   try_=try_+1
   # while guess!=random_number and try_<3:
  #      guess=int(input("try again"))
  #      try_+=1
 #   if guess > random_number:
 #       print("your guess is too high")
#    if guess< random_number:
    #    print("your guess is low")
 #   if guess==random_number:
#        print("you win")


#elif  option==0:
 #   pass

#else:
#    print("Enter Valid Option")

#start=0
#a=1

#for i in range(0,100):
#    if i==1:
#        next=i
#    else:
#        next=start+a
#        start=a
#        a=next
#   print(next ,end=' ')
#    i+=1
    


# rows = 6
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")

# list=[1,2,3,12,19,2]
# ref=3
# new_list=[]
# for i in range(len(list)):
#   total=ref+list[i]
#   print(str(total),end=' ')


# print("I am trying both method with conversion")
# total=[i+ref for i in list]
# print(total)

# tup=(2,5,6,5)
# conversion=list(tup)
# print(conversion)
# conversion.append(10)
# print("After conversion of tuple  :",conversion)

# dict1 = {'name':'talha','password':'Iamthebest','name':'Johndoe'}
# print(dict1)
# 

# def smallest_num_list( list ):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min
# print(smallest_num_list([1, 2, 4, 0,8,6,4,2,41]))

# num=int(input("Enter Number: "))
   
# if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                print("number not is prime")
#                break
#        else:
#            print("number is prime",end=' ') 
    
# fibo_series=[0,1]
# Numbers=int(input("Enter Number to find fibo series"))

# if  Numbers>2:
#   for i in range(2,Numbers):
#     NXt=fibo_series[i-1]+fibo_series[i-2]
#     fibo_series.append(NXt)
# print(fibo_series)