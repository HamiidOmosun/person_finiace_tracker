from datetime import datetime

class Transaction:
  # this takes transcation data like amount, type of transction; income or expenses, 
  # Category; rent or grocesis or entertainment, date
  def __init__(self, amount, type_trans, category):
    self.amount = amount
    self.type = type_trans
    self.category = category
    self.date = datetime.now()
    
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
    #use a for loop to iterate in a list or check items in list
    if self.user_trans == 'type of transaction':
      type_value =input("Enter Income or Expense: ")
      
      filtered = []
      
      for transaction in self.transactions:
          if transaction == type_value:
            filtered.appened(type_value)
      return filtered
    
    elif self.user_trans == 'category':
      type_value = input("Enter any of the following(rent, entertainment, food, \
                        clothes, salary, investment: )")
      
      filtered = []
      
      for transaction in self.transactions:
        if transaction == type_value:
          filtered.append(type_value)
      return filtered
    
    else:
      return False
          
  def add_transaction(self):
    #ask user for transaction details 
    #append to list of transcation
    amount = int(input("Enter amount: ").strip())
    type_trans = input("Enter transcation type (income or Expense)").lower().strip()
    category = input("Enter Category(rent, entertainment, food, clothes, salary, investment: )").lower().strip()
      
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
  #this handles the file or csv path of the user
  def __init__(self,file, filename="transactions.csv"):
    self.filename = filename
  
  def load_file(self):
    #open the file with "r" to read the content of the file
    with open(self.filename, "r") as file:
      transaction = []
    #use a for lop to iterate over each line
      for line in file:
    #clean the line and split it by commas
        parts = line.strip().split(',')
    #assign values form split lines
        amount = float(parts[0])
        type_trans = parts[1]
        category = parts[2]
        date = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S.%f")
    #rebuild transaction list 
        transaction = Transaction(amount, type_trans, category)
        transaction.date = date
    #add transaction to list 
        self.transactions.append(transaction)
    return transaction
  
  def save_file(self, transactions):
    with open(self.filename, "w") as file:
        for txn in transactions:
            line = f"{txn.amount},{txn.type},{txn.category},{txn.date}\n"
            file.write(line)

class CliController:
  #this handles how to the user interracters with the cli
  def __init__(self):
    self.controller = FinanceManager()
  
  def collect_transactions(self, amount, type_trans, category):
    pass
  
  def menu(self):
    pass
  
  def user_choice(self):
    pass
  
  def run(self):
    pass