# Password Manager
def view():
    print("\nStored Passwords:")
    try:
        with open("pwd.txt", "r") as f:
            for line in f.readlines():
                name, pwd = line.strip().split("|")
                print(f"Account: {name} | Password: {pwd}")
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("pwd.txt", "a") as f:
        f.write(f"{name}|{pwd}\n")
        
    print(f"Password stored successfully.")

input("Press Enter to set up your password manager...")
master = input("Enter your master password: ")
passwords = {}
if master == "admin123":
    print("Access granted. Welcome back!")
    while True:
        print("\nPassword Manager Menu:")
        print("1. Store a new password")
        print("2. View stored passwords")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            continue
else:
    print("Wrong Password!")
    
