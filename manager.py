from depense import Expense
from categorie import Category
from budget import Budget
from revenu import Income



class BudgetManager:
    def __init__(self):
        self.budget_actuel = Budget(solde=500)
        self.all_expenses = []
        self.all_incomes = []
        self.all_categories = []
    def add_expense(self,montant= 1,categorie='Loisir',description="Unknown"):
        expense = Expense(montant,categorie,description)
        self.budget_actuel.solde -= expense.montant
        expense_tab = []
        expense_tab.append(expense.montant)
        expense_tab.append(expense.categorie)
        expense_tab.append(expense.description)
        self.all_expenses.append(expense_tab)
    def add_income(self, montant = 1, description="Unknown"):
        income = Income(montant,description)
        self.budget_actuel.solde += income.montant
        income_tab = []
        income_tab.append(income.montant)
        income_tab.append(income.description)
        self.all_incomes.append(income_tab)
    def add_category(self, categorie):
        category = Category(categorie)
        self.all_categories.append(category)
    def show_budget(self):
        return self.budget_actuel.solde
    def show_categories(self):
        return self.all_categories
    def show_incomes(self):
        string = ''
        for all_income_info in self.all_incomes:
            for specific_info in all_income_info:
                string += str(specific_info) + ' '
            string+= '\n'
        return string
    def show_expenses(self):
        string = ''
        for all_expense_info in self.all_expenses:
            for specific_info in all_expense_info:
                string += str(specific_info) + ' '
            string += '\n'
        return string