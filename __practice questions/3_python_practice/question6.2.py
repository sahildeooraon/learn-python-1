a=str(input('type a  palindrome\n').lower())
if a==a[::-1]:
    print("yes it is a palindrome.")
else:
    print("No it is not a palindrome.")