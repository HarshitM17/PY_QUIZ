from calc import *
import webbrowser

Name = input("Enter your name:- ")
Age = input("Enter your age")


print("There are 10 questions in this quiz which are given below...")
ques_a=int(input("Ques 1--> Multiply 4 and 5 ::"))
score=0
if ques_a==20:
    print("Correct")
    score+=1
else:
    num_a,num_b=map(int,input("Enter the numeber a & b to get correct output:").split())
    print(mul(num_a,num_b))
ques_b=int(input("Enter the value of 40 x (34+42):"))
if ques_b==3040:
    print("Correct")
    score+=1
else:
    num_a,num_b,num_c=map(int,input("Enter the numeber a , b and c to get correct output:").split())
    print(mul(40,add(num_b,num_c)))
print("Hint!! Where 42/17 in integer")
ques_c=int(input("Enter the integer value of 76+(40 x (42/17)):"))
if ques_c==156:
    print("Correct")
    score+=1
else:
    num_a,num_b,num_c,num_d=map(int,input("Enter the numeber a , b , c and d to get correct output:").split())
    print(add(num_a,mul(num_b,div(num_c,num_d))))
print("Hint!! Division will be in form of a integer")
ques_d=int(input("Enter the value of 432 - (34 x (67/(64+34))):"))
if ques_d==432:
    print("Correct")
    score+=1
else:
    num_a,num_b,num_c,num_d,num_e=map(int,input("Enter the numeber a,b,c,d and e to get correct output:").split())
    print(sub(num_a,mul(num_b,div(num_c,add(num_d,num_e)))))
ques_e=input("How many seconds are in a day : ")
if ques_e=="86400":
    print("Correct")
    score+=1
else:
    print("Wrong answer!!")
    print("Correct answer is {}".format(mul(24,mul(60,60))))
ques_f=int(input("Give the answer of the following:-  sqrt(3249)+(19)^2: "))
if ques_f==418:
    print("Correct")
    score+=1
else:
    num_a,num_b=map(int,input("Enter the numeber a and b to get correct output:").split())
    print(root(3259)+square(19))
ques_g=int(input("How many states are in India:- "))
if ques_g==28:
    print("Correct")
    score+=1
else:
    print("The number of states in India are {}.".format(28))
ques_h=int(input("How many union teritories are in India:-  "))
if ques_h==8:
    print("Correct")
    score+=1
else:
    print("The number of union teritories in India are {}.".format(8))
ques_i=input("What is the capital of Rajasthan:- ")
if ques_i.upper()=="JAIPUR":
    print("Correct")
    score+=1
else:
    print("The capital of Rajasthan is {}.".format("Jaipur"))
ques_j=input("What is the Capital of India:- ")
if ques_j.upper()=="NEW DELHI":
    print("Correct")
    score+=1
else:print("The Capital of India is {}.".format("New Delhi"))

if 8<=score<=10:
    print("Congragulations on your excellence Mr/Ms/Mrs {}.".format(Name))
    webbrowser.open("https://drive.google.com/file/d/1XW3wumvguf82tPYVvkSe7YMH92wh8yKQ/view")
else:
    print("Better luck next time!")