from datetime import datetime
class Acquisition:
    def __init__(self, target_company, acquiring_company, price):
        self.target_company = target_company
        self.acquiring_company = acquiring_company
        self.price = price
        self.date = datetime.now()

    def execute(self):
        self.target_company.is_acquired = True
        self.target_company.acquirer = self.acquiring_company
        self.target_company.acquisition_price = self.price
def main():
    print(666)
if __name__ == '__main__':
    main()