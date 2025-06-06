import datetime
from expense import Expense


class Budget:
    def __init__(self):
        self.expenses = []
        self.category = ["식비", "교통비", "주거통신"," 유흥", "기타"]

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


    def list_category_expenses(self) :
    #카테고리는 숫자와 사전형을 연결되있어 그 값을 이용하기 위한 변수
       for output in range(1,5) :
            print("="*20)
            print(f"{self.category[output]} 항목")
            for idx, expense in enumerate(self.expenses, 1):# expenses 리스트를 순회
                if int(expense.category) == output:  # 특정 카테고리와 비교
                    print(expense)
            print()
            

            
    def print_category(self) :
        for i in range(0,len(self.category)):
            print(f" {i+1} : {self.category[i]}", end = '  ')

