import sys
from datetime import datetime
from expenseTracker import ExpenseTracker # type: ignore
class  Expense:
    data = { }

    def __init__(self):
        self.tracker :ExpenseTracker = ExpenseTracker()
        print("Personal Expense Tracker")

    def first_option(self):
        f_userInput:str = int(input(" 1. Add New Expense \n 2. View All Expenses \n 3. View Total Expenses \n 4. Delete an Expanse \n 5. Exit \n Enter your option :"))  
        if f_userInput == 1:
            self.new_expense()

        elif f_userInput == 2:
            self.tracker.view_allExpense()
        
        elif f_userInput == 3:
            self.tracker.view_totalExpense()

        elif f_userInput == 4:
            self.tracker.delete_anExpense()

        elif f_userInput == 5:
            self.exit_program() 
    
    def new_expense(self):
        print("\n\n______This is from New Expense________\n")
        expDescription: str = input("Enter Expense Description: ")
        try:
            expAmount: float = float(input("Enter amount spent: "))
        except ValueError:
            print("\n\n\"Invalid input. Please enter a numeric value for the amount.\"")
            return

        if expAmount < 0:
            print("\n\n\"Invalid amount. Please enter a positive number.\"")
            return

        expDate: str = input("Enter date (YYYY-MM-DD): ")
        checkFormat = self.validate_date(expDate)
        if not checkFormat:
            print("\n\"Invalid date format. Please enter in date format (YYYY-MM-DD)\"")
            return
        expDate = str(expDate)
        self.tracker.save_expense(expDescription,expAmount,expDate)
        print("Expense added successfully")


    def validate_date(self,date_string):
        """
        Validates the date string in the format 'YYYY-MM-DD'.
        Returns a datetime object if valid, otherwise raises an error.
        """
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')  # Parse the string into a datetime object
            return date_obj
        
        except:
            return        
        


    def exit_program(self):
         print("Thank you for using the program. Goodbye!")
         sys.exit(0)


if __name__ == "__main__":
    expense :Expense = Expense()

    while True:
        expense.first_option()
    
        