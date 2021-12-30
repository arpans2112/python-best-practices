def decimalToBinary(n):
    return bin(n).replace("0b", "")

x = "0b000010100"
print(decimalToBinary(1<<0))
print(decimalToBinary(1<<1))
print(decimalToBinary(1<<2))
print(decimalToBinary(1<<3))


print(decimalToBinary(1<<5))
# print(x & bin(1<<5))


print(zerolistmaker(3))