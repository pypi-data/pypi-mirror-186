from py_wechat_tools.libs.tools import WeChatBase
import base64
import json
from Crypto.Cipher import AES


class Auth(WeChatBase):

    def decrypt(self, encryptedData, iv, sessionKey):
        """
        解析敏感数据（解析用户信息数据）
        :param encryptedData: 加密数据
        :param iv: 偏移值
        :param sessionKey: 微信 sessionKey，可以通过code2session方法更新
        :return: 解密后的数据
        """
        # base64 decode
        sessionKey = base64.b64decode(sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        if decrypted['watermark']['appid'] != self.appid:
            raise Exception('无效数据')
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

    def code2session(self, js_code):
        """
        登录，code换session

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html

        :param js_code: 通过小程序调用 wx.login() 方法获取的code
        :return: 返回WechatData对象对象包含参数：
                属性              类型              说明
                errcode         number          错误码，正常时返回0
                errmsg          str             错误描述，正常时返回ok
                openid          string          微信唯一id
                session_key     string          会话密钥
                unionid         string          用户在开放平台的唯一标识符，若当前小程序已绑定到微信开放平台帐号下会返回

        """
        url = "https://api.weixin.qq.com/sns/jscode2session"

        data = self.get_full_params(js_code=js_code, grant_type="authorization_code")
        result = self.get(url, params=data)
        return result

    def check_encrypted_data(self, encrypted_msg_hash):
        """
        检查加密信息是否由微信生成（当前只支持手机号加密数据），只能检测最近3天生成的加密数据

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/user-info/auth.checkEncryptedData.html

        :param encrypted_msg_hash: 加密数据的sha256，通过Hex（Base16）编码后的字符串
        :return: 返回WechatData对象对象包含参数：
                属性              类型              说明
                vaild          string           是否是合法的数据
                create_time     number	        加密数据生成的时间戳

        """
        url = "https://api.weixin.qq.com/wxa/business/checkencryptedmsg"
        data = self.check_params(encrypted_msg_hash=encrypted_msg_hash)
        params = self.check_params(access_token=self.access_token)

        result = self.post(url, data=data, params=params)
        return result

    def get_paid_union_id(self, openid, transaction_id=None, mch_id=None, out_trade_no=None):
        """
        用户支付完成后，获取该用户的 UnionId，无需用户授权。本接口支持第三方平台代理查询。

        以下两种方式任选其一。
        1、微信支付订单号（transaction_id）
        2、微信支付商户订单号和微信支付商户号（out_trade_no 及 mch_id）

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/user-info/auth.getPaidUnionId.html

        :param openid: 支付用户唯一标识
        :param transaction_id: 微信支付订单号（方法1必填）

        :param mch_id: 微信支付分配的商户号，和商户订单号配合使用（方法2必填）
        :param out_trade_no: 微信支付商户订单号，和商户号配合使用（方法2必填）

        :return:  返回WechatData对象对象包含参数：
                属性              类型              说明
                unionid          string          用户唯一标识，调用成功后返回
        """

        url = "https://api.weixin.qq.com/wxa/getpaidunionid"
        data = self.check_params(
            access_token=self.access_token,
            openid=openid,
            transaction_id=transaction_id,
            mch_id=mch_id,
            out_trade_no=out_trade_no
        )
        result = self.post(url, data=data)
        return result

    def get_plugin_open_pid(self, code):
        """
        小程序插件code换openid
        通过 wx.pluginLogin 接口获得插件用户标志凭证 code 后传到开发者服务器，开发者服务器调用此接口换取插件用户的唯一标识 openpid。

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/user-info/auth.getPaidUnionId.html

        :param code: 通过 wx.pluginLogin 接口获得插件用户标志凭证 code。
        :return:  返回WechatData对象对象包含参数：
                属性              类型              说明
                openid          string          微信唯一id

        """
        url = "https://api.weixin.qq.com/wxa/getpluginopenpid"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(code=code)

        result = self.get(url, params=params, data=data)
        return result

    def get_phone_number(self, code):
        """
        通过code 换手机号码

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/phonenumber/phonenumber.getPhoneNumber.html

        :param code: 通过getPhoneNumber方F法获取的手机号码专用code
        :return:   返回WechatData对象对象包含参数：
                属性                  类型              说明
                errcode             number	        错误码
                errmsg              string	        错误提示信息
                phone_info          Object	        用户手机号信息

            phone_info: 用户手机号信息
                属性                  类型              说明
                phoneNumber	        string	        用户绑定的手机号（国外手机号会有区号）
                purePhoneNumber	    string	        没有区号的手机号
                countryCode	        string	        区号
                watermark	        Object	        数据水印

            watermark：数据水印
                属性                  类型              说明
                appid	            string	        小程序appid
                timestamp	        number	        用户获取手机号操作的时间戳
        """
        url = "https://api.weixin.qq.com/wxa/business/getuserphonenumber"

        access_token = self.access_token

        params_data = self.check_params(access_token=access_token)
        data = self.check_params(code=code)

        result = self.post(url, data=data, params=params_data)
        return result
