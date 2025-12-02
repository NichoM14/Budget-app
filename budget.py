class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True
        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]  # max 23 chars
            amount = f"{item['amount']:>7.2f}"      # right-align, 2 decimals, max 7 chars
            items += f"{description:<23}{amount}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total_withdraw = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total_withdraw += -item["amount"]
        spent.append(total_withdraw)
        
    total_spent = sum(spent)
    percentages = [int(s / total_spent * 100 // 10 * 10) for s in spent]
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        row = f"{i:>3}|"
        for perc in percentages:
            row += " o " if perc >= i else "   "
        chart += row + " \n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     " 
        for cat in categories:
            if i < len(cat.name):
                row += f"{cat.name[i]}  "
            else:
                row += "   "
        chart += row + "\n"
    

    return chart.rstrip("\n")
