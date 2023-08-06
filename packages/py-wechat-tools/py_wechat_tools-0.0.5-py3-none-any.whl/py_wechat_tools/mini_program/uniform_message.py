from py_wechat_tools.libs.tools import dict2obj, WeChatBase


class MPTemplateMsg:
    template_id = None
    url = None
    miniprogram = None
    data = None
    appid = None

    def __init__(self, template_id: str, url: str, miniprogram: str, data: str):
        """
        微信公众号消息模板
        :param template_id: 公众号模板id
        :param url: 公众号模板消息所要跳转的url
        :param miniprogram: 公众号模板消息所要跳转的小程序，小程序的必须与公众号具有绑定关系
        :param data: 公众号模板消息的数据
        """
        self.template_id = template_id
        self.url = url
        self.miniprogram = miniprogram
        self.data = data


class UniformMessages(WeChatBase):

    def send(self, touser, mp_template_msg: MPTemplateMsg = None):
        """
        统一服务消息
        用户订阅公众号，通过公众号发送的统一服务消息

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/uniform-message/uniformMessage.send.html

        :param touser: 用户openid，可以是小程序的openid，也可以是mp_template_msg.appid对应的公众号的openid
        :param mp_template_msg:  MPTemplateMsg类型，公众号模板消息相关的信息，可以参考公众号模板消息接口
        :return:  返回 WeChatData 类型 返回包含
                属性	            类型	            说明
                errcode	        number	        错误码
                errmsg	        string	        错误信息
        """
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/uniform_send"
        params_data = self.check_params(access_token=self.access_token)

        mp_template_msg.appid = self.appid
        data = self.check_params(
            touser=touser,
            mp_template_msg=mp_template_msg.__dict__,
        )

        result = self.post(url, data=data, params=params_data)
        result_data = dict2obj(result.json())
        return result_data
