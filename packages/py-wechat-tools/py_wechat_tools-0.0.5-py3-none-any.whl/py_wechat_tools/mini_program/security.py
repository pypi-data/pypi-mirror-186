from py_wechat_tools.libs.tools import dict2obj, WeChatBase


"""
异步校验图片/音频是否含有违法违规内容。

应用场景举例：

语音风险识别：社交类用户发表的语音内容检测；
图片智能鉴黄：涉及拍照的工具类应用(如美拍，识图类应用)用户拍照上传检测；电商类商品上架图片检测；媒体类用户文章里的图片检测等；
敏感人脸识别：用户头像；媒体类用户文章里的图片检测；社交类用户上传的图片检测等。 频率限制：单个 appId 调用上限为 2000 次/分钟，
            200,000 次/天；文件大小限制：单个文件大小不超过10M
"""


class Security(WeChatBase):

    def media_check_async(self, media_url, media_type, openid, scene=1):
        """
        异步校验图片/音频是否含有违法违规内容。

        不推荐使用，该方法识别算法还需优化，色情图片大致上能识别出来（别问哪来的色情图片），涉政图片很多没法识别。

        具体用法请看官方文档
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/sec-check/security.mediaCheckAsync.html

        异步接收推送配置官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html#option-url
        :param media_url: 要检测的图片或音频的url，支持图片格式包括 jpg , jepg, png, bmp, gif（取首帧），支持的音频格式包括mp3, aac, ac3, wma, flac, vorbis, opus, wav
        :param media_type:  1:音频;2:图片
        :param openid:  用户的openid（用户需在近两小时访问过小程序）
        :param scene:  场景枚举值（1 资料；2 评论；3 论坛；4 社交日志）
        :return:  返回 WeChatData 类型，包含
                属性	            类型	            说明
                trace_id        string          唯一请求标识，标记单次请求，用于匹配异步推送结果
        """
        url = "https://api.weixin.qq.com/wxa/media_check_async"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(
            media_url=media_url,
            media_type=media_type,
            version=2,
            openid=openid,
            scene=scene,
        )

        return self.post(url, params=params, data=data)

    def media_check_async_notify(self, data):
        """
        (异步通知)校验数据方法
        通过media_check_async_notify()校验异步通知接收到的数据是否来自官方

        :param data：接收到的数据
        :return: 返回 WeChatData 类型 返回信息：

                属性              类型              说明
                ToUserName	    string	        小程序的username
                FromUserName	string	        平台推送服务UserName
                CreateTime	    number	        发送时间
                MsgType	        string	        默认为：Event
                Event	        string	        默认为：wxa_media_check
                appid	        string	        小程序的appid
                trace_id	    string	        任务id
                version	        number	        可用于区分接口版本
                result	        object	        综合结果
                detail	        array	        详细检测结果

            detail包含多个策略类型的检测结果，策略类型的检查结果可能存在的属性如下
                属性              类型              说明
                strategy	    string	        策略类型
                errcode	        number	        错误码，仅当该值为0时，该项结果有效
                suggest	        string	        建议，有risky、pass、review三种值
                label	        number	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                                辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他
                prob	        number	        0-100，代表置信度，越高代表越有可能属于当前返回的标签（label）

            result综合了多个策略的结果给出了建议，包含的属性有
                属性              类型              说明
                suggest	        string	        建议，有risky、pass、review三种值
                label	        string	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                                辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他

        """
        if isinstance(data, str):
            data = dict2obj(data)
        if not isinstance(data, dict):
            raise ValueError("data非dict类型或json字符串")
        return dict2obj(data)

    def msg_sec_check(self, openid, scene, content, nickname=None, title=None, signature=None):
        """
        检查一段文本是否含有违法违规内容。
        不建议使用该接口作为可信任的检测，该接口很多违规关键词都可以通过，
        这里提供一个测试接口关键词，终端打开 python执行下面这条的语句即可获取:
            b'\xe6\xb3\x95\xe8\xbd\xae\xe5\xa4\xa7\xe6\xb3\x95\xe5\xa5\xbd'.decode("utf-8")
        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/sec-check/security.msgSecCheck.html
        :param openid: 用户的openid（用户需在近两小时访问过小程序）
        :param scene: 场景枚举值（1 资料；2 评论；3 论坛；4 社交日志）
        :param content: 需检测的文本内容，文本字数的上限为2500字，需使用UTF-8编码
        :param nickname: 用户昵称，需使用UTF-8编码
        :param title: 文本标题，需使用UTF-8编码
        :param signature: 个性签名，该参数仅在资料类场景有效(scene=1)，需使用UTF-8编码
        :return: 返回 WeChatData 类型 返回信息：
                属性              类型              说明
                errcode	        number	        错误码
                errmsg	        string	        错误信息
                trace_id	    string	        唯一请求标识，标记单次请求
                result	        object	        综合结果
                detail	        array	        详细检测结果

            result综合了多个策略的结果给出了建议，包含的属性有
                属性              类型              说明
                suggest	        string	        建议，有risky、pass、review三种值
                label	        string	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                                辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他

            detail包含多个策略类型的检测结果，策略类型的检查结果可能存在的属性如下
                属性              类型              说明
                strategy	    string	        策略类型
                errcode	        number	        错误码，仅当该值为0时，该项结果有效
                suggest	        string	        建议，有risky、pass、review三种值
                label	        number	        命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003
                                                辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他
                prob	        number	        0-100，代表置信度，越高代表越有可能属于当前返回的标签（label）
                keyword	        string	        命中的自定义关键词

        """
        url = "https://api.weixin.qq.com/wxa/msg_sec_check"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(
            version=2,
            openid=openid,
            scene=scene,
            content=content,
            nickname=nickname,
            title=title,
            signature=signature
        )

        return self.post(url, params=params, data=data, encoding="utf-8", ensure_ascii=False)
