#Tables generator

n = int(input("Enter a Number: "))

count = 1
while count <= 10:
    product = n * count
    print(n, "x", count, "=" , product)
    count = count + 1