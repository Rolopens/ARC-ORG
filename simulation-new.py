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
 
# floats are represented by IEEE 754 floating-point format which are 
# 64 bits long (not 32 bits)
def main():
    deciInput = input("Input decimal mantissa: ")
    deciExpInput = input("Input exponent (10^x): ")
    deciInput = float(deciInput)
    deciExpInput = int(deciExpInput)

    inp = (deciInput * (10 ** deciExpInput));

    # float to binary
    binstr = binary64Converter(inp)
		
	
    print('Binary:')
    if (inp < 1.0 and inp > 0.0):
        print(hex(int(binstr, 2)))
        print("00" + binstr + '\n')
    elif (inp > 0):
        m = binstr[:11]
        e = binstr[11:]
        print('0 ' + m + ' ' + e + '\n')
    if (inp < 0):
        binstr = binstr[1:]
        m = binstr[:11]
        e = binstr[11:]
        print('1 ' + m + ' ' + e + '\n')
    if (inp == 0):
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
