import struct
#Rolo's Version
#todo: everything


getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
 
def binary64Converter(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)
 
def binaryToFloat(value):
    hx = hex(int(value, 2))   
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]
 
def manualExponent(mantissa, exp):
    listMan = list(str(mantissa))
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
    return float(strMan)

# floats are represented by IEEE 754 floating-point format which are 
# 64 bits long (not 32 bits)
def main():
    deciInput = input("Input decimal mantissa: ")
    deciExpInput = input("Input exponent (10^x): ")
    deciInput = float(deciInput)
    deciExpInput = int(deciExpInput)

    inp = (deciInput * (10 ** deciExpInput));
    print(inp)
    inp = manualExponent(deciInput, deciExpInput)
    print(inp)

    # float to binary
    binstr = binary64Converter(inp)
		
	
    print('Binary:')
    if (inp < 1.0 and inp > 0.0):
        m = binstr[:10]
        e = binstr[10:]
        print('0 0' + m + ' ' + e + '\n')
    elif (inp > 0):
        m = binstr[:11]
        e = binstr[11:]
        print('0 ' + m + ' ' + e + '\n')
    elif (inp < 0):
        binstrTruncate = binstr[1:]
        m = binstrTruncate[:11]
        e = binstrTruncate[11:]
        print('1 ' + m + ' ' + e + '\n')
    elif (inp == 0):
        print("0x0000000000000000")

    print('Hexadecimal:')
    if (inp < 1.0 and inp > 0.0):
        print(hex(int(binstr, 2)))
        #print("00" + binstr + '\n')
    elif (inp > 0):
        print(hex(int(binstr, 2)))
        #print('0' + binstr + '\n')
    if (inp < 0):
        print(hex(int(binstr, 2)))
        #print(binstr + '\n')
    if (inp == 0):
        print("0x0000000000000000")

main()
