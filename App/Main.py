from WACC import WACC
from GIV import GIV
import utilities as util
def main():

    grahamIntrinsicValue = GIV.calculateGiv(GIV)

    companyName = util.getString("Company name")
    print(companyName)

    stockPrice = util.getFloat("current stock price")
    print(stockPrice)
    # ----------------------Cost Of Debt-----------------------------
    costOfDebt = WACC.calculateCostOfDebt(WACC)
    print(costOfDebt)

    effectiveTaxRate = WACC.calculateEffectiveTaxRate(WACC)
    print(effectiveTaxRate)

    costOfDebtFinal = WACC.calculateCostOfDebtFinal(WACC)
    print(costOfDebtFinal)

    # ----------------------Cost Of Equity -----------------------------

    costOfEquity = WACC.calculateCostOfEquity(WACC)
    print(costOfEquity)

    # ----------------------Calculating Weight Of Debt and Equity -----------------------------

    result=WACC.calculateWeightOfDebtAndEquity(WACC)
    weightOfDebt = result[0]
    weightOfEquity = result[1]
    print(weightOfDebt)
    print(weightOfEquity)

    wacc = WACC.calculateWACC(WACC)
    print(wacc)

companyName = ""
stockPrice = 0

main()