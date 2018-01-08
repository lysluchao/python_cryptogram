class rsa():
    __m = 8 ; __p = 7;__q = 17;__e = 5

    __n = __p * __q
    __ola_n = (__p - 1) * (__q - 1)
    __d = 0

    # 求出公钥
    while (__d * __e) % __ola_n != (1 % __ola_n):
        __d += 1
        print(__d)
    print("公钥为{0} 明文为{1}".format(__d, __m))

    def crytogram(self):
        # 加密
        c = pow(self.__m, self.__d) % self.__n
        # 解密
        m = pow(c, self.__e) % self.__n
        print("加密后 {0},解密后 {1}".format(c, m))

    def signature(self):
        # 签名
        s = pow(self.__m.__hash__(), self.__e) % self.__n
        print("签名结果 m{} s{}".format(self.__m, s))
        # 验证
        s1 = pow(s, self.__d) % self.__n
        print(s1 == self.__m)


k = rsa()
k.signature()
