class Incentive:
    def __init__(self, type, amount, recipients):
        self.type = type
        self.amount = amount
        self.recipients = recipients
        
def main():
    financial_incentive = Incentive("financial", 5000, "employees")
if __name__ == '__main__':
    main()