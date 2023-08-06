from py_wechat_tools.libs.tools import WeChatBase


class RiskControl(WeChatBase):

    def get_user_risk_rank(self, openid, scene=0, mobile_no=None, client_ip=None, email_address=None,
                           extended_info=None, is_test=None):
        """
        根据提交的用户信息数据获取用户的安全等级 risk_rank，无需用户授权。

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/safety-control-capability/riskControl.getUserRiskRank.html

        :param openid: 用户的openid
        :param scene: 场景值，0:注册，1:营销作弊，默认0
        :param mobile_no: 用户手机号
        :param client_ip: 用户访问源ip
        :param email_address: 用户邮箱地址
        :param extended_info: 额外补充信息
        :param is_test: false：正式调用，true：测试调用
        :return: 返回一个 WeChatData 类，包含：
                属性              类型              说明
                unoin_id        number           唯一请求标识，标记单次请求
                risk_rank       number           用户风险等级
        """
        url = "https://api.weixin.qq.com/wxa/getuserriskrank"

        params = self.check_params(
            access_token=self.access_token
        )
        par = locals()
        par.pop("self", None)
        data = self.check_params(appid=self.appid, **par)

        return self.post(url, params=params, data=data)
