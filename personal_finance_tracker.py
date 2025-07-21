from datetime import datetime

class Transcations:
  # this takes transcation data like amount, type of transction; income or expenses, 
  # Category; rent or grocesis or entertainment, date
  def __init__(self, amount, type_of_transaction, category):
    self.amount = amount
    self.type = type_of_transaction
    self.category = category
    self.date = datetime.now()
    
  def total_income(self):
    pass
  
  def total_expenses(self):
    pass
  
  def balance(self):
    pass

class FinanceManager:
  #this keeps track of all action transcations and manager the finance
  def __init__(self):
    pass
    
  def user_input(self):
    pass
  
  def add_income(self):
    pass
  
  def add_expenses(self):
    pass
  
  def add_to_category(self):
    pass
  
  def show_summary(self):
    pass


class FileHandler:
  #this handles the file or csv path of the user
  def __init__(self):
    pass
  
  def load_file(self):
    pass
  
  def save_file(self):
    pass

class CliController:
  #this handles how to the user interracters with the cli
  def __init__(self):
    pass
  
  def menu(self):
    pass
  
  def user_choice(self):
    pass
  
  def run(self):
    pass