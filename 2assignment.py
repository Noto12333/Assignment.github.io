import os


class MiniBank:
    mainUserInfo = {}
    USER_DATA_FILE = "user_data.txt"

    def __init__(self):
        self.load_user_data()

    def load_user_data(self):
        if os.path.exists(self.USER_DATA_FILE):
            with open(self.USER_DATA_FILE, "r") as file:
                for line in file:
                    user_id, username, passcode, amount = line.strip().split(":")
                    self.mainUserInfo[int(user_id)] = {
                        "r_username": username,
                        "r_passcode": int(passcode),
                        "r_amount": int(amount)
                    }
        else:
            self.mainUserInfo = {}

    def save_user_data(self):
        with open(self.USER_DATA_FILE, "w") as file:
            for user_id, user_info in self.mainUserInfo.items():
                file.write(f"{user_id}:{user_info['r_username']}:{user_info['r_passcode']}:{user_info['r_amount']}\n")

    def first_option(self):
        fuser_input: int = int(input("Press 1 to login:\nPress 2 to register:\nPress 3 to exit: "))
        if fuser_input == 1:
            self.login()
        elif fuser_input == 2:
            self.register()
        elif fuser_input == 3:
            self.exit_app()

    def returnId(self):
        return len(self.mainUserInfo)

    def login(self):
        print("\n\n________This is from login __________\n\n")
        l_username: str = input("Please enter username: ")
        l_passcode: int = int(input("Please enter passcode: "))
        if self.existUser(l_username, l_passcode):
            print("\n\n_______Login Successful________")
            self.menu()
        else:
            print("___User does not exist____")

    def menu(self):
        print("\n\n_________This is from application___________\n\n")
        menuInput = int(input(
            "Press 1 to transfer:\nPress 2 to withdraw:\nPress 3 to update user data:\nPress 4 to exit: "))
        if menuInput == 1:
            self.transfer()
        elif menuInput == 2:
            self.withdraw()
        elif menuInput == 3:
            self.update_user_data()
        elif menuInput == 4:
            self.exit_app()

    def transfer(self):
        sender_username = input("Enter your username: ")
        sender_passcode = int(input("Enter your passcode: "))
        if self.existUser(sender_username, sender_passcode):
            sender_id = self.transfreId(sender_username)
            recipient_username = input("Enter transfer username: ")
            recipient_id = self.transfreId(recipient_username)
            if recipient_id is not None:
                amount = int(input(f"Enter amount to transfer to {recipient_username}: "))
                if self.mainUserInfo[sender_id]["r_amount"] >= amount:
                    self.mainUserInfo[sender_id]["r_amount"] -= amount
                    self.mainUserInfo[recipient_id]["r_amount"] += amount
                    self.save_user_data()
                    print(f"Successfully transferred {amount} to {recipient_username}.")
                else:
                    print("Insufficient balance.")
            else:
                print("Recipient not found.")
        else:
            print("Invalid credentials.")

    def withdraw(self):
        username = input("Enter your username: ")
        passcode = int(input("Enter your passcode: "))
        if self.existUser(username, passcode):
            user_id = self.transfreId(username)
            amount = int(input("Enter amount to withdraw: "))
            if self.mainUserInfo[user_id]["r_amount"] >= amount:
                self.mainUserInfo[user_id]["r_amount"] -= amount
                self.save_user_data()
                print(f"Successfully withdrew {amount}. Remaining balance: {self.mainUserInfo[user_id]['r_amount']}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid credentials.")

    def exit_app(self):
        print("Exiting application. Saving user data...")
        self.save_user_data()
        print("Goodbye!")
        exit()

    def update_user_data(self):
        print("\n\n_________Update User Data___________\n\n")
        updateUserInput: int = int(input("Press 1 to change name:\nPress 2 to change passcode:\nPress 3 to update amount: "))
        if updateUserInput == 1:
            self.update_username()
        elif updateUserInput == 2:
            self.update_passcode()
        elif updateUserInput == 3:
            self.update_amount()

    def update_amount(self):
        updateUsername: str = input("Please enter your username: ")
        updatePasscode: int = int(input("Please enter your passcode: "))
        if self.existUser(updateUsername, updatePasscode):
            transferId = self.transfreId(updateUsername)
            newAmount: int = int(input("Enter amount to update: "))
            self.mainUserInfo[transferId]["r_amount"] += newAmount
            self.save_user_data()
            print("Amount updated successfully:", self.mainUserInfo[transferId]["r_amount"])
        else:
            print("Invalid user credentials.")

    def update_passcode(self):
        oldUsername: str = input("Please enter your username: ")
        oldPasscode: int = int(input("Please enter your current passcode: "))
        if self.existUser(oldUsername, oldPasscode):
            transferId = self.transfreId(oldUsername)
            newPasscode: int = int(input("Please enter new passcode: "))
            self.mainUserInfo[transferId]["r_passcode"] = newPasscode
            self.save_user_data()
            print("Passcode updated successfully.")
        else:
            print("Invalid user credentials.")

    def update_username(self):
        oldUsername: str = input("Please enter your username: ")
        oldPasscode: int = int(input("Please enter your current passcode: "))
        if self.existUser(oldUsername, oldPasscode):
            transferId = self.transfreId(oldUsername)
            newUsername: str = input("Please enter new username: ")
            self.mainUserInfo[transferId]["r_username"] = newUsername
            self.save_user_data()
            print("Username updated successfully.")
        else:
            print("Invalid user credentials.")

    def transfreId(self, username):
        for user_id, user_data in self.mainUserInfo.items():
            if user_data["r_username"] == username:
                return user_id
        return None

    def existUser(self, l_username, l_passcode):
        for user_id, user_data in self.mainUserInfo.items():
            if user_data["r_username"] == l_username and user_data["r_passcode"] == l_passcode:
                return True
        return False

    def register(self):
        print("_________This is from register ________")
        r_username: str = input("Please enter username to register: ")
        r_passcode1: int = int(input("Please enter passcode to register: "))
        r_passcode2: int = int(input("Please enter passcode again to confirm: "))
        r_amount: int = int(input("Please enter amount: "))
        if r_passcode1 == r_passcode2:
            user_id = self.returnId()
            self.mainUserInfo[user_id] = {
                "r_username": r_username,
                "r_passcode": r_passcode1,
                "r_amount": r_amount
            }
            self.save_user_data()
            print("Registration Successful!")
        else:
            print("Passcodes do not match. Please try again.")


if __name__ == "__main__":
    miniBank = MiniBank()
    while True:
        miniBank.first_option()    