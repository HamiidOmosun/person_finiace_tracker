from datetime import datetime
import csv

class Transaction:
  # this takes transcation data like amount, type of transction; income or expenses, 
  # Category; rent or grocesis or entertainment, date
  def __init__(self, amount, type_trans, category,date=None):
    self.amount = amount
    self.type = type_trans
    self.category = category
    self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") if date else datetime.now()
class FinanceManager:
  #this keeps track of all action transcations and manager the finance
  def __init__(self):
    self.transactions = []
  
  def total_income(self):
    total = 0
    for t in self.transactions:
      if t.type == "income":
        total += t.amount 
    return total
  
  def total_expenses(self):
    expenses = 0
    for e in self.transactions:
      if e.type == "expense":
        expenses += abs(e.amount)
    return expenses
  
  def check_balance(self):
    income = self.total_income()
    expense = self.total_expenses()
    balance = income - expense
    return balance
  
  def filter_transactions(self):
    user_trans = input("Search by (type of transaction or Category)").lower().strip()
    #use a for loop to iterate in a list or check items in list
    if user_trans == 'type of transaction':
      type_value =input("Enter Income or Expense: ")
      
      filtered = []
      
      for transaction in self.transactions:
          if transaction.type == type_value:
            filtered.appened(type_value)
      return filtered
    
    elif user_trans == 'category':
      type_value = input("Enter any of the following(rent, entertainment, food,"
                        "\nclothes, salary, investment: )")
      
      filtered = []
      
      for transaction in self.transactions:
        if transaction == type_value:
          filtered.append(type_value)
      return filtered
    
    else:
      return False
          
  def add_transaction(self, amount, type_trans, category):
    #ask user for transaction details 
    #append to list of transcation
    if amount <= 0:
        print("Invalid amount")
        return False

    if type_trans not in ['income', 'expense']:
        print("Must be 'income' or 'expense'")
        return False

    if category not in ['rent', 'entertainment', 'food', 'clothes', 'salary', 'investment']:
        print("Must be a valid category")
        return False
    
    transaction = Transaction(amount, type_trans, category)
    
    self.transactions.append(transaction)
      
  def show_summary(self):
    # Ask user if they want to see the summary
    choice_user = input("Would you like to see a summary of your transactions? (yes/no): ").strip().lower()
    
    if choice_user != 'yes':
        print("Summary cancelled.")
        return

    # If no transactions exist
    if not self.transactions:
        print("No transactions to summarize.")
        return #using just return stops the function from runing any futher
 
    print("\nYour Transaction Summary:")
    for txn in self.transactions:
        print({
            "amount": txn.amount,
            "type of transaction": txn.type,
            "category": txn.category,
            "date": txn.date.strftime("%Y-%m-%d %H:%M:%S")
        })

class FileHandler:
  def __init__(self, file):
    self.file = file
    self.transaction = []

  def load_file(self):
    try:
      with open(self.file, "r") as file:
        reader = csv.DictReader(file)
        self.transactions = [Transaction(
                      int(row["amount"]),
                      row["type of transaction"],
                      row["category"],
                      row["date"])
                          for row in reader]

    except FileNotFoundError:
      print("No file...")
  
  def save_file(self, transactions):
      with open(self.file, "w", newline="") as file:
          fieldnames = ["amount", "type of transaction", "category", "date"]
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          writer.writeheader()
          for txn in transactions:
              writer.writerow({
                  "amount": txn.amount,
                  "type of transaction": txn.type,
                  "category": txn.category,
                  "date": txn.date.strftime("%Y-%m-%d %H:%M:%S")
              })

class CliController:
  #this handles how to the user interracters with the cli
  def __init__(self):
    self.controller = FinanceManager()
  
  def collect_transactions(self):
    amount = int(input("Enter amount: ").strip())
    type_trans = input("Enter transcation type (income or Expense)").lower().strip()
    category = input("Enter Category(rent, entertainment, food, clothes, salary, investment: )").lower().strip()

    return amount, type_trans, category
  
  def menu(self):
    print("\n====== Finance-Tracker =====")
    print("1. Add Transaction")
    print("2. Show sumarry")
    print("3. Check Balance")
    print("4. check total income")
    print("5. check total expenses")
    print("6. filter transaction")
    print("7. Load csv")
    print("8. Exit")
  
  def user_choice(self):
    self.save = FileHandler("transactions.csv")
    self.save.load_file()
    while True:
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            result = self.collect_transactions()
            if result:
              amount, type_trans, category = result
              self.controller.add_transaction(amount, type_trans, category)
              self.save.save_file(self.controller.transactions)
            else:
              print("Print Transaction Entry Cancelled")
              return False
        elif choice == "2":
            self.controller.show_summary()
        elif choice == "3":
            self.transaction
            if self.transaction:
              print(self.controller.check_balance())
        elif choice == "4":
            transaction = self.transaction
            if transaction:
              print(self.controller.total_income())
        elif choice == "5":
            transaction = self.transaction
            if transaction:
              print(self.controller.total_expenses())
        elif choice == "6":
            self.controller.filter_transactions()
        elif choice == "7":
            self.controller.transactions = self.save.transactions
            print("Transactions successfully loaded.")
        elif choice == "8":
          print("You exited the menu ")
          break
        else:
            print("Invalid choice. Try again.")

  def run(self):
      while True:
        self.menu()
        should_continue = self.user_choice()
        if should_continue is False:
            print("Goodbye! Exiting the program.")
            break
          
          
if __name__ == "__main__":
  user = CliController()
  user.run()