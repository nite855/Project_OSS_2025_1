import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.limit = int(input("예산을 입력하세요 > "))
        self.currentBudget = self.limit
        self.dangerPoint = int(input("예산의 몇 %까지 사용할 예정입니까?(%는 제외하고 입력해주세요) > "))

        self.flag = False

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

    def limit_count(self,amount):
        self.currentBudget -= amount

        usedper = self.currentBudget/self.limit * 100
        print(usedper)
        if usedper <= self.dangerPoint :
            print(f"예산이 {self.dangerPoint}% 이하 남았습니다. 더 이상의 소비는 제한됩니다")
            self.flag = True            
        elif usedper <=10 :
            print(f"예산이 10% 남았습니다! 소비를 아껴주세요!\n(남은 금액 : {self.currentBudget})")
        elif usedper <=25 :
            print(f"예산의 75%를 사용했습니다. 주의하세요!\n(남은 금액 : {self.currentBudget})")
        elif usedper <=50 :
            print(f"예산의 50%를 사용했습니다.")

    def cheak_consume(self, amount):
        if(self.currentBudget < amount) :
                print("예산이 부족합니다.")
                return True
        if(self.flag) :
            answer = input("예산이 한계입니다. 정말로 사용하시겠습니까? (Y/N)")
            return False if( answer == 'Y' or answer == 'y') else True
            
        
