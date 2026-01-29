n = int(input("Enter a number: "))

# square of original number
square1 = n * n

# reverse of the number
rev = int(str(n)[::-1])

# square of reversed number
square2 = rev * rev

# reverse of square2
rev_square2 = int(str(square2)[::-1])

if square1 == rev_square2:
    print(n, "is an Adam Number")
else:
    print(n, "is NOT an Adam Number")
