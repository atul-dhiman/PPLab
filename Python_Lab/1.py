# a=5
# b=2
# c=a+b
# d=a-b
# e=a*b
# f=a/b
# g=a//b
# f=a**b
# h=a%b
# # arithematic operators
# print(a) #additon
# print(b) #subtraction
# print(c) #mutliplication
# print(d) #divison
# print(e) #floorinng
# print(f) 
# print(h)

# #comparison operators
# print(a==b)
# print(a>b)
# print(a==b)
# print(a<b)
# print(a<=b)
# print(a>=b)
# print(a!=b)

# #assignment operator
# c=a
# print(c)
# c+=3
# print(c)
# c=-3
# print(c)
# c*=3
# print(c)
# c%=2
# print(c)
# c/=2
# print(c)
# c//=2
# print(c)


# #logical operators
# a=2
# b=10
# print(a<5 and b>19)
# is_allowance=True
# print(not is_allowance)


n=int(input("Enter the value of n"))
sum=0
for i in range(1,n+1):
    sum+=i**3
print(sum)