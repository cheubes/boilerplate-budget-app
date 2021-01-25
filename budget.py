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
        if self.check_funds(amount) :
            self.ledger.append({'amount':-amount, 'description':description})
            self.balance -= amount
            return True
        else :
            return False

    def transfer(self, amount, to):
        if self.check_funds(amount) :
            self.ledger.append({'amount':-amount, 'description':f'Transfer to {to.category}'})
            to.deposit(amount, f'Transfer from {self.category}')
            self.balance -= amount
            return True
        else :
            return False

    def check_funds(self, amount):
        if amount > self.balance :
            return False
        else :
            return True

    def get_balance(self):
        return self.balance

    def __str__(self):
        str = self.category.center(30, '*') + '\n'
        for item in self.ledger :
            description = item["description"][:23].ljust(23)
            amount = f'{item["amount"]:7.2f}'
            line = description + amount
            str += f'{line}\n'
        str += f'Total: {self.balance}'
        return str


def create_spend_chart(categories):
    return ''
