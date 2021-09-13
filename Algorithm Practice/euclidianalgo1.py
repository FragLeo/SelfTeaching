print("Euclidian algorithm, finding the greatest common divisor of two whole numbers")
A = int(input("Input your first number: "))
B = int(input("Input your second number: "))
Ain = A
Bin = B


C = 0

print(A,B)

while B > 0:
    if A > B:
        A = A - B
    else:
        B = B - A

C = A 
print("The largest common divisor of " + str(Ain) + " and " + str(Bin) + " is "+ str(C) + ".")
