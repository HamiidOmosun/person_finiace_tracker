from datetime import datetime

class Transaction:
  # this takes transcation data like amount, type of transction; income or expenses, 
  # Category; rent or grocesis or entertainment, date
  def __init__(self, amount, type_of_transaction, category):
    self.amount = amount
    self.type = type_of_transaction
    self.category = category
    self.date = datetime.now()
    
class FinanceManager:
  #this keeps track of all action transcations and manager the finance
  def __init__(self):
    self.transactions = []
  
  def total_income(self):
    pass
  
  def total_expenses(self):
    pass
  
  def check_balance(self):
    pass
  
  def filter_transaction(self, type, category):
    pass
  
  def add_transaction(self):
    pass
      
  def show_summary(self):
    pass


class FileHandler:
  #this handles the file or csv path of the user
  def __init__(self, filename="transactions.csv"):
    self.filename = filename
    self.data = []
    pass
  
  def load_file(self):
    pass
  
  def save_file(self):
    pass

class CliController:
  #this handles how to the user interracters with the cli
  def __init__(self):
    self.controller = FinanceManager()
  
  def collect_transactions(self, amount, type_of_transaction, category):
    pass
  
  def menu(self):
    pass
  
  def user_choice(self):
    pass
  
  def run(self):
    pass