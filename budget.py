class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount':amount, 'description':description})
        self.balance += amount
        return True

    def withdraw(self, amount, description = ''):
        self.ledger.append({'amount':-amount, 'description':description})
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

def create_spend_chart(categories):
    return ''
