class OldRegime:
    """
    Calculate the income tax based on old tax rate brackets in 2007
    """
    def __init__(self,income):
        self.income = income
        self.tax = 0

    def calculate_first_bracket(self, income):
        # for income in $0-$2,220, the tax is 2.5% times the amount
        self.tax += income*0.025
        return self.tax

    def calculate_second_bracket(self, income):
        # for income in $2,220-$4,440, the tax is 3% times the amount exceding $2220 plus $56
        self.tax += self.calculate_first_bracket(2220)
        self.tax += (income - 2220)*0.03
        return self.tax

    def calculate_third_bracket(self, income):
        # for income in $4,440-$6660, the tax is 4% times the amount exceding $4,440 plus $123
        self.tax += self.calculate_second_bracket(4440)
        self.tax += (income - 4440)*0.04
        return self.tax

    def calculate_fourth_bracket(self, income):
        # for income in $6,660-$8,880, the tax is 5% times the amount exceding $6,660 plus $212
        self.tax += self.calculate_third_bracket(6660)
        self.tax += (income - 6660)*0.05
        return self.tax

    def calculate_fifth_bracket(self, income):
        # for income in $8,880-$11,100, the tax is 6% times the amount exceding $8,880 plus $323
        self.tax += self.calculate_fourth_bracket(8880)
        self.tax += (income - 8880)*0.06
        return self.tax

    def calculate_sixth_bracket(self, income):
        # for income over $11,100, the tax is 7% times the amount exceding $11,100 plus $456
        self.tax += self.calculate_fifth_bracket(11100)
        self.tax += (income - 11100)*0.07
        return self.tax

    def calculate_tax(self):
        if self.income <= 2220:
            return self.calculate_first_bracket(self.income)
        elif self.income <= 4440:
            return self.calculate_second_bracket(self.income)
        elif self.income <= 6660:
            return self.calculate_third_bracket(self.income)
        elif self.income <= 8880:
            return self.calculate_fourth_bracket(self.income)
        elif self.income <= 11100:
            return self.calculate_fifth_bracket(self.income)
        else:
            return self.calculate_sixth_bracket(self.income)

        
class NewRegime:
    """
    Calculate the income tax based on new tax rate brackets in 2022
    """
    def __init__(self,income):
        self.income = income
        self.tax = 0

    def calculate_first_bracket(self, income):
        # for income in $0-$3,200, the tax is 0% times the amount
        self.tax += self.tax*0
        return self.tax

    def calculate_second_bracket(self, income):
        # for income in $3,200-$16,040, the tax is 3% times the amount exceding $3200
        self.tax += self.calculate_first_bracket(3200)
        self.tax += (income - 3200)*0.03
        return self.tax

    def calculate_third_bracket(self, income):
        # for income $16,040 or more, the tax is 3% times ($16040-$3200) pulus 6.5% times the amount exceding $16040
        self.tax += self.calculate_second_bracket(16040)
        self.tax += (income - 16040)*0.065
        return self.tax

    def calculate_tax(self):
        if self.income <= 3200:
            return 0
        elif self.income <= 16040:
            return self.calculate_second_bracket(self.income)
        else:
            return self.calculate_third_bracket(self.income)

def compare(income, deduction):
    old_tax = 0
    new_tax = 0
    old_taxable_income = 0
    new_taxable_income = 0
   
    if income <= 3200:
        new_tax = 0
    else:
        old_taxable_income = income - deduction
        new_taxable_income = income - deduction

    # Old regime
    OR = OldRegime(old_taxable_income)
    old_tax = OR.calculate_tax()

    # New regime
    NR = NewRegime(new_taxable_income)
    if new_taxable_income <= 3200:
        new_tax = 0
    else:
        new_tax = NR.calculate_tax()
    
    return old_tax, new_tax

if __name__ == "__main__":
    income = int(input("Enter your income: "))
    deduction = int(input("Enter your deduction: "))
    old_tax, new_tax = compare(income, deduction)

    print("Old tax is ${}".format(round(old_tax)))
    print("New tax is ${}".format(round(new_tax)))

    if new_tax > old_tax:
        print("New tax is higher with difference ${}.".format(round(new_tax - old_tax)))
    elif new_tax < old_tax:
        print("Old tax is higher with difference ${}.".format(round(old_tax - new_tax)))
    else:
        print("The two regime produces the same amount of tax.")





    
