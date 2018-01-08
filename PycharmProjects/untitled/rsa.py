m = 10
p = 19
q = 23
n = p * q
ola_n = (p - 1) * (q - 1)
d = 0
e = 13
# 求出公钥
while (d * e) % ola_n != (1 % ola_n):
    d += 1
    print(d)
print("公钥为{0} 明文为{1}".format(d, m))
# 加密
c = pow(m, d) % n
# 解密
m = pow(c, e) % n
print("加密后 {0},解密后 {1}".format(c, m))
