import WACC as c


def test():
    interestExpense = 3576
    STDebt = 0
    LTDebt = 91807
    expectedValue = 0.03895127822497195
    actualValue = c.calculateCostOfDebt(interestExpense, STDebt, LTDebt)

    assert expectedValue == actualValue
    print(actualValue)


test()