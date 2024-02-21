from farmhash import FarmHash32, FarmHash64, FarmHash128
FarmHash32("abc")
FarmHash128('abc')

import cityhash

import cityhash

def CITYHASH(K, l, S):
    # Using CityHash function from the cityhash library
    return FarmHash32(bytes(str(K) + str(int(l)) + str(int(S)), 'utf-8'))

'''
def GENPRNG(K, l, S, β):
    i = 0
    bin_result = []

    while β >= 1:
        d = CITYHASH(K, l, S)
        K = d
        l = len(str(K))
        e = CITYHASH(K, l, S)
        K = int(str(d) + str(e))
        l = len(str(K))
        S = abs(d - e)
        bin_result.extend([int(b) for b in bin(d & 0xFFFFFFFF)[2:].zfill(32)])
        β -= 1
        i += 1

    return bin_result

# Example usage:

K_example = '123456'
l_example = len(str(K_example))
S_example = 42
β_example = 10 '''



#result = GENPRNG(K_example, l_example, S_example, β_example)
#print(result)

def _random(s0,s1):
  x, y = s0, s1
  x = x ^ ((x << 23) & 0xFFFFFFFFFFFFFFFF)  # 64bit
  x = (x ^ (x >> 17)) ^ (y ^ (y >> 26))
  s0, s1 = y, x
  return [s0 + s1]

#print(_random(100, 300))

def ROTATELEFT(bits, shift):
    return (bits[shift:] + bits[:shift])

def ROTATERIGHT(bits, shift):
    return (bits[-shift:] + bits[:-shift])


def CONVERTTOSTRING(value):
    # Simple conversion to string, replace with an actual implementation if needed
    return str(value)


def BITWISE_XOR(bits1, bits2):
    # Perform bitwise XOR on corresponding bits
    return [a ^ b for a, b in zip(bits1, bits2)]


def GENHASH(K, β):
    S = int(98899)
    S ^= β
    μ = 2
    δ = 17
    l = len(K)

    ζ = _random(S, l)  # Generate initial hash value ζ using a PRNG
    K_prime = FarmHash128(bytes(str(K) + str(int(l)) + str(int(S)), 'utf-8'))  # Compute K_prime using FarmHash

    t = (K_prime % δ) + μ

    i = 0
    packed_ζ = pack_bits(ζ)  # Pack the bits of ζ into a compact array

    hash_bits = []  # List to store the bits of the hash

    while t >= 1:
        S_prime = S ^ K_prime
        r = K_prime % β

        # Ensure we're within the bounds of packed_ζ
        if i < len(packed_ζ):
            bit = packed_ζ[i]

            if bit == 1:
                ζ = ROTATELEFT(ζ, r)
            else:
                ζ = ROTATERIGHT(ζ, r)

        K = CONVERTTOSTRING(K_prime)
        l = len(str(K))
        K_prime = FarmHash128(bytes(str(int(K)) + str(int(l)) + str(int(S_prime)), 'utf-8'))
        P = _random(S_prime, l)
        ζ = BITWISE_XOR(ζ, P)
        t -= 1
        i += 1

        # Convert ζ to binary and append to hash_bits
        hash_bits.extend(decimal_to_binary(ζ[0]))

    # Convert hash_bits to hexadecimal
    hash_hex = binary_to_hex(hash_bits[:128])
    #print("Character at position 63:", hash_hex[63])
    #print("Substring around position 63:", hash_hex[60:66])

    #return hash_hex
    return bytes.fromhex(hash_hex)

    #return bytes.fromhex(hash_hex[0][2:])
    # Return hexadecimal hash value


def binary_to_hex(binary_list):
    binary_str = ''.join(map(str, binary_list))  # Convert the list of bits to a binary string
    hex_value = hex(int(binary_str, 2))[2:]  # Convert binary string to hexadecimal
    return hex_value

def pack_bits(bits):
    packed = []
    current_byte = 0
    bit_index = 0

    for bit in bits:
        current_byte |= (bit << bit_index)
        bit_index += 1

        if bit_index == 8:
            packed.append(current_byte)
            current_byte = 0
            bit_index = 0

    if bit_index > 0:
        packed.append(current_byte)

    return packed


