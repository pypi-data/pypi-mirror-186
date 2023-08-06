from cpanlp.entity.entity import *
class Stakeholder:
    def __init__(self, name, interests,power):
        self.name = name
        self.interests = interests
        self.power = power
        self.contact_info = ""
        self.concern=""
        self.suggest=""
class Government(Stakeholder):
    def __init__(self, name, interests,power, government_type):
        super().__init__(name, interests,power)
        self.government_type = government_type
    def regulate_company(self, company):
        # Code to regulate the company
        pass
    def make_policy(self, policy):
        # Code to make a policy
        pass
class Media(Stakeholder):
    def __init__(self, name, interests,power):
        super().__init__(name, interests,power)
        self.media_type = ""
        self.publish=""
class Public(Stakeholder):
    def __init__(self, name, interests,power):
        super().__init__(name, interests,power)
        self.voice=""
class RatingAgency(Stakeholder):
    def __init__(self, name, interests,power):
        super().__init__(name, interests,power)
        self.ratings = {}
    def assign_rating(self, company, rating):
        self.ratings[company.name] = rating
class Bank(Stakeholder):
    def __init__(self, name, interests,power):
        super().__init__(name, interests,power)
        self.loans = {}
    def grant_loan(self, company, amount):
        self.loans[company.name] = amount
        

def main():
    customer = Stakeholder("Jane", "product quality and customer service",6)
    b=Media("xinhua","合作",10)
    agency = RatingAgency("Moody's","makemoney",10)
    agency.assign_rating(LLC("huawei","technology",10000),"A")
    print(agency.ratings)
if __name__ == '__main__':
    main()