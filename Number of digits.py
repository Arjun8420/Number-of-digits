#Program to find the number of digits in a given number

Num = int(input("Enter the number = "))
digits = 0

while Num != 0 :
    Num = Num // 10
    print("Number =",Num)
    digits += 1
    
print("Number of digits = ", digits)
    
