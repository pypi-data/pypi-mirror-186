class Policy:
    def __init__(self, name, policy_type, purpose):
        self.name = name
        self.policy_type = policy_type
        self.purpose = purpose
    def implement_policy(self):
        # Code to implement the policy
        pass
    def evaluate_effectiveness(self):
        # Code to evaluate the effectiveness of the policy
        pass
class DividendPolicy(Policy):
    def __init__(self, name,dividend_rate ,policy_type, purpose):
        super().__init__(name, policy_type, purpose)
        self.dividend_rate = dividend_rate

    def get_dividend_rate(self):
        return self.dividend_rate
    
    def set_dividend_rate(self, dividend_rate):
        self.dividend_rate = dividend_rate
        
    def calculate_dividend(self, net_income):
        return net_income * self.dividend_rate
    
    
def main():
    print(123)
    policy1 = DividendPolicy("Deloitte",0.2,"福利","incentive")
    print(policy1.calculate_dividend(100000)) # prints 7000
if __name__ == '__main__':
    main()