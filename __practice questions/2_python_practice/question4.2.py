password="qwert123"
entered_password = input("Enter the password to login")
while entered_password != password:
    entered_password = input("wrong password try again")
print("successfull logined")