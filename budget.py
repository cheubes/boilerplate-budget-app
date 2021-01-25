class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount':amount, 'description':description})



def create_spend_chart(categories):
    return ''
