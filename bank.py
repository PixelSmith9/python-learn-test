def show_balance(balance):
    print(f"\n💼 Your balance is: ${balance:.2f}\n")
    return balance


def put_money(balance):
    try:
        add_m = float(input("💵 Enter the amount you want to add: $"))
        if add_m <= 0:
            print("❌ Please enter a positive number.")
        else:
            balance += add_m
            print(f"✅ ${add_m} has been added to your balance.\n")
            
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    return balance


def send_money(balance):
    receiver = input("📨 Enter recipient's name: ").strip()
    if not receiver:
        print("You can't type empty string")
        return balance

    try:
        send_m = float(input(f"💸 How much would you like to send to {receiver}? $"))

        if send_m <= 0:
            print("❌ Please enter a positive number.")

        elif send_m > User_Balance:
            print("❌ Transaction failed: Your balance is low.")

        else:
            balance -= send_m
            print(f"✅ ${send_m:.2f} has been send to the {receiver}")

    except ValueError:
         print("❌ Invalid input. Please enter a number.")    

    return balance
    


User_Balance = 0
is_running = True

while is_running:
    print("=" * 40)
    print("|{:^38}|".format("💰 WELCOME TO PYTHON BANK 💰"))
    print("=" * 40)
    print("| {:<2} {:<33} |".format("1.", "Show Balance"))
    print("| {:<2} {:<33} |".format("2.", "Add Money"))
    print("| {:<2} {:<33} |".format("3.", "Send Money"))
    print("| {:<2} {:<33} |".format("4.", "Exit"))
    print("=" * 40)

    try:
        choose = int(input("Please Choose Your Need: (1 - 4): "))
    except ValueError:
         print("❌ Invalid input. Please enter a number.")    


    if choose == 1:
        show_balance(User_Balance)
    
    elif choose == 2:
        User_Balance = put_money(User_Balance)
    
    elif choose == 3:
        User_Balance = send_money(User_Balance)
    
    elif choose == 4:
        is_running = False    
    else :
        print("❌ Invalid choice. Please select a valid option.\n")
print("👋 Thank you for using Python Bank. Goodbye!")