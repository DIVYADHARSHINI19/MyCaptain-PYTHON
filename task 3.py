#Fibonacci Series
terms=int(input("Enter the fibonacci terms: "))
a=0
b=1
print("The Fibonacci sequence is :")
if terms==1:
    print(a)
else:
    print(a)
    print(b)

    for i in range(2,terms):
        c=a+b
        a=b
        b=c

        print(c)