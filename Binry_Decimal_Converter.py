#!user/bin/env python3
#Bin_Dec_Converter control program for Binary-Decimal conversions
#By - Zac Palmer

from DecimalToBinary import Decimal_To_Binary as DToB
from BinaryToDecimal import Binary_To_Decimal as BtoD
from DecimalToHexidecimal import Decimal_To_Hexidecimal as DtoH
from HexidecimalToDecimal import Hexidecimal_To_Decimal as HtoD

def main():
    print("Welcome to the Binary-Decimal Converter")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            #decimal to binary op
            print()
            value = str(input("Enter your decimal value : "))
            dec2bin = DToB(value) #instantiate the class with val
            
            if dec2bin.isValid():
                #display results of conversion
                for s in dec2bin.getResultSteps(): #'for each' style of loop for steps
                    print(s)
                print()
                print(f"ThereFore the Decimal value {dec2bin.getDecimal()}"
                      + f" converts to Binary: {dec2bin.getResult()}")
                print()
            else:
                print(f"Conversion Error : {dec2bin.getErrorMsg()}")
                print()
        elif choice == 2:
            #binary to decimal op
            print()
            value = str(input("Enter your Binary Value : "))
            bin2dec = BtoD(value)

            if bin2dec.isValid():
                for steps in bin2dec.getResultSteps():
                    print(steps)
                print()
                print(f"ThereFore the Binary value {bin2dec.getBinary()}" +
                      f" converts to Decimal : {bin2dec.getResult()}")
                print()
            else:
                print(f"Conversion Error : {bin2dec.getErrorMsg()}")
                print()
        #start of extra cred
        elif choice == 3:
            print()
            value = str(input("Enter your Decimal Value : "))
            dec2hex = DtoH(value)

            if dec2hex.isValid():
                for steps in dec2hex.getResultSteps():
                    print(steps)
                print()
                print(f"ThereFore the Decimal value {dec2hex.getDecimal()}"
                      + f" converts to Hexidecimal : {dec2hex.getResult()}")
                print()
            else:
                print(f"Conversion Error : {dec2hex.getErrorMsg()}")
                print()
        elif choice == 4:
            print()
            value = str(input("Enter your Hexidecimal Value : "))
            hex2dec = HtoD(value)

            if hex2dec.isValid():
                for steps in hex2dec.getResultSteps():
                    print(steps)
                print()
                print(f"ThereFore the Hexidecimal value {hex2dec.getHex()}"
                      + f" converts to Decimal {hex2dec.getResult()}")
                print()
            else:
                print(f"Conversion Error : {hex2dec.getErrorMsg()}")
                print()            
        else:
            print("Unknown Conversion Type")

        choice = getChoice()

    print()
    print("~Thanks for using the Binary-Decimal Converter~")



def getChoice():
    goodInput = False
    while not goodInput:
        try:
            choice = int(input("1=Decimal to Binary, 2=Binary to Decimal, 3=Decimal to Hexidecimal, 4=Hexidecimal to Decimal, 0=Quit : "))
            if choice < 0 or choice > 4:
                print("ERROR:Invalid Operation")
                goodInput = False
            else:
                goodInput = True
        except ValueError:
            print("ERROR:Unknown Operation 0,1,2,3,4 only")       
    return choice


if __name__ == "__main__":
    main()

