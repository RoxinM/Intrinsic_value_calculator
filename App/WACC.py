# Calculating the Weighted average cost of capital(WACC)

import utilities as util
class WACC:

    interestExpense = STDebt = LTDebt = -1
    costOfDebt = -1
    incomeTaxExpense = incomeBeforeTax = -1
    effectiveTaxRate = -1
    costOfDebtFinal = -1

    riskFreeRate = beta = -1
    marketReturn = 0.0815
    costOfEquity = -11

    totalDebt = marketCap = -1
    weightOfDebt = weightOfEquity = -1

    wacc = -1

    # ----------------------Calculating Cost Of Debt-----------------------------
    def calculateCostOfDebt(self):
        try:
            self.interestExpense = util.getFloat("Interest Expense")
            self.STDebt = util.getFloat("STDebt")
            self.LTDebt = util.getFloat("LTDebt")

            self.costOfDebt = self.interestExpense/(self.STDebt+self.LTDebt)
            return self.costOfDebt
        except ZeroDivisionError:
            print("ERROR:Unable to calculate Cost Of Debt")
            print("\tSTDebt or LTDebt must be greater than 0")
            print("Inputs:\n\tInterest Expense: {}\n\tSTDebt: {}\n\tLTDebt: {}"
                  .format(self.interestExpense, self.STDebt, self.LTDebt))
            exit()
        except:
            print("ERROR:Unable to calculate Cost Of Debt")
            print("Inputs:\n\tInterest Expense: {}\n\tSTDebt: {}\n\tLTDebt: {}"
                  .format(self.interestExpense, self.STDebt, self.LTDebt))
            exit()


    def calculateEffectiveTaxRate(self):
        try:
            self.incomeTaxExpense = util.getFloat("Income Tax Expense")
            self.incomeBeforeTax = util.getFloat("Income Before Tax")

            self.effectiveTaxRate = self.incomeTaxExpense/self.incomeBeforeTax

            return self.effectiveTaxRate
        except ZeroDivisionError:
            print("ERROR:Unable to calculate Effective Tax Rate")
            print("\tIncome Before Tax must be greater than 0")
            print("Inputs:\n\tIncome Tax Expense: {}\n\tIncome Before Tax: {}"
                  .format(self.incomeTaxExpense, self.incomeBeforeTax))
            exit()

        except:
            print("ERROR:Unable to calculate Effective Tax Rate")
            print("Inputs:\n\tIncome Tax Expense: {}\n\tIncome Before Tax: {}"
                      .format(self.incomeTaxExpense,self.incomeBeforeTax))
            exit()


    def calculateCostOfDebtFinal(self):
        try:
            self.costOfDebtFinal = self.costOfDebt*(1-self.effectiveTaxRate)

            return self.costOfDebtFinal
        except:
            print("ERROR:Unable to calculate Cost Of Debt Final")
            print("Inputs:\n\tCost Of Debt: {}\n\tEffective Tax Rate: {}"
                      .format(self.costOfDebt,self.effectiveTaxRate))
            exit()


    # ----------------------Calculating Cost Of Equity -----------------------------
    def calculateCostOfEquity(self):
        try:
            # U.S treasury bond rates -Treasury Yield 10 year
            self.riskFreeRate = util.getFloat("Risk-Free-Rate")
            self.beta = util.getFloat("beta")
            # use 8.15%
            self.marketReturn = util.getFloat("Market Return")

            self.costOfEquity= (self.riskFreeRate) + ((self.beta)*(self.marketReturn-self.riskFreeRate))

            return self.costOfEquity
        except:
            print("ERROR:Unable to calculate Cost Of Equity")
            print("Inputs:\n\tRisk Free Rate: {}\n\tBeta: {}\n\tMarket Return: {}"
                      .format(self.riskFreeRate, self.beta, self.marketReturn))
            exit()



    # ----------------------Calculating Weight Of Debt and Equity -----------------------------
    def calculateWeightOfDebtAndEquity(self):
        try:
            self.totalDebt = self.STDebt + self.LTDebt
            self.marketCap = util.getFloat("Market Cap")

            self.weightOfDebt = self.totalDebt/(self.totalDebt+ self.marketCap)

            self.weightOfEquity = self.marketCap / (self.totalDebt + self.marketCap)

            return self.weightOfDebt, self.weightOfEquity

        except ZeroDivisionError:
            print("ERROR:Unable to calculate Weight Of Debt/ WeightOfEquity ")
            print("\teither STDebt or LTDebt or marketCap or totalDebt must be greater than 0")
            exit()
        except:
            print("ERROR:Unable to calculate Weight Of Debt")
            print("Inputs:\n\tTotal Debt: {}\n\tMarket Cap: {}"
                      .format(self.totalDebt, self.marketCap))
            exit()


    # ----------------------Calculating WACC -----------------------------
    def calculateWACC(self):
        try:
            self.wacc = self.weightOfDebt * self.costOfDebtFinal+ self.weightOfEquity * self.costOfEquity

            return self.wacc
        except:
            print("ERROR:Unable to calculate WACC")
            print("Inputs:\n\tCost Of Debt Final: {}\n\tCost Of Equity: {}\n\tWeight Of Debt: {}\n\tWeight Of Equity: {}"
                      .format(self.costOfDebtFinal, self.costOfEquity, self.weightOfDebt, self.weightOfEquity))
            exit()


