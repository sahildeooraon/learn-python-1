a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=input("what operation you want to do +,-,*,/ \n")
match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
