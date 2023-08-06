from py_wechat_tools.libs.tools import WeChatBase


class Soter(WeChatBase):

    def verify_signature(self, openid, json_string, json_signature):
        """
        SOTER 生物认证秘钥签名验证

        官方文档
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/soter/soter.verifySignature.html

        :param openid: 用户 openid
        :param json_string:  通过 wx.startSoterAuthentication 成功回调获得的 resultJSON 字段
        :param json_signature:  通过 wx.startSoterAuthentication 成功回调获得的 resultJSONSignature 字段
        :return:  返回 WeChatData 类型，包含
                属性	            类型	            说明
                is_ok           boolean         验证结果

        """
        url = "https://api.weixin.qq.com/cgi-bin/soter/verify_signature"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(
            openid=openid,
            json_string=json_string,
            json_signature=json_signature
        )

        return self.post(url, params=params, data=data)
