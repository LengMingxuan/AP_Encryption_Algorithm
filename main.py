import sys, getopt

def encode(s):
    l1 = []
    l2 = []
    for i,c in enumerate(s):
        if i % 2 == 0:
            l1.append(c)
        else:
            l2.append(c)
    l1 = l1[::-1]
    return ''.join(l2)+''.join(l1)

def decode(s):
    n = len(s)
    l2 = s[:n//2]
    l1 = s[n//2:]
    l1 = l1[::-1]
    l = []
    for i in range(max(len(l1), len(l2))):
        if i < len(l2):
            l.append(l1[i])
            l.append(l2[i])
        else:
            l.append(l1[i])
    return ''.join(l)

def encrypt(key, s):
    s = encode(s)
    b = bytearray(str(s).encode("gbk"))
    n = len(b) # 姹傚嚭 b 鐨勫瓧鑺傛暟
    c = bytearray(n*2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2閮芥槸0~15涔嬮棿鐨勬暟,鍔犱笂65灏卞彉鎴愪簡A-P 鐨勫瓧绗︾殑缂栫爜
        c[j] = c1
        c[j+1] = c2
        j = j+2
    return c.decode("gbk")

def decrypt(key, s):
    c = bytearray(str(s).encode("gbk"))
    n = len(c) # 璁＄畻 b 鐨勫瓧鑺傛暟
    if n % 2 != 0 :
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j+1]
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        b[i]= b1
    try:
        b = b.decode("gbk")
        return decode(b)
    except:
        return "failed"

def main(argv):
    key = 15
    s = ''
    type_ = True
    try:
        opts, args = getopt.getopt(argv,"hdes:",["istr="])
    except:
        print('test.py -e -s <string>')
        print('test.py -d -s <string>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -e -s <string>')
            print('test.py -d -s <string>')
            sys.exit(2)
        elif opt == "-e":
            type_ = True
        elif opt == "-d":
            type_ = False
        elif opt in ("-s", "--istr"):
            s = arg
        if type_:
            print(encrypt(key, s))
        else:
            print(decrypt(key, s))



if __name__ == '__main__':
    main(sys.argv[1:])