def pack_bits(bits):
    packed = []
    current_byte = 0
    bit_index = 0

    for bit in bits:
        current_byte |= (bit << bit_index)
        bit_index += 1

        if bit_index == 8:
            packed.append(current_byte)
            current_byte = 0
            bit_index = 0

    if bit_index > 0:
        packed.append(current_byte)

    return packed

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'  # Special case: decimal 0 is binary 0

    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Example usage:
K_example = "OSHA"  # Replace with your actual input value
β_example = 256  # Replace with your actual β value
S = 98899
l = len(K_example)
result = GENHASH(K_example, β_example)
print(result)





'''
def GENHASH(K, β, μ=5, δ=17):
    l = len(str(K))
    S = int(42)  # Initialize S as an integer number
    S ^= β

    ζ = GENPRNG(K, l, S, β)

    K_prime = FarmHash32(bytes(str(K) + str(int(l)) + str(int(S)), 'utf-8'))

    t = (K_prime % δ) + μ

    i = 0

    while t >= 1:
        S_prime = S ^ K_prime
        r = K_prime % β

        if i < len(ζ) and ζ[i] == 1:
          ζ = ROTATELEFT(ζ, r)
        else:
          ζ = ROTATERIGHT(ζ,r)

        K = CONVERTTOSTRING(K_prime)
        l = len(str(K))
        K_prime = FarmHash32(bytes(str(int(K)) + str(int(l)) + str(int(S_prime)) , 'utf-8'))
        P = GENPRNG(int(K), l, int(S_prime), β)
        ζ = BITWISE_XOR(ζ, P)
        t -= 1
        i +=1

    ζ = ζ[:256] + [0] * (256 - len(ζ))

    return bytes(ζ)
'''
# Example usage:
'''
def GENHASH(K, β):
    l = len(str(K))
    S = int(98899)  # Initialize S as an integer number
    S ^= β
    μ=2
    δ=17

    #ζ = GENPRNG(K, l, S, β)
    ζ = _random(S , l)

    K_prime = FarmHash32(bytes(str(K) + str(int(l)) + str(int(S)), 'utf-8'))

    t = (K_prime % δ) + μ

    i = 0

    while t >= 1:
        S_prime = S ^ K_prime
        r = K_prime % β

        if i < len(ζ) and ζ[i] == 1:
          ζ = ROTATELEFT(ζ, r)
        else:
          ζ = ROTATERIGHT(ζ,r)

        K = CONVERTTOSTRING(K_prime)
        l = len(str(K))
        K_prime = FarmHash32(bytes(str(int(K)) + str(int(l)) + str(int(S_prime)) , 'utf-8'))
        #P = GENPRNG(int(K), l, int(S_prime), β)
        P = _random(S_prime , l)
        ζ = BITWISE_XOR(ζ, P)
        t -= 1
        i +=1

    #ζ = ζ[:256] + [ζ] * (256 - len(ζ))
    r = ζ[0]
    digit_list = [int(digit) for digit in str(r)]

    return bytes(digit_list)

# Example usage:
K_example = "OSHA"  # Replace with your actual input value
β_example = 256  # Replace with your actual β value
S = 98899
l = len(K_example)
result = GENHASH(K_example, β_example)
#result = [hex(item) for item in result]
print(result)
'''

'''
K_example = "OSHA"  # Replace with your actual input value
β_example = 10  # Replace with your actual β value
result = HASH(K_example, β_example) '''
#print(result)'''
''''
def GENHASH(msg,β):
    l = len(msg)
    S = int(42)

    if l <= 64:
        ζ = HASH(msg, l, S, β)
    else:
        i = 0
        ζ = [0] * 256  # Assuming 256-bit output based on the usage in the provided code

        while i < l:
            m = msg[i:i + 64]
            P = HASH(m, len(m), S, β)
            ζ = BITWISE_XOR(ζ, P)
            i += 64

    α = hex(int(''.join(map(str, ζ)), 2))[2:]
    return bytes.fromhex(α)

# Example usage:
msg_example = "OSHA"  # Replace with your actual input message
S_example = 42  # Replace with your actual S value
β_example = 10  # Replace with your actual β value

result = GENHASH(msg_example, β_example)
print(result) '''