import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.")
        print("\n\n")
        print("[지출 목록]".center(70))
        print(f"{'번호':^2} | {'날짜':^10} | {'카테고리':^11} | {'설명':^15} | {'금액':^8}")
        print("-" * 71)

        total =0
        
        for idx, expense in enumerate(self.expenses, 1):
           print(f"{idx:^5}| {expense}")
           total += expense.amount 

        print("-" * 71)
        print(f"{'총 지출':>54} | {total:>8}원")  
        


    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


    
