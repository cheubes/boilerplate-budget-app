class Category:
    category = ''
    ledger = []

    def __init__(self, category):
        self.category = category

    def deposit(self, amount, description):
        self.ledger.append({'amount':amount, 'description':description})



def create_spend_chart(categories):
    return ''
