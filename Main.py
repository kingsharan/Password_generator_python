import random
import string

print("This is a random password generator. This will generate a specific password for you.")

digit = float(input("How many number password do you need Max 12 Min 8 "))
while digit !=8 and digit !=12 and digit !=11 and digit !=9 and digit !=10:
    print("enter valid number")
    digit = float(input("How many number password do you need Max 12 Min 8 "))
a = random.choice(string.ascii_uppercase)
b = random.randint(0,9)
c = random.choice(string.ascii_lowercase)
d = ''.join([random.choice(  '!@#$%^&*()_' ) for n in range(1)])
e = random.choice(string.ascii_uppercase)
f = random.randint(0,9)
g = random.choice(string.ascii_lowercase)
h = random.choice(string.ascii_uppercase)
i = random.randint(0,9)
j = random.choice(string.ascii_lowercase)
k = random.randint(0,9)
l = random.choice(string.ascii_lowercase)
main8 = 10
main9 = 10
main10 = 10
main11 = 10
main12 = 10
if digit == 8:
    main8 =random.randint(0,3)#8
if digit == 9:
    main9 =random.randint(0,3)#9
if digit == 10:
    main10 =random.randint(0,3)#10
if digit == 11:
    main11 =random.randint(0,3)#11
if digit == 12:
    main12 =random.randint(0,3)#12      

if main8 == 0:
    print(a,b,c,d,e,f,g,h)

if main8 == 1:
    print(h,g,f,e,d,c,b,a)

if main8 == 2:
    print(b,a,c,e,d,g,h,f)

if main8 == 3:
    print(e,a,c,g,h,f,d,b)
#end        
if main9 == 0:
    print(a,b,c,d,e,f,g,h,k)

if main9 == 1:
    print(h,g,f,e,d,c,b,a,j)

if main9 == 2:
    print(b,a,c,e,d,g,h,f,l)

if main9 == 3:
    print(e,a,c,g,h,f,d,b,a)
#end        
if main10 == 0:
    print(a,b,c,d,e,f,g,j,i,e)

if main10 == 1:
    print(h,g,f,e,d,c,b,b,l,f)

if main10 == 2:
    print(b,a,c,e,d,g,h,e,b,l)

if main10 == 3:
    print(e,a,c,g,h,f,d,k,l,b)
#end         
if main11 == 0:
    print(b,f,a,c,d,e,f,g,j,i,e)

if main11 == 1:
    print(l,h,g,f,e,d,c,b,b,l,f)

if main11 == 2:
    print(b,a,c,e,d,g,k,h,e,b,l)

if main11 == 3:
    print(e,a,c,g,h,f,d,l,k,l,b)
#end       
if main12 == 0:
    print(b,f,a,c,d,e,f,g,j,i,e,l)

if main12 == 1:
    print(l,h,g,f,e,d,c,b,b,l,f,a)

if main12 == 2:
    print(b,a,c,e,d,g,k,h,e,b,l,f)

if main12 == 3:
    print(e,a,c,g,h,f,d,l,k,l,j,b)
#end       
