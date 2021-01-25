import math

class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.spent = 0

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount':amount, 'description':description})
        self.balance += amount
        return True

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) :
            self.ledger.append({'amount':-amount, 'description':description})
            self.balance -= amount
            self.spent += amount
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
    total_spent = 0
    for category in categories :
        total_spent += category.spent
    category_names = []
    percentages_spent = []
    for category in categories :
        category_names.append(category.category)
        percentages_spent.append(math.floor(category.spent/total_spent*10)*10)
    print(percentages_spent)

    spend_chart = 'Percentage spent by category\n'

    for i in range(100, -1, -10) :
        spend_chart += f'{i:3}|'
        for p in percentages_spent :
            if p >= i :
                spend_chart +=  ' o '
            else :
                spend_chart +=  '   '
        spend_chart += ' \n'
    spend_chart += '    '
    for p in percentages_spent :
        spend_chart += '---'
    spend_chart += '-\n'

    max_len = 0
    for name in category_names :
        if len(name) > max_len :
            max_len = len(name)
    for i in range(0, max_len) :
        spend_chart += '    '
        for name in category_names :
            if i < len(name) :
                spend_chart += f' {name[i]} '
            else :
                spend_chart += '   '
        spend_chart += ' '
        if i != max_len - 1 :
            spend_chart += '\n'

    return spend_chart
