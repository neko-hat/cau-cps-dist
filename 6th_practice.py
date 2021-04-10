"""hex code = 0x4d 0x76 0x50 0x50 0x76 0x2d 0x21 0x62 0x59 0x2d 0x15 0x12 0x04
0x3e 0x81 0x3e 0x6e 0x6e"""

from math import gcd

def setting(p : int, q : int):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_e(phi_n)
    d = find_d(phi_n, e)

    return n, e, d

def find_e(phi_n: int):
    e = 0
    for i in range(2, phi_n):
        if gcd(phi_n, i) == 1:
            e = i
            break

    return e

def find_d(phi_n, e):
    d = 0
    for i in range(2, phi_n):
        if (e * i) % phi_n == 1:
            d = i
            break

    return d

def decrypt(int_code : list, pri_key : list):
    plain_bytes = []
    for i in int_code:
        plain_bytes.append((i ** pri_key[1]) % pri_key[0])

    plain_text = "".join([chr(x) for x in plain_bytes])

    return plain_text

if __name__=="__main__":
    hex_code = [0x4d, 0x76, 0x50, 0x50, 0x76, 0x2d,
                0x21, 0x62, 0x59, 0x2d, 0x15, 0x12,
                0x04, 0x3e, 0x81, 0x3e, 0x6e, 0x6e]

    int_code = [int(x) for x in hex_code]

    p = 11
    q = 13
    n, e, d = setting(p, q)
    pub_key = [n, e]
    pri_key = [n, d]

    dec_plain = decrypt(int_code, pri_key)

    print(dec_plain)
