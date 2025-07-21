from personal_finance_tracker import Transaction, FinanceManager
import pytest 


def test_total_income():
    t1 = Transaction(300, "income", "freelance")
    t2 = Transaction(-100, "expense", "rent")
    t3 = Transaction(200, "income", "bonus")

    Manager = FinanceManager()
    Manager.transactions = [t1, t2, t3]

    assert  Manager.total_income() == 500
    
def test_total_expense():
    t1 = Transaction(300, "income", "freelance")
    t2 = Transaction(-100, "expense", "rent")
    t3 = Transaction(200, "income", "bonus")
    t4 = Transaction(-200, "expense", "bonus")
    
    Manager = FinanceManager()
    Manager.transactions = [t1, t2, t3, t4]
    
    assert Manager.total_expenses() == 300
  
def test_check_balance():
    t1 = Transaction(300, "income", "freelance")
    t2 = Transaction(-100, "expense", "rent")
    t3 = Transaction(200, "income", "bonus")
    t4 = Transaction(-200, "expense", "bonus")
    
    Manager = FinanceManager()
    Manager.transactions = [t1, t2, t3, t4]
    
    assert Manager.check_balance() == 200

    
  
 
  
  
