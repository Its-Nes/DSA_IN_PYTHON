def strings():
    s=input("Enter a string: ")
    print(len(s))
    print(s.upper())
    print(s.lower())
    print(s[::-1])

    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

strings()