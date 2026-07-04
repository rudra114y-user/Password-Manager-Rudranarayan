import random
import string

passwords = {}

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Generate Strong Password")
    print("4. Save Passwords")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account = input("Enter Account Name: ")
        password = input("Enter Password: ")
        passwords[account] = password
        print("Password Added Successfully!")

    elif choice == "2":
        if passwords:
            print("\nSaved Accounts:")
            for account, password in passwords.items():
                print(f"{account}: {password}")
        else:
            print("No passwords stored.")

    elif choice == "3":
        strong_password = generate_password()
        print("Generated Password:", strong_password)

    elif choice == "4":
        with open("passwords.txt", "w") as file:
            for account, password in passwords.items():
                file.write(f"{account}:{password}\n")
        print("Passwords Saved to File!")

    elif choice == "5":
        print("Exiting Password Manager...")
        break

    else:
        print("Invalid Choice!")