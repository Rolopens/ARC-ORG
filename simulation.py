def normalConversion(deciNumber, negBit):
    #still need to fix this part
    binNumber = bin(int(deciNumber))
    binNumber = binNumber[2:]
    print(binNumber)
    binExp = len(binNumber) - 1
    print(binExp)
    ePrime = bin(binExp + 1023)
    ePrime = "00000000000" + ePrime[2:]
    ePrime = ePrime[-11:]
    print(ePrime)
    binNumber = binNumber[1:] + "0000000000000000000000000000000000000000000000000000"
    binNumber = binNumber[:52]
    result = negBit + ePrime + binNumber
    result = hex(int(result, 2))
    print(result)

def zeroCase():
    print( "0x" + "0" * 16)

def NaNCase(deciNumber, negBit):
    print("TODO: NaN Case")

def denormalizedCase(deciNumber, negBit):
    print("TODO: Denormalized Case")

def main():
    deciInput = input("Input decimal mantissa: ")
    deciExpInput = input("Input exponent (10^x): ")

    deciInput = float(deciInput)
    deciExpInput = int(deciExpInput)

    if (deciInput >0):
        negBit = "0"
        deciNumber = deciInput * 10 ** deciExpInput   
        normalConversion(deciNumber, negBit)
    elif(deciInput < 0):
        negBit = "1"
        deciNumber = deciInput * 10 ** deciExpInput * -1
        normalConversion(deciNumber, negBit)
    elif(deciInput == 0):
        zeroCase()

main()
