class ATM:
    balance = 1000
    chance = 3
    restart = "y"
    print("Welcome to Python Bank")
    while chance >= 0:
        print("Please enter your PIN : ")
        id = input()
        if id == '9999':
            while restart not in ('N', 'N', 'No', 'NO', 'no'):
                print("Welcome")
                print("Choice any option")
                print("1. Check your account balance \t "
                      "2. Withdraw funds \t"
                      "3. Deposit Money \t "
                      "4. SMS account details \t"
                      "5. Exit")
                choice = int(input("choice : "))

                if choice == 1:
                    print("Your account balance is : ", balance)
                    print("Go back (y/n): ")
                    restart = input()
                    if restart == ('n', 'N', 'No', 'NO', 'no'):
                        print("Thank you")
                        break

                elif choice == 2:
                    print("Enter withdraw amount: ")
                    withdraw = int(input())
                    balance = balance -withdraw
                    print("Your withdraw money: ", withdraw)
                    print("Your new balance is : ", balance)
                    print("Go back (y/n): ")
                    restart = input()
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        print("Thank you")
                        break

                elif choice == 3:
                    print("How much do you want to deposit :")
                    deposit = int(input())
                    balance = balance + deposit
                    print("Your new balance is : ", balance)
                    print("Go back (y/n): ")
                    restart = input()
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        print("Thank you")
                        break

                elif choice == 4:
                    print("Enter your mobile phone")
                    number = input()
                    if number == "123456789":
                        print("SMS sent ")
                    else:
                        print("This is not a valid phone number")
                        print("Go back (y/n)")
                if restart in ('n', 'N', 'No', 'NO', 'no'):
                    print("Thank you")
                    break


                elif choice == 5:
                    print("Thank you, have a nice day")
                    break
                else:
                    print("Please enter a valid option :")
                    restart = 'y'
        elif id != '1234':
            print("Please enter a valid PIN: ")
            chance = chance -1
            if chance == 0:
                print("No more tries ")
                break
        elif restart == 'n':
            break