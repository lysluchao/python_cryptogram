class rsa():
    def __init__(self):
        self.__m = 8 ; self.__p = 7;self.__q = 17;self.__e = 5

        self.__n = self.__p * self.__q
        self.__ola_n = (self.__p - 1) * (self.__q - 1)
        self.__d = 0

        # 求出公钥
        while (self.__d * self.__e) %self.__ola_n != (1 % self.__ola_n):
            self.__d += 1
            print(self.__d)
        print("公钥为{0} 明文为{1}".format(self.__d, self.__m))

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
