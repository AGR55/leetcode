numero = 10
otro_numero = 82

xor_result = numero ^ otro_numero

def count_set_bits(x) -> int:
    count: int = 0

    while x:
        count += x & 1
        x >>= 1

    return count

print(bin(otro_numero))
print(bin(numero))
print(bin(xor_result))
print(count_set_bits(xor_result))
