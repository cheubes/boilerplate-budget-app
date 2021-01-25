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

    def transfer(self, amount, to):
        self.ledger.append({'amount':-amount, 'description':f'Transfer to {to.category}'})
        to.deposit(amount, f'Transfer from {self.category}')
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

def create_spend_chart(categories):
    return ''
