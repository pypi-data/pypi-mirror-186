from py_wechat_tools.libs.tools import WeChatBase


class ShortLink(WeChatBase):

    def generate(self, page_url, page_title=None, is_permanent=False):
        """
        获取小程序 Short Link，适用于微信内拉起小程序的业务场景。目前只开放给电商类目(具体包含以下一级类目：电商平台、商家自营、跨境电商)。
        通过该接口，可以选择生成到期失效和永久有效的小程序短链

        官方文档
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/short-link/shortlink.generate.html

        :param page_url: 通过 Short Link 进入的小程序页面路径，必须是已经发布的小程序存在的页面，可携带 query，最大1024个字符
        :param page_title:  页面标题，不能包含违法信息，超过20字符会用... 截断代替
        :param is_permanent:  生成的 Short Link 类型，短期有效：false，永久有效：true
        :return:  返回 WeChatData 类型，包含
                属性	            类型	            说明
                link            string          短连接
        """
        url = "https://api.weixin.qq.com/wxa/genwxashortlink"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(
            page_url=page_url,
            page_title=page_title,
            is_permanent=is_permanent
        )

        return self.post(url, params=params, data=data)
