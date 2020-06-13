# Calculating the intrinsic value using the Graham Intrinsic Value Formula
import utilities as util
class GIV:

    eps = -1 # Earnings per share value
    pe = 7 # Price to earnings
    growthRate = -1
    growthRateMultiplier = 1
    corporateBondYield = 4.4
    AAABondYield = -1
    currentPrice = -1
    intrinsicValue = -1

    def calculateGiv(self):
        self.eps = util.getFloat("EPS")
        self.growthRate = util.getFloat("Growth Rate")
        self.AAABondYield = util.getFloat("AAA Bond Yield")

        grahamIntrinsicValue = (self.eps*(self.pe+(self.growthRate*self.growthRateMultiplier)
                                         )*self.corporateBondYield)/self.AAABondYield
        print(grahamIntrinsicValue)
