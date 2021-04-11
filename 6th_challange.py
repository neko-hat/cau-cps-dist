"""hex code = 0x0003b971 0x000114f6 0x0001caef 0x0002e6c9 0x00043e9e 0x00043e9e 0x0003a621 0x00047021 0x00047bf4 0x0003b101 0x000352ce 0x00030c96 0x0003a621 0x00043e9e 0x00043e9e 0x0003a621 0x0002e6c9 0x0001bdf8 0x000352ce 0x0003142d0 0x002e6c90 0x00114f600 0x01caef00 0x047bf400 0x03b10100 0x02c07300 0x03b10100 0x0355f600 0x0355f6"""


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
    
    seq = "0003b971000114f60001caef0002e6c900043e9e00043e9e0003a6210004702100047bf40003b101000352ce00030c960003a62100043e9e00043e9e0003a6210002e6c90001bdf8000352ce0003142d0002e6c9000114f60001caef00047bf40003b1010002c0730003b101000355f6000355f6"
    length = 8
    print([seq[i:i+length] for i in range(0, len(seq), length)])

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
