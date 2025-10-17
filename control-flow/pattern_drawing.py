number = int(input("Enter the size of the pattern:"))
row = 1
while row <= number:
    for i in range(number):
        print("*", end=" ")
    row += 1
    print()