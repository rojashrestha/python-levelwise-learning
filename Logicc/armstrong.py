#armstrong is a narcissistic number 
#if sum of the digit ^ number of digit = digit itself

num=int(input("enter the number:"))
sum=0
temp=num # to copy the num , so the orginal is not lost 
digits = len(str(num)) #length of the string and the str(num) function converts the interger to string 

while temp>0:
    digit=temp%10 #modulo operator , this gives the last digit of the number 
    sum += digit **digits
    temp = temp // 10 


if sum ==num:
    print(num,"is an armstrong number")
else:
    print(num, "is not an armstrong number")



