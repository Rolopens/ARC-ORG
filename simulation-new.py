'''
LLAMAS, ANTONIO MIGUEL
LOPEZ, LUIS ENRICO
PENA, ROMEO MANUEL
ARC-ORG S17
'''

import struct

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
 
def binary64Converter(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)
 
def binaryToFloat(value):
    hx = hex(int(value, 2))   
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]
 
def manualExponent(mantissa, exp):
    isNegative = False
    listMan = list(str(mantissa))
    if listMan[0] == '-':
        del listMan[0]
        isNegative = True
    while exp != 0:
        if exp > 0:
            if listMan.index('.')==len(listMan)-1:
                listMan.append('0')
            inDot = listMan.index(".")
            listMan[inDot] = listMan[inDot+1]
            listMan[inDot+1] = '.'
            exp -= 1
        elif exp < 0:
            if listMan.index('.')==0:
                listMan.insert(0, '0')
            inDot = listMan.index(".")
            listMan[inDot] = listMan[inDot-1]
            listMan[inDot-1] = '.'
            exp += 1
    strMan = ""
    for x in listMan:
        strMan += x
    if isNegative:
        strMan = '-' + strMan
    return float(strMan)

def fillBin(binString):
    binList = list(binString)
    while len(binList) < 64:
        binList.insert(0, '0')
    binString = ""
    for x in binList:
        binString += x
    return binString

def fillHex(hexString):
    hexList = list(hexString)
    del hexList[0]
    del hexList[0]
    while len(hexList) < 16:
        hexList.insert(0, '0')
    hexString = ""
    for x in hexList:
        hexString += x
    return '0x' + hexString

# floats are represented by IEEE 754 floating-point format which are 
# 64 bits long (not 32 bits)
def main():
    deciInput = input("Input decimal mantissa: ")
    deciExpInput = input("Input exponent (10^x): ")
    deciInput = float(deciInput)
    deciExpInput = int(deciExpInput)
    overflowFlag = False

    try:
        inp = manualExponent(deciInput, deciExpInput)
        print(inp)

        # float to binary
        binstr = binary64Converter(inp)
    except OverflowError:
        overflowFlag = True	
	
    print('Binary:')
    if (overflowFlag == True):
        print ("0 11111111111 0000000000000000000000000000000000000000000000000000")
    elif (inp < 1.0 and inp > 0.0):
        binstr = fillBin(binstr)
        m = binstr[:10]
        e = binstr[10:]
        print('0 0' + m + ' ' + e + '\n')
    elif (inp > 0):
        binstr = fillBin(binstr)
        m = binstr[:11]
        e = binstr[11:]
        print('0 ' + m + ' ' + e + '\n')
    elif (inp < 0):
        binstrTruncate = binstr[1:]
        m = binstrTruncate[:11]
        e = binstrTruncate[11:]
        print('1 ' + m + ' ' + e + '\n')
    elif (inp == 0):
        print("0 00000000000 0000000000000000000000000000000000000000000000000000")

    print('Hexadecimal:')
    if (overflowFlag == True):
        print("0x7FF0000000000000")
    elif (inp < 1.0 and inp > 0.0):
        hexstr = (hex(int(binstr, 2)))
        print(fillHex(str(hexstr)))
        #print("00" + binstr + '\n')
    elif (inp > 0):
        hexstr = (hex(int(binstr, 2)))
        print(fillHex(str(hexstr)))
        #print('0' + binstr + '\n')
    elif (inp < 0):
        print(hex(int(binstr, 2)))
        #print(binstr + '\n')
    elif (inp == 0):
        print("0x0000000000000000")

main()
