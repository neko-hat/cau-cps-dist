#  0x4d 0x76 0x50 0x50 0x76 0x2d 0x21 0x62 0x59 0x2d 0x15 0x12 0x04 0x3e 0x81 0x3e 0x6e 0x6e

temp = [0x4d, 0x76, 0x50, 0x50, 0x76, 0x2d, 0x21, 0x62, 0x59, 0x2d, 0x15, 0x12, 0x04, 0x3e, 0x81, 0x3e, 0x6e, 0x6e]

temp_de = [int(x) for x in temp]

print(temp_de)

temp_str = "".join([chr(x) for x in temp_de])
print(temp_str)

from math import gcd

def decrypt(cipher_text : list, pri_key : list):
    # p = c^d % 
    # to_list 
    plain_bytes = []
    for i in cipher_text:
        plain_bytes.append((i ** pri_key[1]) % pri_key[0])
        
    plain_text = "".join([chr(x) for x in plain_bytes])
     
    
    return plain_text
def setting(p : int, q : int):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_e(phi_n)
    d = find_d(phi_n, e)

    return n, e, d
def find_e(phi_n : int):
    e = 0
    for i in range(2, phi_n):
        if gcd(phi_n, i) == 1:
            e = i
            break
    return e

def find_d(phi_n, e):
    d = 0
    mod = 0
    while True:
        if mod == 1:
            break
        d += 1
        mod = (e * d) % phi_n

    return d

if __name__=="__main__":
    p = 11
    q = 13
    n, e, d = setting(p, q)
    pub_key = [n, e]
    pri_key = [n ,d]
    temp = [0x4d, 0x76, 0x50, 0x50, 0x76, 0x2d, 0x21, 0x62, 0x59, 0x2d, 0x15, 0x12, 0x04, 0x3e, 0x81, 0x3e, 0x6e, 0x6e]

    temp_de = [int(x) for x in temp]   
    
    temp_de_str = decrypt(temp_de, pri_key)
    
    print(temp_de_str)