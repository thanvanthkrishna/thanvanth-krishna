#lambda task
#1.max of 3 num
a=lambda x,y,z:max(x,y,z)
x=int(input("Enter a num:"))
y=int(input("Enter a num:"))
z=int(input("Enter a num:"))
print(max(x,y,z))

#2.even or odd
a=lambda x:x%2==0
n=int(input("Enter a num:"))
b=a(n)
print(b)
if b==True:
    print("It is even")
else:
    print("It is odd")

#3.div by 5
a=lambda x:"It is div by 5" if x%5==0 else "Not div by 5"
n=int(input("Enter a num:"))
print(a(n))

#4.square and cube
a=lambda x:x**2
n=int(input("Enter a num:"))
print("The square value is:",a(n))
b=lambda x:x**3
print("The cube value is:",b(n))


#5.last digit
a=lambda x:x%10
b=int(input("Enter a  num:"))
print("The last digit is:",a(b))

#6.positive or negative
a=lambda x:"Positive" if x>=0 else "Negative"
n=int(input("Enter a num:"))
print(a(n))

#7.pass or fail
a=lambda x:"PASS" if x>=40 else "FAIL"
n=int(input("Enter a num:"))
print(a(n))


#8.multiply 3 num
a=lambda x,y,z:x*y*z
x=int(input("Enter a num:"))
y=int(input("Enter a num:"))
z=int(input("Enter a num:"))
print(a(x,y,z))

#9.string length
a=lambda x:len(x)
b=input("Enter a string:")
print(a(b))

#10.temperature conversion
a=lambda x:(x*1.8)+32
n=int(input("Enter the temperature in celsius:"))
b=a(n)
print("Temperature in fahrenhit:",round(b,1))

#MAPPING
#1.square
a=[1,2,3]
square=list(map(lambda x:x**2,a))
print("square:",square)

#2.double
a=[2,4,6]
double=list(map(lambda x:x*2,a))
print("Double:",double)

#3.add 1
a=[5,6,7]
add=list(map(lambda x:x+1,a))
print("After adding 1:",add)

#4.convert to string
a=[1,2,3]
b=list(map(lambda x:str(x),a))
print("The string is:",b)

#5.cube
a=[1,2,3]
b=list(map(lambda x:x**3,a))
print("cube values:",b)

#6.uppercase
a=["a","b","c"]
b=list(map(lambda x:x.upper(),a))
print("uppercase:",b)

#7.string length
a=['hi','hello','bye']
b=list(map(lambda x:len(x),a))
print("String length:",b)

#8.add 2 list
a=[1,2,3]
b=[4,5,6]
c=list(map(lambda x,y:x+y,a,b))
print("added list:",c)

#9.multiply by 3
a=[5,6,7]
b=list(map(lambda x:x*3,a))
print("After multiplyed by 3:",b)

#10.subract 2
a=[5,6,7]
b=list(map(lambda x:x-2,a))
print("after sub by 2:",b)

#FILTERING
#1.even num
a=[1,2,3,4,5]
b=list(filter(lambda x:x%2==0,a))
print("Even numbers:",b)

#2.odd num
a=[1,2,3,4,5]
b=list(filter(lambda x:x%2!=0,a))
print("Odd:",b)

#3.num greater than 5
a=[2,6,8,1]
b=list(filter(lambda x:x>5,a))
print("Num greater than 5:",b)

#4.num less tha 10
a=[5,12,7,20]
b=list(filter(lambda x:x<10,a))
print("NUm less than 10:",b)

#5.positive num
a=[1,-2,3,-4]
b=list(filter(lambda x:x>0,a))
print("Positive num:",b)

#6.negative num
a=[1,-2,3,-4]
b=list(filter(lambda x:x<0,a))
print("Negative numbers:",b)

#7.num div by 3
a=list(range(1,11))
b=list(filter(lambda x:x%3==0,a))
print("num div by 3:",b)

#8.num div by 5
a=[10,12,15,7]
b=list(filter(lambda x:x%5==0,a))
print("Num div by 5:",b)

#9.num bw 1 to 10
a=[0,5,12,8]
b=list(filter(lambda x:0<x<10,a))
print("Num bw 1 to 10:",b)

#10.num equal to 7
a=[7,2,7,4]
b=list(filter(lambda x:x==7,a))
print("printing 7",b)
