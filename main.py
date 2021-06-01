import sys, getopt
###############################################################################################
# d = {d0,d1,d2,...,dn}设为长度为n的原始字符串，n为整数， l1 = {d2k,d2k-2,...,d0},                 #
# 其中0 ≤ k ≤ n/2,l2 = {d1,d3,...,d2k+1}, 其中0≤k≤n/2-1,ds = l1 + l2 设m为ds中任意               #
# 一个字符的二进制，还需要正整数k、N，作为加密所需的参数，c1、c2为m加密后的元素。先要对                    #
# m和k进行异或运算，再对N取模运算得到c1, 对m和k进行异或运算，再除以N取整，得到c2 .                       #
# c1 = m ⊕ k mod N ,c2 = m ⊕ k / N.                                                           #
# 解密过程为加密过程的逆向操作，具体操作为m = (c2 ×N + c1) ⊕ k.                                     #
###############################################################################################
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
    n = len(b) # 求出 b 的字节数
    c = bytearray(n*2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码
        c[j] = c1
        c[j+1] = c2
        j = j+2
    return c.decode("gbk")

def decrypt(key, s):
    c = bytearray(str(s).encode("gbk"))
    n = len(c) # 计算 b 的字节数
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
