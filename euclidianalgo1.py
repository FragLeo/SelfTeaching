print("Euclidian algorithm, finding the greatest common divisor of two whole numbers")
A = int(input("Input your first number: "))
B = int(input("Input your second number: "))

C = 0

print(A,B)

while B > 0:
    if A > B:
        A = A - B
    else:
        B = B - A

C = A 
print(C)