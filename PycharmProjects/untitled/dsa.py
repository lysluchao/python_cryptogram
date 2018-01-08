# p;q;g=pow(h,(p-1)/q)%p;y=pow(g,x)%p;r;

def dsa():
    q = 101
    p = 78 * 101 + 1
    h = 3
    g = pow(h, int((p - 1) / q)) % p
    x = 75
    y = pow(g, x) % p
    m = 89127873895
    # 随机数
    r = 50

    # 求出r的逆元
    reverse_r = 0
    while (reverse_r * r) % q != 1:
        reverse_r += 1
    # 签名
    t = (pow(g, r) % p) % q
    # 省略计算m的hash,用m原值代替
    s = ((m + x * t) * reverse_r) % q
    print("签名结果三元组 m:{0} s:{1} t:{2}".format(m, s, t))

    # 求出s的逆元
    reverse_s = 0
    while (reverse_s * s) % q != 1:
        reverse_s += 1
    # 验证
    w = reverse_s % q
    u1 = (m * w) % q
    u2 = (t * w) % q
    v = ((pow(g, u1) * pow(y, u2)) % p) % q
    if v == t:
        print("验证成功！")


dsa()
