"""
References:
https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
https://www.geeksforgeeks.org/python-program-to-convert-decimal-to-hexadecimal/
"""

# Conversion table of remainders to hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

reverse_table = {'0': 0, '1': 1, '2': 2, '3': 3,
         '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, 'A': 10, 'B': 11,
         'C': 12, 'D': 13, 'E': 14, 'F': 15}

# decimal to binary version 1
def dec2bin(number: int):
    ans = ""
    if ( number == 0 ):
        return 0
    while ( number ):
        ans += str(number&1)
        number = number >> 1
     
    ans = ans[::-1]
 
    return ans

# Function to print binary number for the
# input decimal using recursion
def decimalToBinary(n): 
    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n//2)
    print(n%2, end=' ')
 

# Function calculates the decimal equivalent
# to given binary number
def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
    if(decimal <= 0):
        return ''
    remainder = decimal % 16
    return decimalToHexadecimal(decimal//16) + conversion_table[remainder]
 
# hexadecimal to decimal
def h2decimal(hexadecimal):
    res = 0
    size = len(hexadecimal) - 1 # computing max power value
    for num in hexadecimal:
        res = res + reverse_table[num]*16**size
        size = size - 1
    return res


 # TODO: check for negative decimal values


def main():
	# Test 1
    number = 60
    print(f"The binary of the number {number} is {dec2bin(number)}")

	# Test 2
    decimalToBinary(8)
    print("\n")
    decimalToBinary(18)
    print("\n")
    decimalToBinary(7)
    print("\n")

	# Test 3
    binaryToDecimal(100)
    binaryToDecimal(101)
    binaryToDecimal(1001)

    # Test 4
    decimal_number = 69
    print("The hexadecimal form of", decimal_number, "is", decimalToHexadecimal(decimal_number))

	# Test 5
    print(h2decimal("A7".strip().upper()))

    return
 
# driver code
if __name__ == "__main__":
    main()
