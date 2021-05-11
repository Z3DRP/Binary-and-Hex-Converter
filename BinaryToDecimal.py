#Binary to Decimal Conversion Class

class Binary_To_Decimal:
    """Convert Binary to its Decimal Form"""

    def __init__(self,binVal):
        self.setBinary(binVal)
        self._Error = ""
        self._DecimalConversion = ""

        if self.isValid():
            self._Steps = [] #empty list for steps
            self.ConvertToDecimal()

    def setBinary(self,Bval):
        self._strBinary = Bval
    def getBinary(self):
        return self._strBinary

    def isValid(self):
        valid = True
        try:
            self._Binary = str(self._strBinary)
            for digit in range(0,len(self._Binary)):
                if self._Binary[digit] != '0' and self._Binary[digit] != '1':
                    self._Error = "Binary must be all 1's or 0's"
                    valid = False
        except Exception:
            self._Error = "Invalid Format"
            valid = False
        return valid

    def getErrorMsg(self):
        return self._Error

    def ConvertToDecimal(self):
        newBin = ""
        index = 0
        posVal = 0 # test
        decimal = 0
        for x in self._Binary[::-1]:
            newBin += x
        while index < len(newBin): 
            if newBin[index] == "1":
                decimal += 2**index
                posVal = 2**index
                posVal = "{:12}".format(posVal)
                self._Steps.append(f"There is a {posVal} (2^{index}) in the value")
            index += 1
        self._DecimalConversion = str(decimal)

    def getResult(self):
        return self._DecimalConversion
    def getResultSteps(self):
        return self._Steps
                
