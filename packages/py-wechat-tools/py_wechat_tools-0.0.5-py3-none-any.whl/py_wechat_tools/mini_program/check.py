import hashlib


class Check:

    @staticmethod
    def message_push_check(token, signature, timestamp, nonce, echostr):
        """
        验证服务器地址的有效性
        用于消息接口配置域名时的校验方法

        微信官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html#option-url

        从get请求中获取这些参数，直接返回该接口的返回结果即可

        :param token: 开发者生成的token
        :param signature: 微信加密签名，signature结合了开发者填写的token参数和请求中的timestamp参数、nonce参数。
        :param timestamp: 时间戳
        :param nonce: 随机数
        :param echostr: 随机字符串
        :return: 校验通过直接返回随机字符串，校验不通过返回空字符串
        """

        arr = [token, timestamp, nonce]
        arr.sort()
        arr_str = "".join(arr)
        sha1 = hashlib.sha1(arr_str.encode())
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr
        return ""
