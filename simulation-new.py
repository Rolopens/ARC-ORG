import struct

def main():
    deciInput = input("Input decimal mantissa: ")
    deciExpInput = input("Input exponent (10^x): ")

    deciInput = float(deciInput)
    deciExpInput = float(deciExpInput)

    product = deciInput * 10 ** deciExpInput

    print(product)

main()
