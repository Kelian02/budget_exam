class Income:
    def __init__(self,montant,description):
        self.montant = montant
        self.description = description

    def __str__(self):
        return f"Income description: {self.description}, montant: {self.montant}"

