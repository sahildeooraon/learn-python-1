#match cases
 
a=int(input("Select a lucky draw no. from 1 to 200\n"))
match a:
    case 1:
        print("you won the 1st price.")
    case 10:
        print("you won the 2nd price.")
    case 50:
        print("you won the 3rd price.")
    case 150:
        print("you won the 4th price.")
    case _:
        print("sorry better luck next time.")