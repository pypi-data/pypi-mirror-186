
from py_wechat_tools.libs.tools import WeChatBase


class SubscribeMessage(WeChatBase):

    def get_category(self):
        """
        获取小程序账号的类目

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/subscribe-message/subscribeMessage.getCategory.html

        :return: 返回 WeChatData 类型 返回包含
                属性	                    类型	                说明
                errcode	                number	            错误码
                errmsg	                string	            错误信息
                data	                array	            类目列表

            data: 个人模板列表结构
                属性	                    类型	                说明
                id	                    number	            类目id，查询公共库模版时需要
                name	                string	            类目的中文名
        """
        url = "https://api.weixin.qq.com/wxaapi/newtmpl/getcategory"

        params_data = self.check_params(
            access_token=self.access_token
        )

        return self.get(url, params=params_data)

    def get_pub_template_title_list(self, ids, start=0, limit=10):
        """
        获取帐号所属类目下的公共模板标题

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/subscribe-message/subscribeMessage.getPubTemplateTitleList.html

        :param ids: 类目 id，多个用逗号隔开
        :param start: 用于分页，表示从 start 开始。从 0 开始计数。
        :param limit: 用于分页，表示拉取 limit 条记录。最大为 30。
        :return: 返回 WeChatData 类型 返回包含
                属性	                    类型	                说明
                errcode	                number	            错误码
                errmsg	                string	            错误信息
                data	                array	            模板标题列表

            data: 个人模板列表结构
                属性	                    类型	                说明
                tid	                    number	            模版标题 id
                title	                string	            模版标题
                type	                number	            模版类型，2 为一次性订阅，3 为长期订阅
                categoryId	            number	            模版所属类目 id

        """
        url = "https://api.weixin.qq.com/wxaapi/newtmpl/getpubtemplatetitles"

        params_data = self.check_params(
            access_token=self.access_token,
            ids=ids,
            start=start,
            limit=limit,
        )

        return self.get(url, params=params_data)

    def get_pub_template_key_words_by_id(self, tid):
        """
        获取模板标题下的关键词列表

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/subscribe-message/subscribeMessage.getPubTemplateKeyWordsById.html

        :param tid: 模板标题 id，可通过接口获取
        :return: 返回 WeChatData 类型 返回包含
                属性	                    类型	                说明
                errcode	                number	            错误码
                errmsg	                string	            错误信息
                count	                number	            模版标题列表总数
                data	                array	            关键词列表

            data: 个人模板列表结构
                属性	                    类型	                说明
                kid	                    number	            关键词 id，选用模板时需要
                name	                string	            关键词内容
                example	                string	            关键词内容对应的示例
                rule	                string	            参数类型
        """
        url = "https://api.weixin.qq.com/wxaapi/newtmpl/getpubtemplatekeywords"

        params_data = self.check_params(
            access_token=self.access_token,
            tid=tid
        )

        return self.get(url, params=params_data)

    def get_template_list(self):
        """
        获取当前帐号下的个人模板列表

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/subscribe-message/subscribeMessage.getTemplateList.html
        :return: 返回 WeChatData 类型 返回包含
                属性	                    类型	                说明
                errcode	                number	            错误码
                errmsg	                string	            错误信息
                data	                array	            个人模板列表

            data: 个人模板列表结构
                属性	                    类型	                说明
                priTmplId	            string	            添加至帐号下的模板 id，发送小程序订阅消息时所需
                title	                string	            模版标题
                content	                string	            模版内容
                example	                string	            模板内容示例
                type	                number	            模版类型，2 为一次性订阅，3 为长期订阅
                keywordEnumValueList	Array	            枚举参数值范围

            keywordEnumValueList: 枚举参数值范围的结构
                属性	                    类型	                说明
                keywordCode	            string	            枚举参数的 key
                enumValueList	        Array	            枚举参数值范围列表
        """
        url = "https://api.weixin.qq.com/wxaapi/newtmpl/gettemplate"

        params_data = self.check_params(access_token=self.access_token)

        return self.get(url, params=params_data)

    def add_template(self, tid, kidList, sceneDesc=None):
        """
        添加个人消息模板

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/subscribe-message/subscribeMessage.addTemplate.html

        :param tid: 模板标题 id，可通过接口获取，也可登录小程序后台查看获取
        :param kidList: 开发者自行组合好的模板关键词列表，关键词顺序可以自由搭配（例如 [3,5,4] 或 [4,5,3]），最多支持5个，最少2个关键词组合
        :param sceneDesc: 服务场景描述，15个字以内
        :return: 返回 WeChatData 类型 返回包含
                属性	                    类型	                说明
                errcode	                number	            错误码
                errmsg	                string	            错误信息
                priTmplId	            string	            添加至帐号下的模板id，发送小程序订阅消息时所需
        """
        url = "https://api.weixin.qq.com/wxaapi/newtmpl/addtemplate"

        params_data = self.check_params(access_token=self.access_token)
        data = self.check_params(tid=tid, kidList=kidList, sceneDesc=sceneDesc)

        return self.post(url, params=params_data, data=data)

    def delete_template(self, priTmplId):
        """
        删除帐号下的个人模板
        :param priTmplId: 要删除的模板id
        :return: 返回 WeChatData 类型 返回包含
                属性	            类型	            说明
                errcode	        number	        错误码
                errmsg	        string	        错误信息
        """
        url = "https://api.weixin.qq.com/wxaapi/newtmpl/deltemplate"

        params_data = self.check_params(access_token=self.access_token)
        data = self.check_params(priTmplId=priTmplId)

        return self.post(url, params=params_data, data=data)

    def send(self, touser, template_id, data, page=None, miniprogram_state=None, lang="zh_CN"):
        """
        发送订阅消息
        小程序弹出授权，授权通过后发出的订阅消息，无需关注公众号

        :param touser: 接收者（用户）的 openid
        :param template_id: 所需下发的订阅模板id
        :param data: 点击模板卡片后的跳转页面，仅限本小程序内的页面。支持带参数,（示例index?foo=bar）。该字段不填则模板无跳转。
        :param page: 模板内容，格式形如 { "key1": { "value": any }, "key2": { "value": any } }
        :param miniprogram_state: 跳转小程序类型：developer为开发版；trial为体验版；formal为正式版；默认为正式版
        :param lang: 进入小程序查看”的语言类型，支持zh_CN(简体中文)、en_US(英文)、zh_HK(繁体中文)、zh_TW(繁体中文)，默认为zh_CN
        :return:  返回 WeChatData 类型 返回包含
                属性	            类型	            说明
                errcode	        number	        错误码
                errmsg	        string	        错误信息
        """
        url = "https://api.weixin.qq.com/cgi-bin/message/subscribe/send"
        params_data = self.check_params(access_token=self.access_token)
        data = self.check_params(
            touser=touser,
            template_id=template_id,
            data=data,
            page=page,
            miniprogram_state=miniprogram_state,
            lang=lang,
        )

        return self.post(url, data=data, params=params_data)
