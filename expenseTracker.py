import pymongo # type: ignore 
from bson.objectid import ObjectId # type: ignore
class ExpenseTracker:
    def __init__(self):
        try:
            self.connection = pymongo.MongoClient("localhost",27017)
            self.database = self.connection["expenseDB"]
            self.collection =  self.database["mycol_1"]
            print("Connection success !")
        except Exception as error:
            print(error)

    def save_expense(self, expDescription, expAmount, expDate):
        data = {"Description": expDescription, "Amount": expAmount, "Date": expDate}
        try:
            result = self.collection.insert_one(data)
            print(f"Expense saved: {result.inserted_id}")
        except Exception as error:
            print(f"Error saving expense: {error}")

    def view_allExpense(self):
        try:
            result = self.collection.find()
            for my_dict in result:
                pure_string = ", ".join(f"{key}:{value}" for key, value in my_dict.items())
                print(pure_string)
        except Exception as err:
            print(err)        

    def view_totalExpense(self):
        try:
            result = self.collection.find()
            total_data = []
            for data in result:
                total_data.append(data)

            total_amount = sum(float(item['Amount']) for item in total_data)
            print(f"Total Expense : {total_amount}")  
        except Exception as err:
            print(err) 


    def delete_anExpense(self):
        try:
            
            deleteId: str = input("Enter the ID of expense to delete: ")
            query = {"_id": ObjectId(deleteId)}
    
            result = self.collection.delete_one(query)
            if result.deleted_count > 0:
                print("Expense deleted successfully!\n")
            else:
                print("No expense found with the provided ID.\n")

        except Exception as error:
            print(f"Error: {error}")

