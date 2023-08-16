import unittest
from manager import BudgetManager


class TestBudgetManager(unittest.TestCase):
    initial_budget = 1500

    def test_show_budget(self):
        budget_manager = BudgetManager()
        self.assertEqual(budget_manager.show_budget(), self.initial_budget)

    def test_add_expense(self):
        budget_manager = BudgetManager()
        montant = 50
        budget_manager.add_expense(montant=montant)
        self.assertEqual(budget_manager.show_budget(), self.initial_budget-montant)

    def test_add_income(self):
        budget_manager = BudgetManager()
        montant = 150
        budget_manager.add_income(montant=montant)
        self.assertEqual(budget_manager.show_budget(), self.initial_budget-montant)
