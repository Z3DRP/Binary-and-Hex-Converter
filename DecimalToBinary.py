#Decimal to Binary Conversion Class

class Decimal_To_Binary:
    """Convert Decimal Numbers to its Binary Form"""

    def __init__(self,decVal):
        self.setDecimal(decVal)
        self._Error = ""
        self._BinaryConversion = ""
        
        if self.isValid():
            self._Steps = [] # empty list for all of the steps comments in conversion
            #self.ConvertToBinary() #regular loop for conversion steps
            self.ConvertByRecursion(self._Decimal)#parameter becomes local in method
            

    def setDecimal(self,dVal):
        #starting value in string form
        self._StrDecimal = dVal
    def getDecimal(self):
        return self._StrDecimal

    def isValid(self):
        valid = True
        try:
            self._Decimal = int(self._StrDecimal)
            if self._Decimal <= 0:
                self._Error = "Decimal Value Must Be A Postive Integer"
                valid = False
        except Exception:
            self._Error = "Value is not an int"
            valid = False
        return valid

    def getErrorMsg(self):
        return self._Error

    def ConvertToBinary(self):
        #conversion using simple loop *Not Recursion
        workVal = self._Decimal #copy of integer form of value
        while workVal > 0:
            remainder = workVal % 2 #reaminderr for current / 2
            newVal = workVal // 2
            #create step for this iteration....
            #shouldnt really format here, but easy in this case
            commentStr = "{:12}".format(workVal)
            ycommentStr = "{:12}".format(newVal)
            self._Steps.append(f"{commentStr} divided by 2 = {ycommentStr} with remainder of :")
            

            #build BinaryConversioin
            self._BinaryConversion = str(remainder) + self._BinaryConversion
            #reset workVal to next value after division by 2
            workVal = newVal

    def ConvertByRecursion(self,dval):
        #dval is the 'currenct'working value in decimal after devision by 2
        remainder = dval % 2 #remainder of division by 2 for current value
        newVal = dval // 2
        # x and y are comment str from above 
        x = "{:12}".format(dval)
        y = "{:12}".format(newVal)
        self._Steps.append(f"By recursion : {x} divided by 2 = {y} W/ remainder of : {remainder}")

        #recursive call if base case has not been reached
        if newVal > 0:
            self.ConvertByRecursion(newVal)

        #method ends by taking current remainder and putting it in final result
        self._BinaryConversion += str(remainder)
        #normal exit to prev instance of ConvertByRecursion method
        

    def getResult(self):
        return self._BinaryConversion

    def getResultSteps(self):
        return self._Steps #return list of steps
    
