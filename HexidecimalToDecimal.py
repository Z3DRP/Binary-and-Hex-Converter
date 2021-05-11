#Hexidecimal to Decimal Conversion Class

class Hexidecimal_To_Decimal:
    """Convert Hexidecimal to its Decimal Form"""

    def __init__(self,hexval):
        self.setHex(hexval)
        self._Error = ""
        self._DecimalConversion = ""

        if self.isValid():
            self._Steps = []
            self.ConvertToDecimal()


    def setHex(self,hexval):
        self._strHexidecimal = hexval
    def getHex(self):
        return self._strHexidecimal

    def isValid(self):
        validHex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        valid = True
        try:
            self._Hexi = str(self._strHexidecimal)
            for digit in range(0,len(self._Hexi)):
                if self._Hexi[digit].lower() not in validHex:
                    self._Error = "Hexidecimal numbers are 1-9 & A-F"
                    valid = False
        except Exception:
            self._Error = "Invalid Format"
            valid = False
        return valid

    def getErrorMsg(self):
        return self._Error

    def ConvertToDecimal(self):
        hexInt = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        hexLetr = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
        newHex = ""
        index = 0
        posVal = 0
        decimal = 0
        for x in self._Hexi[::-1]:
            newHex += x
        while index < len(newHex):
            if newHex[index] in hexInt:
                decimal += hexInt[newHex[index]] * 16**index
                posVal = hexInt[newHex[index]] * 16**index
            elif newHex[index].lower() in hexLetr:
                decimal += hexLetr[newHex[index]] * 16**index
                posVal = hexLetr[newHex[index]] * 16**index
            posVal = "{:12}".format(posVal)
            self._Steps.append(f"There is a(n) {posVal} in the number (16^{index})")
            index += 1
        self._DecimalConversion = str(decimal)

    def getResult(self):
        return self._DecimalConversion
    def getResultSteps(self):
        return self._Steps
                
                

        
