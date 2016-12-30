# gcd - Greater Common Divisor
# gcd(357, 234) = 3


def native_gcd(a, b):
    best = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            best = i
    return best


def euclid_gcd(a, b):
    if b == 0:
        return a

    return euclid_gcd(b, a % b)


# print(native_gcd(357, 234))
print(euclid_gcd(28851538, 1183019)) # 17657
