#Decimal to Hexidecimal Conversion Class

class Decimal_To_Hexidecimal:
    """Convert Decimal Numbers to its Hexidecimal Form"""

    def __init__(self,decVal):
        self.setDecimal(decVal)
        self._Error = ""
        self._HexidecimalConversion = ""

        if self.isValid():
            self._Steps = []
            self.ConvertToHex(self._Decimal)

    def setDecimal(self,dVal):
        self._StrDecimal = dVal
    def getDecimal(self):
        return self._StrDecimal

    def isValid(self):
        valid = True
        try:
            self._Decimal = int(self._StrDecimal)
            if self._Decimal <= 0:
                self._Error = "Decimal Value Must Be Positive"
                valid = False
        except Exception:
            self._Error = "Value Is Not An Integer"
            valid = False
        return valid

    def getErrorMsg(self):
        return self._Error

    def ConvertToHex(self,dval):
        hexVals = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",}
        remainder = dval % 16
        newVal = dval // 16
        dStr = "{:12}".format(dval)
        nStr = "{:12}".format(newVal)
        self._Steps.append(f"{dStr} divided by 16 = {nStr} W/ remainder of : {remainder}")

        #base case
        if newVal > 0:
            self.ConvertToHex(newVal)

        if remainder in hexVals:
            self._HexidecimalConversion += hexVals[remainder]
        else:
            self._HexidecimalConversion += str(remainder)


    def getResult(self):
        return self._HexidecimalConversion
    def getResultSteps(self):
        return self._Steps
