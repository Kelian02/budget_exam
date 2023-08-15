# This is a sample Python script.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from manager import BudgetManager
from kivy.properties import StringProperty


class BoxLayoutExample(BoxLayout):
    pass


class BudgetApp(App):
    solde_text = StringProperty()
    def build(self):
        self.budget_manager = BudgetManager()

    def add_expense(self, montant, description ,categorie):
        float_montant = float(montant)
        self.budget_manager.add_expense(montant=float_montant, categorie=categorie,description=description)
        self.update_solde_text()
        print("Dépense ajoutée!")

    def add_income(self, montant, description):
        float_montant = float(montant)
        self.budget_manager.add_income(montant=float_montant, description=description)
        self.update_solde_text()
        print("Revenu ajouté!")

    def show_budget(self, instance):
        self.update_solde_text()

    def show_all_incomes(self):
        self.solde_text = f"{self.budget_manager.show_incomes()}"
    def show_all_expenses(self):
        self.solde_text = f"{self.budget_manager.show_expenses()}"

    def update_solde_text(self):
        self.solde_text = f"Solde : {self.budget_manager.show_budget():.2f}€"


if __name__ == "__main__":
    BudgetApp().run()
