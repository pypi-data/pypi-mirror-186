import datetime
from pprint import pprint

from py_wechat_tools.libs.tools import dict2obj, WeChatBase


# 小程序直播
class Broadcast(WeChatBase):

    def create_room(
            self,
            name: str,
            coverImg: str,
            startTime: datetime.datetime,
            endTime: datetime.datetime,
            anchorName: str,
            anchorWechat: str,
            shareImg: str,
            feedsImg: str,
            subAnchorWechat: str = None,
            createrWechat: str = None,
            isFeedsPublic: int = 1,
            type: int = 0,
            closeLike: int = 0,
            closeGoods: int = 0,
            closeComment: int = 0,
            closeReplay: int = 1,
            closeShare: int = 0,
            closeKf: int = 0,
    ):
        """
        创建直播间


        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.bankcard.html

        :param name: [必填] 直播间名字，最短3个汉字，最长17个汉字，1个汉字相当于2个字符
        :param coverImg: [必填] 背景图，1、填入mediaID（mediaID获取后，三天内有效）；图片 mediaID 的获取，请参考以下文档：
                         https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html；
                         直播间背景图，图片规则：建议像素1080*1920，大小不超过2M
                      * 注意：只支持mediaID，请先调用 wx.superresolution() 方法获取或者
        :param startTime: [必填] 直播计划开始时间（开播时间需要在当前时间的10分钟后 并且 开始时间不能在 6 个月后）
                          注意：开始时间不要正好偏移10分钟，因为请求过程中会消耗时间导致报错。
        :param endTime: [必填] 直播计划结束时间（开播时间和结束时间间隔不得短于30分钟，不得超过12小时，官方文档上的24小时是写错的）
                          注意：开播时间 = 结束时间 - 开始时间，记得加上开始时间的偏移量
        :param anchorName: [必填] 主播昵称，最短2个汉字，最长15个汉字，1个汉字相当于2个字符
        :param anchorWechat: [必填]主播微信号，如果未实名认证，需要先前往“小程序直播”小程序进行实名验证, 小程序二维码链接：
                             https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh
        :param shareImg: [必填] 分享图，填入mediaID（mediaID获取后，三天内有效）；图片 mediaID 的获取，请参考以下文档：
                         https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html；
                         直播间分享图，图片规则：建议像素800*640，大小不超过1M；
        :param feedsImg: [必填] 购物直播频道封面图，填入mediaID（mediaID获取后，三天内有效）；图片 mediaID 的获取，请参考以下文档：
                         https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html;
                         购物直播频道封面图，图片规则：建议像素800*800，大小不超过100KB；
        :param subAnchorWechat: [默认None]主播副号微信号，也要实名认证
        :param createrWechat: [默认None]创建者微信号，不传入则此直播间所有成员可见。传入则此房间仅创建者、管理员、超管、直播间主播可见
        :param isFeedsPublic: [默认：1]是否开启官方收录 【1: 开启，0：关闭】，默认开启收录
        :param type: [默认：0]直播间类型 【1: 推流，0：手机直播】
        :param closeLike: [默认：0]是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启）
        :param closeGoods: [默认：0]是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启）
        :param closeComment: [默认：0]是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启）
        :param closeReplay: [默认：1]是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启）
        :param closeShare: [默认：0]是否关闭分享 【0：开启，1：关闭】默认开启分享（直播开始后不允许修改）
        :param closeKf: [默认：0]是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启）

        :return: 返回 WeChatData 数据如下：
                属性              类型              说明
                errcode         int             错误代码（0表示正常）
                roomId	        int             房间ID
                qrcode_url      str             当主播微信号没有在 “小程序直播“ 小程序实名认证 返回该字段，值为一个认证的链接

        """
        prams = locals().copy()
        prams.pop("self")
        # 处理时间
        prams["startTime"] = int(prams["startTime"].timestamp())
        prams["endTime"] = int(prams["endTime"].timestamp())

        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/create"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(**prams)

        return self.post(url, params=params, data=data)

    def get_live_info(self, page: int = None, limit: int = None, room_id: int = None):
        """
        获取直播间列表和回放


        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/getLiveInfo.html

        :param page: [默认1] 页码，第几页
        :param limit: [默认10] 每页数量
        :param room_id: [选填] 直播间ID，传入表示获取回放

        :return: 返回 WeChatData 数据如下：

            属性              类型              说明
            room_info       list<obj>       房间信息，room_id == None时返回
            total           int             拉取房间总数
            live_replay     list<obj>             回放列表信息，room_id != None 时返回

            room_info对象:
                属性                  类型	            说明
                name                string	        直播间名称
                cover_img           string	        直播间背景图链接
                start_time          number	        直播间开始时间，列表按照start_time降序排列
                end_time            number	        直播计划结束时间
                anchor_name         string	        主播名
                roomid              number	        直播间ID
                goods               list	        商品
                live_status         number	        直播间状态。101：直播中，102：未开始，103已结束，104禁播，105：暂停，106：异常，107：已过期
                share_img           string	        直播间分享图链接
                live_type           number	        直播类型，1 推流 0 手机直播
                close_like          number	        是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启）
                close_goods         number	        是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启）
                close_comment	    number	        是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启）
                close_kf            number	        是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启）
                close_replay	    number	        是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启）
                is_feeds_public	    number	        是否开启官方收录，1 开启，0 关闭
                creater_openid	    string	        创建者openid
                feeds_img	        string	        官方收录封面

                goods对象：
                    属性                  类型	        说明
                    name                string	        商品名称
                    cover_img           string	        商品封面图链接
                    url                 string          商品小程序路径
                    price               number	        商品价格（分）
                    price2              number	        商品价格，使用方式看price_type
                    price_type          number	        价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传）
                    goods_id            number	        商品id
                    third_party_appid	string	        第三方商品appid ,当前小程序商品则为空

            live_replay对象：
                属性              类型          说明
                create_time     string      回放视频创建时间
                expire_time	    string	    回放视频 url 过期时间
                media_url	    string	    回放视频链接
        """

        url = "https://api.weixin.qq.com/wxa/business/getliveinfo"
        if not page or page < 1:
            page = 1
        if not limit or limit < 1:
            limit = 10

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(
            start=limit * (page - 1),
            limit=limit,
            action=None if room_id is None else "get_replay",
            room_id=room_id,
        )

        return self.post(url, params=params, data=data)

    def delete_room(self, room_id: int):
        """
        删除直播间

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/deleteRoom.html

        :param room_id: [必填] 直播间id
        :return: 返回 WeChatData：
        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/deleteroom"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(id=room_id)

        return self.post(url, params=params, data=data)

    def edit_room(
            self,
            room_id: int,
            name: str,
            coverImg: str,
            startTime: datetime.datetime,
            endTime: datetime.datetime,
            anchorName: str,
            anchorWechat: str,
            shareImg: str,
            feedsImg: str,
            isFeedsPublic: int = 1,
            closeLike: int = 0,
            closeGoods: int = 0,
            closeComment: int = 0,
            closeReplay: int = 1,
            closeShare: int = 0,
            closeKf: int = 0,
    ):
        """
        编辑直播间

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/editRoom.html

        :param room_id: [必填] 直播间id
        :param name: [必填] 直播间名字，最短3个汉字，最长17个汉字，1个汉字相当于2个字符
        :param coverImg: [必填] 背景图，1、填入mediaID（mediaID获取后，三天内有效）；图片 mediaID 的获取，请参考以下文档：
                         https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html；
                         直播间背景图，图片规则：建议像素1080*1920，大小不超过2M
                      * 注意：只支持mediaID，请先调用 wx.superresolution() 方法获取或者
        :param startTime: [必填] 直播计划开始时间（开播时间需要在当前时间的10分钟后 并且 开始时间不能在 6 个月后）
                          注意：开始时间不要正好偏移10分钟，因为请求过程中会消耗时间导致报错。
        :param endTime: [必填] 直播计划结束时间（开播时间和结束时间间隔不得短于30分钟，不得超过12小时，官方文档上的24小时是写错的）
                          注意：开播时间 = 结束时间 - 开始时间，记得加上开始时间的偏移量
        :param anchorName: [必填] 主播昵称，最短2个汉字，最长15个汉字，1个汉字相当于2个字符
        :param anchorWechat: [必填]主播微信号，如果未实名认证，需要先前往“小程序直播”小程序进行实名验证, 小程序二维码链接：
                             https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh
        :param shareImg: [必填] 分享图，填入mediaID（mediaID获取后，三天内有效）；图片 mediaID 的获取，请参考以下文档：
                         https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html；
                         直播间分享图，图片规则：建议像素800*640，大小不超过1M；
        :param feedsImg: [必填] 购物直播频道封面图，填入mediaID（mediaID获取后，三天内有效）；图片 mediaID 的获取，请参考以下文档：
                         https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html;
                         购物直播频道封面图，图片规则：建议像素800*800，大小不超过100KB；
        :param isFeedsPublic: [默认：1]是否开启官方收录 【1: 开启，0：关闭】，默认开启收录
        :param closeLike: [默认：0]是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启）
        :param closeGoods: [默认：0]是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启）
        :param closeComment: [默认：0]是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启）
        :param closeReplay: [默认：1]是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启）
        :param closeShare: [默认：0]是否关闭分享 【0：开启，1：关闭】默认开启分享（直播开始后不允许修改）
        :param closeKf: [默认：0]是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启）

        :return: 返回 WeChatData 数据如下：
                属性              类型              说明
                errcode         int             错误代码（0表示正常）
        """

        prams = locals().copy()
        prams.pop("self")
        prams["id"] = prams.pop('room_id')
        # 处理时间
        prams["startTime"] = int(prams["startTime"].timestamp())
        prams["endTime"] = int(prams["endTime"].timestamp())

        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/editroom"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(**prams)

        return self.post(url, params=params, data=data)

    def get_push_url(self, room_id: int):
        """
        获取直播间推流

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/getPushUrl.html

        :param room_id: [必填] 直播间id
        :return: 返回 WeChatData：
                属性              类型              说明
                pushAddr        string          推流地址

        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/getpushurl"

        params = self.check_params(access_token=self.access_token, roomId=room_id)

        return self.get(url, params=params)

    def get_shared_code(self, room_id: int, params: str = None):
        """
        获取直播间分享二维码

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/getSharedCode.html

        :param room_id: [必填] 直播间id
        :param params: [选填] 自定义参数
        :return: 返回 WeChatData：
                属性              类型              说明
                cdnUrl          string          分享二维码cdn url
                pagePath        string          分享路径
                posterUrl       string          分享海报 url

        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/getsharedcode"

        params = self.check_params(access_token=self.access_token, roomId=room_id, params=params)

        return self.get(url, params=params)

    def get_sub_anchor(self, room_id: int):
        """
        获取主播副号

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/getSubAnchor.html

        :param room_id: [必填] 直播间id
        :return: 返回 WeChatData：
                属性              类型              说明
                username        string          主播微信号

        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/getsubanchor"

        params = self.check_params(access_token=self.access_token, roomId=room_id)

        return self.get(url, params=params)

    def modify_sub_anchor(self, room_id: int, username: str):
        """
        获取主播副号

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/modifySubAnchor.html

        :param room_id: [必填] 直播间id
        :param username: [必填] 微信号
        :return: 返回 WeChatData：

        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/modifysubanchor"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(roomId=room_id, username=username)

        return self.post(url, params=params, data=data)

    def delete_sub_anchor(self, room_id: int):
        """
        删除主播副号

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/deleteSubAnchor.html

        :param room_id: [必填] 直播间id
        :return: 返回 WeChatData：

        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/deletesubanchor"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(roomId=room_id)

        return self.post(url, params=params, data=data)

    def add_sub_anchor(self, room_id: int, username: str):
        """
        添加主播副号

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/livebroadcast/studio-management/addSubAnchor.html

        :param room_id: [必填] 直播间id
        :param username: [必填] 微信号
        :return: 返回 WeChatData：

        """
        url = "https://api.weixin.qq.com/wxaapi/broadcast/room/addsubanchor"

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(roomId=room_id, username=username)

        return self.post(url, params=params, data=data)
