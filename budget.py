class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount':amount, 'description':description})
        return True

    def withdraw(self, amount, description = ''):
        self.ledger.append({'amount':-amount, 'description':description})
        return True


def create_spend_chart(categories):
    return ''
