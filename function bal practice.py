'''balance = int(input("Enter balance: "))
def check_balance():
    print("Available balance:", balance)
def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction successful")
        print("Withdraw amount:", amount)
        print("Remaining balance:", balance)
    else:
        if amount>=3000:
            print("Insufficient balance")
def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful")
    print("Current balance:", balance)
def atm():
    while True:
        count+=1
        while count<=3:
            if pin==1234:
                print("\n1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    check_balance()
                elif choice == 2:
                    withdraw()
                elif choice == 3:
                    deposit()
                elif choice == 4:
                    print("Thank you, visit again!")
                    break
                else:
                    print("Invalid choice")
            else:
                count+=1
                print(f"{count+1} chance")
                print("wrong pin")
                break
atm()'''


balance = int(input("Enter balance: "))

def check_balance():
    print("Available balance:", balance)

def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction successful")
        print("Withdraw amount:", amount)
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful")
    print("Current balance:", balance)

def atm():
    count = 0

    while count < 3:
        pin = int(input("Enter PIN: "))

        if pin == 1234:
            while True:
                print("\n1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    check_balance()
                elif choice == 2:
                    withdraw()
                elif choice == 3:
                    deposit()
                elif choice == 4:
                    print("Thank you, visit again!")
                    return
                else:
                    print("Invalid choice")
        else:
            count += 1
            print("Wrong PIN")
            print(f"{3 - count} chances left")
            
    print("Card blocked")
    
atm()